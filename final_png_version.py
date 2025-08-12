#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
电源测试设备集成控制系统 - 最终版本
具有高质量PNG渐变背景
"""

import tkinter as tk
from tkinter import ttk
import os
import threading
import time

class PowerTestIntegrateSystem:
    """电源测试设备集成控制系统 - 支持PNG背景"""
    
    def __init__(self):
        """初始化系统"""
        # 创建主窗口
        self.root = tk.Tk()
        self.root.title("电源测试设备集成控制系统 - PNG背景版")
        self.root.geometry("1200x800")
        
        # 设置最小窗口尺寸
        self.root.minsize(800, 600)
        
        # 初始化变量
        self.bg_image = None
        self.buttons = []
        self.current_tab = 0
        
        # 创建背景和界面
        self.create_background()
        self.create_interface()
        self.start_time_update()
        
        # 窗口居中
        self.center_window()
        
        print("✅ 电源测试设备集成控制系统已启动（PNG背景版）")
    
    def create_background(self):
        """创建高质量背景"""
        # 创建全屏Canvas作为背景
        self.bg_canvas = tk.Canvas(self.root, highlightthickness=0)
        self.bg_canvas.pack(fill=tk.BOTH, expand=True)
        
        # 加载背景图片
        self.load_background_image()
        
        # 绘制初始背景
        self.draw_background()
        
        # 绑定窗口缩放事件
        self.root.bind('<Configure>', self.on_window_resize)
    
    def load_background_image(self):
        """加载背景图片"""
        image_files = [
            "gradient_background.png",    # 高质量PNG
            "gradient_simple.gif",        # 简化GIF
            "gradient_background.gif"     # 原始GIF
        ]
        
        for image_file in image_files:
            if os.path.exists(image_file):
                try:
                    if image_file.endswith('.png'):
                        # 加载PNG背景（需要PIL）
                        from PIL import Image, ImageTk
                        pil_image = Image.open(image_file)
                        # 预缩放到标准尺寸
                        pil_image = pil_image.resize((1200, 800), Image.Resampling.LANCZOS)
                        self.bg_image = ImageTk.PhotoImage(pil_image)
                        self.bg_format = 'png'
                        print(f"✅ 加载PNG背景: {image_file}")
                        return
                    else:
                        # 加载GIF背景
                        self.bg_image = tk.PhotoImage(file=image_file)
                        self.bg_format = 'gif'
                        print(f"✅ 加载GIF背景: {image_file}")
                        return
                        
                except Exception as e:
                    print(f"⚠️ 无法加载 {image_file}: {e}")
                    continue
        
        # 如果没有找到图片，使用Canvas渐变
        self.bg_image = None
        self.bg_format = 'canvas'
        print("📝 使用Canvas渐变背景")
    
    def draw_background(self):
        """绘制背景"""
        try:
            # 获取当前窗口尺寸
            self.root.update_idletasks()
            width = self.root.winfo_width()
            height = self.root.winfo_height()
            
            if width <= 1 or height <= 1:
                width, height = 1200, 800
            
            # 清除旧背景
            self.bg_canvas.delete("background")
            
            if self.bg_image:
                # 使用图片背景
                if self.bg_format == 'png':
                    # PNG背景 - 重新缩放以适应窗口
                    from PIL import Image, ImageTk
                    if hasattr(self, '_original_pil_image'):
                        pil_image = self._original_pil_image
                    else:
                        # 重新加载原始图片
                        pil_image = Image.open("gradient_background.png")
                        self._original_pil_image = pil_image
                    
                    # 缩放到当前窗口尺寸
                    scaled_image = pil_image.resize((width, height), Image.Resampling.LANCZOS)
                    self.bg_image = ImageTk.PhotoImage(scaled_image)
                
                # 在画布中心显示背景
                self.bg_canvas.create_image(width//2, height//2, 
                                          image=self.bg_image, 
                                          anchor='center', 
                                          tags="background")
            else:
                # Canvas渐变背景
                self.draw_canvas_gradient(width, height)
                
        except Exception as e:
            print(f"❌ 背景绘制错误: {e}")
            # 回退到简单渐变
            self.draw_canvas_gradient(width, height)
    
    def draw_canvas_gradient(self, width, height):
        """绘制Canvas渐变背景"""
        steps = min(100, height // 6)
        
        for i in range(steps):
            y1 = int(i * height / steps)
            y2 = int((i + 1) * height / steps)
            
            ratio = i / steps
            
            # 蓝色渐变
            start_r, start_g, start_b = 150, 200, 255
            end_r, end_g, end_b = 30, 60, 120
            
            r = int(start_r + (end_r - start_r) * ratio)
            g = int(start_g + (end_g - start_g) * ratio)
            b = int(start_b + (end_b - start_b) * ratio)
            
            color = f"#{r:02x}{g:02x}{b:02x}"
            
            self.bg_canvas.create_rectangle(0, y1, width, y2, 
                                          fill=color, outline=color,
                                          tags="background")
    
    def create_interface(self):
        """创建用户界面"""
        # 创建左侧按钮区域
        self.create_sidebar()
        
        # 创建主内容区域
        self.create_content_area()
        
        # 创建状态栏
        self.create_status_bar()
    
    def create_sidebar(self):
        """创建左侧边栏"""
        # 创建半透明的背景框
        sidebar_bg = self.bg_canvas.create_rectangle(
            20, 50, 250, 550,
            fill='#2C3E50', outline='#3498DB', width=2,
            tags="sidebar"
        )
        
        # 创建按钮
        button_configs = [
            ("电源控制", self.tab_power_control, "#E74C3C"),
            ("数据采集", self.tab_data_collection, "#3498DB"),
            ("参数设置", self.tab_parameter_setting, "#F39C12"),
            ("系统监控", self.tab_system_monitor, "#27AE60"),
            ("报告生成", self.tab_report_generation, "#9B59B6")
        ]
        
        self.buttons = []
        for i, (text, command, color) in enumerate(button_configs):
            y_pos = 80 + i * 80
            
            # 创建按钮背景
            btn_bg = self.bg_canvas.create_rectangle(
                35, y_pos, 235, y_pos + 60,
                fill=color, outline='white', width=2,
                tags=f"button_{i}"
            )
            
            # 创建按钮文本
            btn_text = self.bg_canvas.create_text(
                135, y_pos + 30,
                text=text,
                font=('Microsoft YaHei UI', 12, 'bold'),
                fill='white',
                tags=f"button_{i}"
            )
            
            # 绑定点击事件
            self.bg_canvas.tag_bind(f"button_{i}", "<Button-1>", 
                                  lambda e, cmd=command, idx=i: self.button_click(cmd, idx))
            
            self.buttons.append((btn_bg, btn_text))
        
        # 高亮第一个按钮
        self.highlight_button(0)
    
    def create_content_area(self):
        """创建主内容区域"""
        # 创建内容区域背景
        self.content_bg = self.bg_canvas.create_rectangle(
            280, 50, 1150, 650,
            fill='#34495E', outline='#3498DB', width=2,
            tags="content"
        )
        
        # 创建标题
        self.content_title = self.bg_canvas.create_text(
            715, 90,
            text="欢迎使用电源测试设备集成控制系统",
            font=('Microsoft YaHei UI', 18, 'bold'),
            fill='#ECF0F1',
            tags="content"
        )
        
        # 创建内容文本
        self.content_text = self.bg_canvas.create_text(
            715, 350,
            text="请从左侧选择功能模块开始使用",
            font=('Microsoft YaHei UI', 14),
            fill='#BDC3C7',
            tags="content"
        )
    
    def create_status_bar(self):
        """创建状态栏"""
        # 状态栏背景
        self.bg_canvas.create_rectangle(
            0, 720, 1200, 800,
            fill='#2C3E50', outline='#3498DB', width=1,
            tags="statusbar"
        )
        
        # 状态文本
        self.status_text = self.bg_canvas.create_text(
            100, 760,
            text="系统已就绪",
            font=('Microsoft YaHei UI', 10),
            fill='#ECF0F1',
            tags="statusbar"
        )
        
        # 时间显示
        self.time_text = self.bg_canvas.create_text(
            1100, 760,
            text="",
            font=('Microsoft YaHei UI', 10),
            fill='#ECF0F1',
            tags="statusbar"
        )
    
    def button_click(self, command, index):
        """按钮点击处理"""
        self.highlight_button(index)
        command()
        self.current_tab = index
    
    def highlight_button(self, index):
        """高亮指定按钮"""
        colors = ["#E74C3C", "#3498DB", "#F39C12", "#27AE60", "#9B59B6"]
        
        for i, (btn_bg, btn_text) in enumerate(self.buttons):
            if i == index:
                # 高亮选中的按钮
                self.bg_canvas.itemconfig(btn_bg, fill='#ECF0F1', outline=colors[i], width=3)
                self.bg_canvas.itemconfig(btn_text, fill=colors[i])
            else:
                # 还原其他按钮
                self.bg_canvas.itemconfig(btn_bg, fill=colors[i], outline='white', width=2)
                self.bg_canvas.itemconfig(btn_text, fill='white')
    
    def update_content(self, title, content):
        """更新内容区域"""
        self.bg_canvas.itemconfig(self.content_title, text=title)
        self.bg_canvas.itemconfig(self.content_text, text=content)
        self.bg_canvas.itemconfig(self.status_text, text=f"当前模块: {title}")
    
    # 各个功能模块
    def tab_power_control(self):
        """电源控制模块"""
        self.update_content("电源控制", "电源开关控制\n电压调节\n电流限制\n保护功能设置")
    
    def tab_data_collection(self):
        """数据采集模块"""
        self.update_content("数据采集", "实时电压采集\n实时电流采集\n功率计算\n数据记录")
    
    def tab_parameter_setting(self):
        """参数设置模块"""
        self.update_content("参数设置", "采样频率设置\n报警阈值设置\n通信参数配置\n用户权限管理")
    
    def tab_system_monitor(self):
        """系统监控模块"""
        self.update_content("系统监控", "设备状态监控\n温度监控\n故障诊断\n性能分析")
    
    def tab_report_generation(self):
        """报告生成模块"""
        self.update_content("报告生成", "测试报告生成\n数据导出\n图表制作\n打印预览")
    
    def start_time_update(self):
        """启动时间更新线程"""
        def update_time():
            while True:
                try:
                    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
                    if hasattr(self, 'time_text'):
                        self.bg_canvas.itemconfig(self.time_text, text=current_time)
                    time.sleep(1)
                except:
                    break
        
        time_thread = threading.Thread(target=update_time, daemon=True)
        time_thread.start()
    
    def on_window_resize(self, event):
        """窗口大小改变事件"""
        if event.widget == self.root:
            # 延迟重绘以避免频繁更新
            self.root.after(100, self.redraw_on_resize)
    
    def redraw_on_resize(self):
        """窗口缩放后重绘"""
        self.draw_background()
    
    def center_window(self):
        """窗口居中"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")
    
    def run(self):
        """运行程序"""
        self.root.mainloop()

def main():
    """主函数"""
    try:
        app = PowerTestIntegrateSystem()
        app.run()
    except Exception as e:
        print(f"❌ 程序运行错误: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
