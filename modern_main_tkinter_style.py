"""
tkintertools风格主界面 - 蓝色渐变毛玻璃效果
按照tkintertools的设计风格，包含渐变背景和现代化按钮
"""
import tkinter as tk
from tkinter import ttk
from datetime import datetime
import sys
import os
import math

class GlassButton:
    """毛玻璃风格按钮"""
    
    def __init__(self, parent, text="", width=140, height=45,
                 bg_color='#5AA0F2', 
                 active_color='#70B0FF',
                 hover_color='#6AB0F8',
                 text_color='white',
                 font=('Microsoft YaHei', 11, 'normal'),
                 command=None):
        
        self.parent = parent
        self.text = text
        self.width = width
        self.height = height
        self.bg_color = bg_color
        self.active_color = active_color
        self.hover_color = hover_color
        self.text_color = text_color
        self.font = font
        self.command = command
        
        self.state = 'normal'
        self.canvas = None
        self.shape_id = None
        self.text_id = None
        
        self.create_button()
        
    def create_button(self):
        """创建毛玻璃按钮"""
        # 获取父组件背景色
        try:
            parent_bg = '#4A90E2'  # 使用蓝色背景
        except:
            parent_bg = '#4A90E2'
            
        # 创建Canvas
        self.canvas = tk.Canvas(
            self.parent,
            width=self.width + 4,
            height=self.height + 4,
            highlightthickness=0,
            bd=0,
            bg=parent_bg
        )
        
        self.draw_button()
        self.bind_events()
        
    def draw_button(self):
        """绘制按钮"""
        self.canvas.delete("all")
        
        # 根据状态选择颜色
        if self.state == 'active':
            fill_color = self.active_color
            outline_color = '#80C0FF'
        elif self.state == 'hover':
            fill_color = self.hover_color
            outline_color = '#80C0FF'
        else:
            fill_color = self.bg_color
            outline_color = '#6090D2'
        
        # 绘制圆角矩形
        x1, y1 = 2, 2
        x2, y2 = self.width + 2, self.height + 2
        radius = 12
        
        # 创建圆角矩形路径
        points = self.create_rounded_rect_points(x1, y1, x2, y2, radius)
        
        # 绘制背景
        self.shape_id = self.canvas.create_polygon(
            points,
            fill=fill_color,
            outline=outline_color,
            width=1,
            smooth=True
        )
        
        # 绘制文本
        text_x = (x1 + x2) // 2
        text_y = (y1 + y2) // 2
        
        self.text_id = self.canvas.create_text(
            text_x, text_y,
            text=self.text,
            font=self.font,
            fill=self.text_color,
            anchor='center'
        )
        
        # 绑定事件
        self.bind_shape_events()
    
    def create_rounded_rect_points(self, x1, y1, x2, y2, radius):
        """创建圆角矩形顶点"""
        points = []
        
        # 四个角的圆弧
        corners = [
            (x2 - radius, y1 + radius, 0, 90),      # 右上
            (x2 - radius, y2 - radius, 270, 360),   # 右下
            (x1 + radius, y2 - radius, 180, 270),   # 左下
            (x1 + radius, y1 + radius, 90, 180),    # 左上
        ]
        
        for cx, cy, start_angle, end_angle in corners:
            for angle in range(start_angle, end_angle + 1, 6):
                rad = math.radians(angle)
                x = cx + radius * math.cos(rad)
                y = cy + radius * math.sin(rad)
                points.extend([x, y])
        
        return points
    
    def bind_events(self):
        """绑定事件"""
        self.canvas.bind('<Button-1>', self.on_click)
        self.canvas.bind('<Enter>', self.on_enter)
        self.canvas.bind('<Leave>', self.on_leave)
    
    def bind_shape_events(self):
        """绑定形状事件"""
        if self.shape_id:
            self.canvas.tag_bind(self.shape_id, '<Button-1>', self.on_click)
        if self.text_id:
            self.canvas.tag_bind(self.text_id, '<Button-1>', self.on_click)
    
    def on_click(self, event):
        """点击事件"""
        if self.command:
            self.command()
    
    def on_enter(self, event):
        """鼠标进入"""
        if self.state != 'active':
            self.state = 'hover'
            self.draw_button()
            self.canvas.configure(cursor='hand2')
    
    def on_leave(self, event):
        """鼠标离开"""
        if self.state != 'active':
            self.state = 'normal'
            self.draw_button()
            self.canvas.configure(cursor='')
    
    def set_active(self, active=True):
        """设置激活状态"""
        self.state = 'active' if active else 'normal'
        self.draw_button()
    
    def pack(self, **kwargs):
        """布局方法"""
        self.canvas.pack(**kwargs)
    
    def place(self, **kwargs):
        """位置布局方法"""
        self.canvas.place(**kwargs)
    
    def grid(self, **kwargs):
        """网格布局方法"""
        self.canvas.grid(**kwargs)


