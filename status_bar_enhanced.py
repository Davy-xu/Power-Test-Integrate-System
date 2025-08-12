#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
状态栏功能增强版本
实现底部空间预留和右边时间显示
"""
import tkinter as tk
from datetime import datetime
import time
import threading

class StatusBarEnhancedInterface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("状态栏增强版 - 底部间距和时间显示")
        self.root.geometry("1200x800")
        self.root.configure(bg='#1e1e1e')
        
        self.setup_ui()
        self.start_time_update()
        
    def setup_ui(self):
        """设置增强的UI界面"""
        # 创建主画布
        self.canvas = tk.Canvas(self.root, bg='#2d2d30', highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # 创建顶部标题区域
        self.create_header()
        
        # 创建主内容区域（预留底部65像素空间）
        self.create_main_content()
        
        # 创建增强的状态栏
        self.create_enhanced_status_bar()
        
        # 绑定窗口大小改变事件
        self.root.bind('<Configure>', self.on_window_resize)
        
    def create_header(self):
        """创建顶部标题"""
        self.canvas.create_text(
            50, 30, text="电源测试设备集成控制系统",
            font=('Microsoft YaHei', 18, 'bold'), 
            fill='white', anchor='w'
        )
        
        self.canvas.create_text(
            50, 55, text="状态栏增强版 - 底部间距和时间显示测试",
            font=('Microsoft YaHei', 12), 
            fill='#bdc3c7', anchor='w'
        )
        
    def create_main_content(self):
        """创建主内容区域"""
        # 获取画布尺寸
        self.root.update_idletasks()
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        
        # 主内容区域：顶部80像素，底部预留65像素（50+15）
        content_y = 80
        content_height = canvas_height - 80 - 65
        
        # 主内容背景
        self.content_bg = self.canvas.create_rectangle(
            20, content_y, canvas_width-20, content_y + content_height,
            fill='#3c3c3c', outline='#606060', width=2
        )
        
        # 内容标题
        self.canvas.create_text(
            50, content_y + 30,
            text="主要功能测试区域",
            font=('Microsoft YaHei', 16, 'bold'),
            fill='white', anchor='w'
        )
        
        # 功能说明
        features = [
            "✓ 界面底部预留65像素空间（50像素状态栏 + 15像素下边距）",
            "✓ 时间显示在状态栏右边缘，使用蓝色字体",
            "✓ 状态信息显示在状态栏左侧",
            "✓ 实时更新，每秒刷新时间显示",
            "✓ 响应窗口大小变化，自动调整布局",
            "✓ 现代化设计，符合专业软件界面标准"
        ]
        
        for i, feature in enumerate(features):
            self.canvas.create_text(
                50, content_y + 80 + i * 30,
                text=feature,
                font=('Consolas', 11),
                fill='#cccccc', anchor='w'
            )
            
    def create_enhanced_status_bar(self):
        """创建增强的状态栏（底部50像素高度 + 15像素下边距）"""
        # 获取画布尺寸
        self.root.update_idletasks()
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        
        # 状态栏位置：距离底部15像素，高度50像素
        status_y = canvas_height - 65  # 50(高度) + 15(下边距) = 65
        status_height = 50
        
        # 清除旧的状态栏元素
        self.canvas.delete("status_bar")
        
        # 状态栏背景
        self.status_bg = self.canvas.create_rectangle(
            0, status_y, canvas_width, status_y + status_height,
            fill='#404040', outline='#606060', width=1, tags="status_bar"
        )
        
        # 状态文本（左侧）
        self.status_text = self.canvas.create_text(
            20, status_y + 25, text="系统运行正常 | 准备就绪",
            font=('Microsoft YaHei', 12), fill='#cccccc', 
            anchor='w', tags="status_bar"
        )
        
        # 时间文本（右侧）- 蓝色字体，Consolas字体
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.time_text = self.canvas.create_text(
            canvas_width - 20, status_y + 25, text=current_time,
            font=('Consolas', 12, 'bold'), fill='#4a9eff',
            anchor='e', tags="status_bar"
        )
        
        print(f"📊 状态栏创建完成:")
        print(f"   - 位置: y={status_y}, 高度={status_height}")
        print(f"   - 底部边距: 15像素")
        print(f"   - 时间位置: x={canvas_width-20}")
        
    def update_time_display(self):
        """更新时间显示"""
        if hasattr(self, 'time_text'):
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.canvas.itemconfig(self.time_text, text=current_time)
            
        # 更新状态文本（演示动态状态）
        if hasattr(self, 'status_text'):
            status_messages = [
                "系统运行正常 | 准备就绪",
                "设备检测中 | 状态良好", 
                "数据传输正常 | 连接稳定",
                "性能监控中 | 运行流畅"
            ]
            status_index = int(time.time()) % len(status_messages)
            self.canvas.itemconfig(self.status_text, text=status_messages[status_index])
            
    def start_time_update(self):
        """启动时间更新线程"""
        def update_thread():
            while True:
                try:
                    self.root.after(0, self.update_time_display)
                    time.sleep(1)
                except:
                    break
                    
        thread = threading.Thread(target=update_thread, daemon=True)
        thread.start()
        
    def on_window_resize(self, event=None):
        """响应窗口大小改变"""
        if event and event.widget == self.root:
            # 延迟重建以避免频繁调用
            self.root.after(100, self.rebuild_layout)
            
    def rebuild_layout(self):
        """重建布局以适应新窗口尺寸"""
        try:
            # 重新创建主内容区域
            self.create_main_content()
            # 重新创建状态栏
            self.create_enhanced_status_bar()
        except Exception as e:
            print(f"❌ 布局重建失败: {e}")
            
    def run(self):
        """运行增强版界面"""
        print("🚀 状态栏增强版启动")
        print("📋 测试项目:")
        print("   1. 检查底部是否有65像素空间（50+15）")
        print("   2. 检查时间是否在右边缘显示为蓝色")
        print("   3. 检查时间是否每秒自动更新")
        print("   4. 调整窗口大小测试响应性")
        print("   5. 观察状态信息动态变化")
        print()
        
        self.root.mainloop()

if __name__ == "__main__":
    app = StatusBarEnhancedInterface()
    app.run()
