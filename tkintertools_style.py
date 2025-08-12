"""
现代化毛玻璃风格界面
模仿tkintertools的设计风格，具有蓝色渐变背景和现代化按钮
"""
import tkinter as tk
from tkinter import ttk
import math
from datetime import datetime

class GlassButton:
    """毛玻璃风格按钮"""
    
    def __init__(self, parent, text="", width=160, height=50,
                 bg_color='rgba(100, 150, 200, 0.3)', 
                 active_color='rgba(120, 170, 220, 0.5)',
                 text_color='white',
                 font=('Microsoft YaHei', 12, 'normal'),
                 command=None):
        
        self.parent = parent
        self.text = text
        self.width = width
        self.height = height
        self.bg_color = bg_color
        self.active_color = active_color
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
        # 创建Canvas
        self.canvas = tk.Canvas(
            self.parent,
            width=self.width + 4,
            height=self.height + 4,
            highlightthickness=0,
            bd=0,
            bg='#4A90E2'  # 与背景色匹配
        )
        
        self.draw_button()
        self.bind_events()
        
    def draw_button(self):
        """绘制按钮"""
        self.canvas.delete("all")
        
        # 根据状态选择颜色
        if self.state == 'active':
            # 活跃状态：更亮的蓝色
            fill_color = '#5AA0F2'
            outline_color = '#70B0FF'
        elif self.state == 'hover':
            # 悬停状态：半透明白色叠加
            fill_color = '#6AB0F8'
            outline_color = '#80C0FF'
        else:
            # 正常状态：半透明蓝色
            fill_color = '#4A90E2'
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