class TkinterToolsInterface:
    """tkintertools风格主界面"""
    
    def __init__(self, root):
        self.root = root
        self.current_tab = 0
        self.version_label = None
        self.time_label = None
        self.tab_frames = {}
        self.buttons = []
        self.setup_window()
        self.create_interface()
        self.update_time()
    
    def setup_window(self):
        """设置窗口属性"""
        self.root.title("Power Test Integrate System - tkintertools Style")
        self.root.geometry("1200x800")
        
        # 创建渐变背景
        self.create_gradient_background()
        
        # 设置窗口最小尺寸
        self.root.minsize(1000, 600)
        
        # 让窗口在屏幕中央打开
        self.center_window()
    
    def create_gradient_background(self):
        """创建蓝色渐变背景"""
        # 创建Canvas作为背景
        self.bg_canvas = tk.Canvas(self.root, highlightthickness=0)
        self.bg_canvas.pack(fill=tk.BOTH, expand=True)
        
        # 绘制渐变背景
        self.root.after(100, self.draw_gradient)
    
    def draw_gradient(self):
        """绘制蓝色渐变"""
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        
        if width <= 1 or height <= 1:
            self.root.after(100, self.draw_gradient)
            return
            
        # 清除之前的渐变
        self.bg_canvas.delete("gradient")
        
        # 从深蓝到浅蓝的渐变
        for i in range(height):
            # 计算渐变颜色
            ratio = i / height
            # 从 #2E5BBA 到 #4A90E2
            r = int(0x2E + (0x4A - 0x2E) * ratio)
            g = int(0x5B + (0x90 - 0x5B) * ratio)
            b = int(0xBA + (0xE2 - 0xBA) * ratio)
            
            color = f"#{r:02x}{g:02x}{b:02x}"
            self.bg_canvas.create_line(0, i, width, i, fill=color, width=1, tags="gradient")
    
    def center_window(self):
        """将窗口居中显示"""
        self.root.update_idletasks()
        
        # 获取屏幕尺寸
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # 获取窗口尺寸
        window_width = 1200
        window_height = 800
        
        # 计算居中位置
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        
        # 设置窗口位置和大小
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    
    def create_interface(self):
        """创建界面"""
        # 主容器框架
        main_frame = tk.Frame(self.bg_canvas, bg='#4A90E2')
        main_frame.place(relx=0.5, rely=0.5, anchor='center', width=1100, height=720)
        
        # 标题区域
        self.create_title_area(main_frame)
        
        # 导航按钮区域
        self.create_navigation_area(main_frame)
        
        # 主内容区域
        self.create_content_area(main_frame)
        
        # 状态栏
        self.create_status_area(main_frame)
    
    def create_title_area(self, parent):
        """创建标题区域"""
        title_frame = tk.Frame(parent, bg='#4A90E2', height=80)
        title_frame.pack(fill=tk.X, padx=30, pady=(30, 10))
        title_frame.pack_propagate(False)
        
        # CVTE Logo (左侧)
        logo_frame = tk.Frame(title_frame, bg='#4A90E2', width=200)
        logo_frame.pack(side=tk.LEFT, fill=tk.Y)
        logo_frame.pack_propagate(False)
        
        # 检查是否存在CVTE logo图片
        logo_path = "CVTE logo1.png"
        if os.path.exists(logo_path):
            try:
                from PIL import Image, ImageTk
                # 加载并调整logo尺寸
                img = Image.open(logo_path)
                img = img.resize((160, 60), Image.Resampling.LANCZOS)
                self.logo_photo = ImageTk.PhotoImage(img)
                
                logo_label = tk.Label(logo_frame, image=self.logo_photo, bg='#4A90E2')
                logo_label.pack(expand=True)
            except ImportError:
                # 如果没有PIL，使用文字logo
                self.create_text_logo(logo_frame)
        else:
            # 使用文字logo
            self.create_text_logo(logo_frame)
        
        # 系统标题 (中央)
        title_label = tk.Label(
            title_frame,
            text="Power Test Integrate System",
            font=('Microsoft YaHei', 20, 'bold'),
            fg='white',
            bg='#4A90E2'
        )
        title_label.pack(expand=True, anchor='center')
        
        # 版本信息 (右侧)
        version_frame = tk.Frame(title_frame, bg='#4A90E2', width=200)
        version_frame.pack(side=tk.RIGHT, fill=tk.Y)
        version_frame.pack_propagate(False)
        
        version_text = "v3.0.0\ntkintertools Style"
        self.version_label = tk.Label(
            version_frame,
            text=version_text,
            font=('Microsoft YaHei', 9),
            fg='#E0E0E0',  # 浅灰色替代rgba
            bg='#4A90E2',
            justify=tk.RIGHT
        )
        self.version_label.pack(expand=True, anchor='e')
    
    def create_text_logo(self, logo_frame):
        """创建文字logo"""
        logo_label = tk.Label(
            logo_frame, 
            text="CVTE", 
            font=('Arial', 24, 'bold'),
            bg='#4A90E2', 
            fg='white'
        )
        logo_label.pack(expand=True)
    
    def create_navigation_area(self, parent):
        """创建导航按钮区域"""
        nav_frame = tk.Frame(parent, bg='#4A90E2', height=70)
        nav_frame.pack(fill=tk.X, padx=30, pady=10)
        nav_frame.pack_propagate(False)
        
        # 按钮容器 - 居中
        btn_container = tk.Frame(nav_frame, bg='#4A90E2')
        btn_container.pack(expand=True)
        
        # 创建导航按钮
        tab_names = ["测试主界面", "自定义功能", "仪器指令", "手动控制", "设备端口"]
        self.buttons = []
        
        for i, name in enumerate(tab_names):
            btn = GlassButton(
                btn_container,
                text=name,
                width=140,
                height=50,
                bg_color='#5AA0F2',
                active_color='#70B0FF',
                hover_color='#6AB0F8',
                font=('Microsoft YaHei', 11, 'normal'),
                command=lambda idx=i: self.switch_tab(idx)
            )
            btn.pack(side=tk.LEFT, padx=8, pady=10)
            self.buttons.append(btn)
            print(f"✅ 创建按钮: {name}")
        
        # 设置第一个按钮为激活状态
        self.buttons[0].set_active(True)
    
    def create_content_area(self, parent):
        """创建主内容区域"""
        self.content_frame = tk.Frame(parent, bg='#5A9AE8', relief='flat', bd=0)  # 使用浅蓝色替代rgba
        self.content_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=(0, 10))
        
        # 加载默认内容
        self.load_tab_content(0)
    
    def create_status_area(self, parent):
        """创建状态栏"""
        status_frame = tk.Frame(parent, bg='#4A90E2', height=40)
        status_frame.pack(fill=tk.X, padx=30, pady=(0, 20))
        status_frame.pack_propagate(False)
        
        # 版本信息 (左侧)
        version_info = self.get_version_info()
        version_label = tk.Label(
            status_frame,
            text=f"版本: {version_info}",
            font=('Microsoft YaHei', 9),
            fg='#E0E0E0',  # 浅灰色替代rgba
            bg='#4A90E2'
        )
        version_label.pack(side=tk.LEFT, pady=10)
        
        # 当前时间 (右侧)
        self.time_label = tk.Label(
            status_frame,
            text="",
            font=('Microsoft YaHei', 9),
            fg='#E0E0E0',  # 浅灰色替代rgba
            bg='#4A90E2'
        )
        self.time_label.pack(side=tk.RIGHT, pady=10)
    
    def get_version_info(self):
        """获取版本信息"""
        return "v3.0.0 - tkintertools风格"
    
    def update_time(self):
        """更新时间显示"""
        if self.time_label:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.time_label.config(text=current_time)
        
        # 每秒更新一次
        self.root.after(1000, self.update_time)
    
    def switch_tab(self, index):
        """切换标签"""
        # 重置所有按钮状态
        for btn in self.buttons:
            btn.set_active(False)
        
        # 激活选中的按钮
        self.buttons[index].set_active(True)
        
        # 更新当前标签
        self.current_tab = index
        
        # 加载对应内容
        self.load_tab_content(index)
        
        tab_names = ["测试主界面", "自定义功能", "仪器指令", "手动控制", "设备端口"]
        print(f"✅ 切换到: {tab_names[index]}")
    
    def load_tab_content(self, tab_index):
        """加载标签内容"""
        # 清除当前内容
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        tab_names = ["测试主界面", "自定义功能", "仪器指令", "手动控制", "设备端口"]
        
        if tab_index < len(tab_names):
            try:
                # 动态导入对应的标签模块
                module_names = [
                    "interface.tabs.test_main",
                    "interface.tabs.custom_function", 
                    "interface.tabs.instrument_command",
                    "interface.tabs.manual_control",
                    "interface.tabs.device_port"
                ]
                
                if tab_index < len(module_names):
                    module_name = module_names[tab_index]
                    module = __import__(module_name, fromlist=[''])
                    
                    # 获取标签类名
                    class_names = [
                        "TestMainTab",
                        "CustomFunctionTab",
                        "InstrumentCommandTab", 
                        "ManualControlTab",
                        "DevicePortTab"
                    ]
                    
                    if tab_index < len(class_names):
                        class_name = class_names[tab_index]
                        if hasattr(module, class_name):
                            tab_class = getattr(module, class_name)
                            # 创建标签实例
                            tab_instance = tab_class(self.content_frame)
                            print(f"✅ 加载内容: {tab_names[tab_index]}")
                        else:
                            self.create_placeholder_content(tab_names[tab_index])
                    else:
                        self.create_placeholder_content(tab_names[tab_index])
                else:
                    self.create_placeholder_content(tab_names[tab_index])
                        
            except ImportError as e:
                print(f"⚠️ 模块导入失败: {e}")
                self.create_placeholder_content(tab_names[tab_index])
            except Exception as e:
                print(f"❌ 加载内容时出错: {e}")
                self.create_placeholder_content(tab_names[tab_index])
        else:
            self.create_placeholder_content("未知页面")
    
    def create_placeholder_content(self, tab_name):
        """创建占位符内容"""
        placeholder_label = tk.Label(
            self.content_frame,
            text=f"{tab_name}\n\n功能开发中...",
            font=('Microsoft YaHei', 16),
            fg='white',
            bg='#4A90E2',
            justify=tk.CENTER
        )
        placeholder_label.pack(expand=True)


def main():
    """主函数"""
    root = tk.Tk()
    app = TkinterToolsInterface(root)
    
    print("🎨 tkintertools风格界面已启动")
    print("✨ 特点:")
    print("   • 蓝色渐变背景")
    print("   • 毛玻璃效果按钮")
    print("   • 现代化设计风格")
    print("   • CVTE品牌标识")
    
    root.mainloop()


if __name__ == "__main__":
    main()
