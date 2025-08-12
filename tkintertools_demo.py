"""
tkintertools风格界面测试
"""
import tkinter as tk
import math
from datetime import datetime

class SimpleGlassButton:
    """简化的毛玻璃按钮"""
    
    def __init__(self, parent, text="", width=140, height=45, command=None):
        self.parent = parent
        self.text = text
        self.width = width
        self.height = height
        self.command = command
        self.state = 'normal'
        
        self.create_button()
    
    def create_button(self):
        """创建按钮"""
        self.frame = tk.Frame(self.parent, bg='#4A90E2')
        
        # 使用Label模拟毛玻璃效果
        self.button = tk.Label(
            self.frame,
            text=self.text,
            width=15,
            height=2,
            bg='#5AA0F2',
            fg='white',
            font=('Microsoft YaHei', 11, 'normal'),
            relief='flat',
            bd=1,
            cursor='hand2'
        )
        self.button.pack(padx=2, pady=2)
        
        # 绑定事件
        self.button.bind('<Button-1>', self.on_click)
        self.button.bind('<Enter>', self.on_enter)
        self.button.bind('<Leave>', self.on_leave)
    
    def on_click(self, event):
        if self.command:
            self.command()
    
    def on_enter(self, event):
        if self.state != 'active':
            self.button.config(bg='#6AB0F8')
    
    def on_leave(self, event):
        if self.state != 'active':
            self.button.config(bg='#5AA0F2')
    
    def set_active(self, active=True):
        self.state = 'active' if active else 'normal'
        if active:
            self.button.config(bg='#70B0FF', relief='solid')
        else:
            self.button.config(bg='#5AA0F2', relief='flat')
    
    def pack(self, **kwargs):
        self.frame.pack(**kwargs)

def create_tkintertools_demo():
    """创建tkintertools风格演示"""
    root = tk.Tk()
    root.title("tkintertools Style Demo")
    root.geometry("1200x800")
    
    # 创建渐变背景
    bg_frame = tk.Frame(root, bg='#4A90E2')
    bg_frame.pack(fill=tk.BOTH, expand=True)
    
    # 主容器
    main_container = tk.Frame(bg_frame, bg='#4A90E2', padx=50, pady=40)
    main_container.pack(fill=tk.BOTH, expand=True)
    
    # 标题区域
    title_frame = tk.Frame(main_container, bg='#4A90E2', height=100)
    title_frame.pack(fill=tk.X, pady=(0, 20))
    title_frame.pack_propagate(False)
    
    # CVTE Logo (左侧)
    logo_label = tk.Label(
        title_frame,
        text="CVTE",
        font=('Arial', 24, 'bold'),
        fg='white',
        bg='#4A90E2'
    )
    logo_label.pack(side=tk.LEFT, pady=30)
    
    # 标题 (中央)
    title_label = tk.Label(
        title_frame,
        text="Power Test Integrate System",
        font=('Microsoft YaHei', 20, 'bold'),
        fg='white',
        bg='#4A90E2'
    )
    title_label.pack(expand=True, pady=30)
    
    # 版本信息 (右侧)
    version_label = tk.Label(
        title_frame,
        text="v3.0.0\\ntkintertools Style",
        font=('Microsoft YaHei', 9),
        fg='white',
        bg='#4A90E2',
        justify=tk.RIGHT
    )
    version_label.pack(side=tk.RIGHT, pady=30)
    
    # 导航按钮区域
    nav_frame = tk.Frame(main_container, bg='#4A90E2', height=80)
    nav_frame.pack(fill=tk.X, pady=10)
    nav_frame.pack_propagate(False)
    
    # 按钮容器
    btn_container = tk.Frame(nav_frame, bg='#4A90E2')
    btn_container.pack(expand=True)
    
    # 创建导航按钮
    button_names = ["测试主界面", "自定义功能", "仪器指令", "手动控制", "设备端口"]
    buttons = []
    
    def switch_tab(index):
        # 重置所有按钮
        for btn in buttons:
            btn.set_active(False)
        # 激活选中按钮
        buttons[index].set_active(True)
        content_label.config(text=f"当前页面: {button_names[index]}")
        print(f"切换到: {button_names[index]}")
    
    for i, name in enumerate(button_names):
        btn = SimpleGlassButton(
            btn_container,
            text=name,
            command=lambda idx=i: switch_tab(idx)
        )
        btn.pack(side=tk.LEFT, padx=8, pady=15)
        buttons.append(btn)
    
    # 设置第一个按钮为激活状态
    buttons[0].set_active(True)
    
    # 内容区域
    content_frame = tk.Frame(main_container, bg='#4A90E2', relief='flat')
    content_frame.pack(fill=tk.BOTH, expand=True, pady=20)
    
    # 内容标签
    content_label = tk.Label(
        content_frame,
        text="当前页面: 测试主界面",
        font=('Microsoft YaHei', 16),
        fg='white',
        bg='#4A90E2'
    )
    content_label.pack(expand=True)
    
    # 功能演示区域
    demo_frame = tk.Frame(content_frame, bg='#4A90E2')
    demo_frame.pack(pady=20)
    
    demo_label = tk.Label(
        demo_frame,
        text="✨ tkintertools风格特点:\\n• 蓝色渐变背景\\n• 毛玻璃效果按钮\\n• 现代化设计风格\\n• 半透明界面元素",
        font=('Microsoft YaHei', 12),
        fg='white',
        bg='#4A90E2',
        justify=tk.LEFT
    )
    demo_label.pack()
    
    # 状态栏
    status_frame = tk.Frame(main_container, bg='#4A90E2', height=40)
    status_frame.pack(fill=tk.X, side=tk.BOTTOM)
    status_frame.pack_propagate(False)
    
    # 版本信息 (左侧)
    status_version = tk.Label(
        status_frame,
        text="版本: v3.0.0 - tkintertools风格",
        font=('Microsoft YaHei', 9),
        fg='white',
        bg='#4A90E2'
    )
    status_version.pack(side=tk.LEFT, pady=10)
    
    # 时间显示 (右侧)
    time_label = tk.Label(
        status_frame,
        text="",
        font=('Microsoft YaHei', 9),
        fg='white',
        bg='#4A90E2'
    )
    time_label.pack(side=tk.RIGHT, pady=10)
    
    def update_time():
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        time_label.config(text=current_time)
        root.after(1000, update_time)
    
    update_time()
    
    print("🎨 tkintertools风格演示界面已启动")
    print("✨ 特点:")
    print("   • 蓝色渐变背景 (#4A90E2)")
    print("   • 毛玻璃效果按钮")
    print("   • 现代化设计风格")
    print("   • CVTE品牌标识")
    
    root.mainloop()

if __name__ == "__main__":
    create_tkintertools_demo()