class ModernTkinterToolsInterface:
    """现代化tkintertools风格界面"""
    
    def __init__(self, root):
        self.root = root
        self.current_tab = 0
        self.setup_window()
        self.create_interface()
        self.update_time()
    
    def setup_window(self):
        """设置窗口"""
        self.root.title("Power Test Integrate System - tkintertools Style")
        self.root.geometry("1200x800")
        
        # 创建蓝色渐变背景
        self.create_gradient_background()
        
        # 窗口居中
        self.center_window()
    
    def create_gradient_background(self):
        """创建渐变背景"""
        # 使用Canvas创建渐变效果
        self.bg_canvas = tk.Canvas(self.root, highlightthickness=0)
        self.bg_canvas.pack(fill=tk.BOTH, expand=True)
        
        # 绘制渐变背景
        self.draw_gradient()
        
    def draw_gradient(self):
        """绘制蓝色渐变"""
        width = 1200
        height = 800
        
        # 从深蓝到浅蓝的渐变
        for i in range(height):
            # 计算渐变颜色
            ratio = i / height
            # 从 #2E5BBA 到 #4A90E2
            r = int(0x2E + (0x4A - 0x2E) * ratio)
            g = int(0x5B + (0x90 - 0x5B) * ratio)
            b = int(0xBA + (0xE2 - 0xBA) * ratio)
            
            color = f"#{r:02x}{g:02x}{b:02x}"
            self.bg_canvas.create_line(0, i, width, i, fill=color, width=1)
    
    def center_window(self):
        """窗口居中"""
        self.root.update_idletasks()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - 1200) // 2
        y = (screen_height - 800) // 2
        self.root.geometry(f"1200x800+{x}+{y}")
    
    def create_interface(self):
        """创建界面"""
        # 主容器框架
        main_frame = tk.Frame(self.bg_canvas, bg='#4A90E2')
        main_frame.place(relx=0.5, rely=0.5, anchor='center', width=1100, height=700)
        
        # 标题区域
        self.create_title_area(main_frame)
        
        # 左侧按钮区域
        self.create_sidebar(main_frame)
        
        # 右侧内容区域
        self.create_content_area(main_frame)
        
        # 底部状态栏
        self.create_status_bar(main_frame)
    
    def create_title_area(self, parent):
        """创建标题区域"""
        title_frame = tk.Frame(parent, bg='#4A90E2', height=80)
        title_frame.pack(fill=tk.X, padx=20, pady=(20, 10))
        title_frame.pack_propagate(False)
        
        # 主标题
        title_label = tk.Label(
            title_frame,
            text="Power Test Integrate System",
            font=('Microsoft YaHei', 24, 'bold'),
            fg='white',
            bg='#4A90E2'
        )
        title_label.pack(side=tk.LEFT, pady=20)
        
        # 版本信息
        version_label = tk.Label(
            title_frame,
            text="v3.0.0 (Modern Style)",
            font=('Microsoft YaHei', 10),
            fg='rgba(255,255,255,0.8)',
            bg='#4A90E2'
        )
        version_label.pack(side=tk.LEFT, padx=(20, 0), pady=25)
    
    def create_sidebar(self, parent):
        """创建左侧边栏"""
        sidebar_frame = tk.Frame(parent, bg='#4A90E2', width=280)
        sidebar_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(20, 0))
        sidebar_frame.pack_propagate(False)
        
        # 按钮列表
        buttons_data = [
            ("测试主界面", "🏠"),
            ("自定义功能", "⚙️"),
            ("仪器指令", "📡"),
            ("手动控制", "🎮"),
            ("设备端口", "🔌"),
            ("数据分析", "📊"),
            ("系统设置", "🛠️"),
            ("关于系统", "ℹ️")
        ]
        
        self.sidebar_buttons = []
        
        for i, (text, icon) in enumerate(buttons_data):
            btn = GlassButton(
                sidebar_frame,
                text=f"{icon} {text}",
                width=250,
                height=50,
                font=('Microsoft YaHei', 12, 'normal'),
                command=lambda idx=i: self.switch_tab(idx)
            )
            btn.pack(pady=8, padx=10)
            self.sidebar_buttons.append(btn)
        
        # 设置第一个按钮为激活状态
        self.sidebar_buttons[0].set_active(True)
    
    def create_content_area(self, parent):
        """创建内容区域"""
        content_frame = tk.Frame(parent, bg='rgba(255,255,255,0.1)', relief='flat')
        content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=20, pady=(0, 20))
        
        # 内容标题
        content_title = tk.Label(
            content_frame,
            text="测试主界面",
            font=('Microsoft YaHei', 18, 'bold'),
            fg='white',
            bg='rgba(255,255,255,0.1)'
        )
        content_title.pack(pady=20)
        
        # 功能区域
        self.create_function_area(content_frame)
    
    def create_function_area(self, parent):
        """创建功能区域"""
        # 三个主要功能区域
        function_areas = [
            ("基础测试", "进行基本的电源测试功能"),
            ("高级设置", "配置高级测试参数"),
            ("数据导出", "导出测试结果和报告")
        ]
        
        for i, (title, desc) in enumerate(function_areas):
            area_frame = tk.Frame(parent, bg='rgba(255,255,255,0.1)', height=120)
            area_frame.pack(fill=tk.X, padx=20, pady=10)
            area_frame.pack_propagate(False)
            
            # 区域标题
            area_title = tk.Label(
                area_frame,
                text=title,
                font=('Microsoft YaHei', 14, 'bold'),
                fg='white',
                bg='rgba(255,255,255,0.1)'
            )
            area_title.pack(anchor='w', padx=20, pady=(15, 5))
            
            # 区域描述
            area_desc = tk.Label(
                area_frame,
                text=desc,
                font=('Microsoft YaHei', 10),
                fg='rgba(255,255,255,0.8)',
                bg='rgba(255,255,255,0.1)'
            )
            area_desc.pack(anchor='w', padx=20)
            
            # 操作按钮
            btn_frame = tk.Frame(area_frame, bg='rgba(255,255,255,0.1)')
            btn_frame.pack(anchor='w', padx=20, pady=(10, 0))
            
            action_btn = GlassButton(
                btn_frame,
                text="开始",
                width=80,
                height=30,
                font=('Microsoft YaHei', 10),
                command=lambda t=title: self.execute_function(t)
            )
            action_btn.pack(side=tk.LEFT)
    
    def create_status_bar(self, parent):
        """创建状态栏"""
        status_frame = tk.Frame(parent, bg='#4A90E2', height=40)
        status_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=20)
        status_frame.pack_propagate(False)
        
        # 状态信息
        self.status_label = tk.Label(
            status_frame,
            text="就绪",
            font=('Microsoft YaHei', 9),
            fg='white',
            bg='#4A90E2'
        )
        self.status_label.pack(side=tk.LEFT, pady=10)
        
        # 时间显示
        self.time_label = tk.Label(
            status_frame,
            text="",
            font=('Microsoft YaHei', 9),
            fg='rgba(255,255,255,0.8)',
            bg='#4A90E2'
        )
        self.time_label.pack(side=tk.RIGHT, pady=10)
    
    def switch_tab(self, index):
        """切换标签"""
        # 重置所有按钮状态
        for btn in self.sidebar_buttons:
            btn.set_active(False)
        
        # 激活选中的按钮
        self.sidebar_buttons[index].set_active(True)
        
        # 更新状态
        tab_names = ["测试主界面", "自定义功能", "仪器指令", "手动控制", 
                    "设备端口", "数据分析", "系统设置", "关于系统"]
        self.status_label.config(text=f"当前页面: {tab_names[index]}")
        
        print(f"✅ 切换到: {tab_names[index]}")
    
    def execute_function(self, function_name):
        """执行功能"""
        self.status_label.config(text=f"正在执行: {function_name}")
        print(f"🚀 执行功能: {function_name}")
    
    def update_time(self):
        """更新时间"""
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.time_label.config(text=current_time)
        self.root.after(1000, self.update_time)


def create_tkintertools_style_interface():
    """创建tkintertools风格界面"""
    root = tk.Tk()
    app = ModernTkinterToolsInterface(root)
    
    print("🎨 tkintertools风格界面已启动")
    print("✨ 特点:")
    print("   • 蓝色渐变背景")
    print("   • 毛玻璃效果按钮")
    print("   • 现代化设计风格")
    print("   • 半透明界面元素")
    
    root.mainloop()


if __name__ == "__main__":
    create_tkintertools_style_interface()
