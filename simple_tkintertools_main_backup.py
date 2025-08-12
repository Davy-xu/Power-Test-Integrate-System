"""
简化的tkintertools风格主界面
现代化设计，包含渐变背景、卡片式布局和专业配色
"""
import tkinter as tk
from tkinter import ttk
from datetime import datetime
import math
import sys
import os

class SimpleTkinterToolsInterface:
    def __init__(self):
        self.root = None
        self.bg_canvas = None
        self.tab_buttons = []
        self.content_frame = None
        self.content_window = None
        self.current_tab = 0
        self.setup_styles()
    
    def setup_styles(self):
        """设置现代化ttk样式"""
        self.style = ttk.Style()
        
        # 设置现代化主题
        try:
            self.style.theme_use('clam')
        except:
            pass
        
        # 配置现代化颜色
        self.style.configure('Modern.TCombobox',
                           fieldbackground='#ffffff',
                           background='#f8f9fa',
                           bordercolor='#dee2e6',
                           arrowcolor='#6c757d',
                           focuscolor='#0d6efd')
        
        self.style.configure('Modern.TLabel',
                           background='#ffffff',
                           foreground='#212529')
        
        self.style.configure('Modern.TFrame',
                           background='#ffffff',
                           bordercolor='#dee2e6')
    def draw_background(self):
        """绘制优化的渐变背景（防止卡顿）"""
        # 如果开启窗口优化模式，跳过重绘逻辑，仅绘制简单背景
        import os
        if os.environ.get('WINDOW_OPTIMIZE') == '1':
            width = self.bg_canvas.winfo_width() or 1200
            height = self.bg_canvas.winfo_height() or 800
            self.bg_canvas.delete("bg")
            self.create_simple_background(width, height)
            return
        try:
            # 如果处于窗口优化模式，使用最简背景
            import os
            if os.environ.get('WINDOW_OPTIMIZE') == '1':
                width = self.bg_canvas.winfo_width() or 1200
                height = self.bg_canvas.winfo_height() or 800
                self.bg_canvas.delete("bg")
                self.create_simple_background(width, height)
                return
            self.root.update_idletasks()
            width = self.bg_canvas.winfo_width()
            height = self.bg_canvas.winfo_height()
            if width <= 1:
                width = 1200
            if height <= 1:
                height = 800
            
            # 删除旧的背景元素
            self.bg_canvas.delete("bg")
            
            # 检查是否需要简化绘制（窗口很大时）
            is_large_window = width > 1400 or height > 900
            
            if is_large_window:
                # 大窗口时使用超简化背景
                self.create_simple_background(width, height)
            else:
                # 普通窗口使用优化渐变
                self.create_optimized_gradient(width, height)
                self.add_simple_grid(width, height)
                
        except Exception as e:
            print(f"❌ 背景绘制错误: {e}")
            # 如果渐变绘制失败，使用简单背景
            self.create_simple_background(width, height)
            
    def create_simple_background(self, width, height):
        """创建简单背景（无渐变，最快速度）"""
        self.bg_canvas.create_rectangle(
            0, 0, width, height,
            fill="#99CCFF", outline="", tags="bg"
        )
    
    def create_optimized_gradient(self, width, height):
        """创建优化的渐变背景（减少步骤数）"""
        # 减少渐变步骤数，从100步减少到20步，提高性能
        steps = 20  # 大幅减少步骤数
        for i in range(steps):
            ratio = i / steps
            # 使用更现代的色彩搭配
            r1, g1, b1 = 0x66, 0x99, 0xCC  # 起始色 #6699CC
            r2, g2, b2 = 0xB8, 0xD4, 0xF0  # 结束色 #B8D4F0
            
            r = int(r1 + (r2 - r1) * ratio)
            g = int(g1 + (g2 - g1) * ratio)  
            b = int(b1 + (b2 - b1) * ratio)
            
            color = f"#{r:02x}{g:02x}{b:02x}"
            
            y1 = int(height * i / steps)
            y2 = int(height * (i + 1) / steps)
            
            self.bg_canvas.create_rectangle(
                0, y1, width, y2,
                fill=color, outline=color, tags="bg"
            )
    
    def add_simple_grid(self, width, height):
        """添加简化的网格图案（减少线条数量）"""
        grid_size = 80  # 增大网格大小，减少线条数量
        grid_color = "#A8C5E8"
        
        # 只绘制较少的网格线
        for x in range(0, width, grid_size):
            if x % (grid_size * 2) == 0:  # 每隔一条线绘制
                self.bg_canvas.create_line(
                    x, 0, x, height,
                    fill=grid_color, width=1, tags="bg"
                )
        
        for y in range(0, height, grid_size):
            if y % (grid_size * 2) == 0:  # 每隔一条线绘制
                self.bg_canvas.create_line(
                    0, y, width, y,
                    fill=grid_color, width=1, tags="bg"
                )
    def __init__(self):
        self.root = None
        self.bg_canvas = None
        self.tab_buttons = []
        self.content_frame = None
        self.content_window = None
        self.current_tab = 0

    def create_simplified_interface(self):
        """创建简化的界面，专注于功能而非复杂效果"""
        print("🚀 创建简化界面...")
        
        # 创建简单背景
        self.bg_canvas.create_rectangle(0, 0, 2000, 2000, fill="#e3f2fd", outline="", tags="bg")
        
        # 创建标题
        self.bg_canvas.create_text(600, 50, text="电源测试设备集成控制系统", 
                                  font=('Microsoft YaHei UI', 18, 'bold'), 
                                  fill='#1565c0', tags="title")
        
        # 创建左侧按钮
        self.create_simple_tabs()
        
        # 创建内容区域
        self.create_simple_content_area()
        
        # 创建状态栏
        self.create_simple_status_bar()
        
        print("✅ 简化界面创建完成")
    
    def create_simple_tabs(self):
        """创建更紧凑的左侧按钮"""
        tab_names = ["测试主界面", "自定义功能", "仪器指令", "手动控制", "设备端口", "系统运行日志", "数据同步", "系统信息", "帮助"]
        
        self.tab_buttons = []
        start_x, start_y = 15, 90  # 减少左边距
        button_width, button_height = 110, 35  # 减少按钮尺寸 (120,40 -> 110,35)
        
        for i, name in enumerate(tab_names):
            y_pos = start_y + i * 42  # 减少间距 (50 -> 42)
            
            # 创建更紧凑的按钮
            btn = tk.Button(self.bg_canvas, text=name, 
                           font=('Microsoft YaHei UI', 8),  # 减小字体 (9 -> 8)
                           bg='#42a5f5' if i == 0 else '#90caf9',
                           fg='white' if i == 0 else '#0d47a1',
                           relief='flat', width=14, height=1,  # 减少按钮高度 (2 -> 1)
                           command=lambda idx=i: self.simple_switch_tab(idx))
            
            # 放置按钮
            self.bg_canvas.create_window(start_x, y_pos, window=btn, anchor='nw',
                                       width=button_width, height=button_height)
            
            self.tab_buttons.append(btn)
        
        self.current_tab = 0
    
    def create_simple_content_area(self):
        """创建超大放大的内容区域 - 激进版本"""
        print("🔥 创建超大内容区域...")
        
        # 计算超大的内容区域位置 - 最大化利用空间
        content_x, content_y = 130, 80  # 进一步减少边距
        
        # 创建内容框架
        self.content_frame = tk.Frame(self.bg_canvas, bg='white', relief='raised', bd=2)
        
        # 计算超大尺寸
        initial_width = 1100   # 进一步增加宽度 (1000 -> 1100)
        initial_height = 650   # 进一步增加高度 (600 -> 650)
        
        print(f"🎯 超大内容区域参数:")
        print(f"   位置: ({content_x}, {content_y})")
        print(f"   尺寸: {initial_width} x {initial_height}")
        
        # 放置内容区域
        self.content_window = self.bg_canvas.create_window(
            content_x, content_y, window=self.content_frame, anchor='nw',
            width=initial_width, height=initial_height
        )
        
        # 添加默认内容
        self.show_simple_welcome_content()
        
        # 绑定窗口调整大小事件 - 超级积极地利用空间
        def resize_content(event=None):
            if event and event.widget == self.root:
                try:
                    win_w = self.bg_canvas.winfo_width()
                    win_h = self.bg_canvas.winfo_height()
                    # 超大的内容区域 - 最大化利用
                    new_w = max(700, win_w - 140)  # 进一步减少边距
                    new_h = max(450, win_h - 100)  # 进一步减少边距
                    self.bg_canvas.itemconfig(self.content_window, width=new_w, height=new_h)
                    print(f"� 超大内容区域调整: {new_w}x{new_h}")
                except Exception as e:
                    print(f"调整内容区域时出错: {e}")
        
        self.root.bind('<Configure>', resize_content)
        
        print(f"✅ 超大内容区域创建完成，ID: {self.content_window}")
    
    def create_simple_status_bar(self):
        """创建紧凑的状态栏"""
        # 动态计算状态栏位置，更靠近底部
        def get_status_y():
            try:
                canvas_height = self.bg_canvas.winfo_height()
                return max(700, canvas_height - 25)  # 距离底部25像素
            except:
                return 720  # 默认位置
        
        status_y = get_status_y()
        
        # 当前状态
        self.bg_canvas.create_text(20, status_y, text="当前: 测试主界面",  # 减少左边距 (30 -> 20)
                                  font=('Microsoft YaHei UI', 8),  # 减小字体 (9 -> 8)
                                  fill='#666666', anchor='w', tags="status")
        
        # 时间显示 - 动态位置
        def get_time_x():
            try:
                canvas_width = self.bg_canvas.winfo_width()
                return max(1100, canvas_width - 20)  # 距离右边20像素
            except:
                return 1150  # 默认位置
        
        time_x = get_time_x()
        self.time_text_id = self.bg_canvas.create_text(time_x, status_y, text="", 
                                                      font=('Microsoft YaHei UI', 8),  # 减小字体
                                                      fill='#666666', anchor='e', tags="time")
        
        # 开始时间更新
        self.update_simple_time()
    
    def show_simple_welcome_content(self):
        """显示简单的欢迎内容"""
        # 清除之前的内容
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        # 标题
        title = tk.Label(self.content_frame, text="测试主界面", 
                        font=('Microsoft YaHei UI', 14, 'bold'),
                        bg='white', fg='#1565c0')
        title.pack(pady=20)
        
        # 状态信息
        status_frame = tk.Frame(self.content_frame, bg='#f5f5f5', relief='groove', bd=1)
        status_frame.pack(fill='x', padx=20, pady=10)
        
        status_label = tk.Label(status_frame, 
                               text="系统状态\n✓ 设备连接状态: 已连接\n✓ 数据采集状态: 就绪\n⦿ 测试进度: 0%\n⏰ 运行时间: 00:00:00",
                               font=('Microsoft YaHei UI', 10),
                               bg='#f5f5f5', fg='#424242', justify='left')
        status_label.pack(pady=10, padx=10)
        
        # 窗口信息
        self.window_info_label = tk.Label(self.content_frame, text="", 
                                         font=('Microsoft YaHei UI', 9),
                                         bg='white', fg='#666666')
        self.window_info_label.pack(pady=10)
        
        # 开始更新窗口信息
        self.update_window_info()
    
    def simple_switch_tab(self, tab_index):
        """简单的选项卡切换"""
        # 更新按钮样式
        for i, btn in enumerate(self.tab_buttons):
            if i == tab_index:
                btn.config(bg='#42a5f5', fg='white')
            else:
                btn.config(bg='#90caf9', fg='#0d47a1')
        
        self.current_tab = tab_index
        
        # 更新状态
        tab_names = ["测试主界面", "自定义功能", "仪器指令", "手动控制", "设备端口", "系统运行日志", "数据同步", "系统信息", "帮助"]
        self.bg_canvas.itemconfig("status", text=f"当前: {tab_names[tab_index]}")
    
    def update_simple_time(self):
        """更新简单时间显示"""
        try:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.bg_canvas.itemconfig(self.time_text_id, text=current_time)
            self.root.after(1000, self.update_simple_time)
        except Exception as e:
            print(f"时间更新错误: {e}")
    
    def update_window_info(self):
        """更新窗口信息显示"""
        try:
            width = self.root.winfo_width()
            height = self.root.winfo_height()
            state = self.root.state()
            resizable = self.root.resizable()
            
            info_text = f"窗口信息: {width}×{height} | 状态: {state} | 可调整: {resizable}"
            self.window_info_label.config(text=info_text)
            
            self.root.after(1000, self.update_window_info)
        except Exception as e:
            print(f"窗口信息更新错误: {e}")

    def create_interface(self):
        """创建选项卡界面（优化版本，防止卡顿）"""
        print("🚀 开始创建界面...")
        
        # 显示加载提示
        self.show_loading_message()
        
        # 分步骤创建界面，避免一次性创建导致卡顿
        self.root.after(100, self.step1_create_header)
        # 绑定根窗口变化时整体刷新（已使用 _perform_resize 管理）
        # self.root.bind('<Configure>', self.on_window_resize)

    def show_loading_message(self):
        """显示加载提示"""
        self.bg_canvas.create_text(
            600, 300, text="正在加载界面，请稍候...", 
            font=('Microsoft YaHei', 16), 
            fill='#2c3e50', tags="loading"
        )
        self.root.update()
    
    def step1_create_header(self):
        """步骤1：创建头部"""
        print("📋 创建头部区域...")
        try:
            self.create_header()
            self.root.after(50, self.step2_create_tabs)
        except Exception as e:
            print(f"❌ 创建头部失败: {e}")
            self.root.after(50, self.step2_create_tabs)
    
    def step2_create_tabs(self):
        """步骤2：创建选项卡"""
        print("🔘 创建选项卡按钮...")
        try:
            self.create_tabs()
            self.root.after(50, self.step3_create_content)
        except Exception as e:
            print(f"❌ 创建选项卡失败: {e}")
            self.root.after(50, self.step3_create_content)
    
    def step3_create_content(self):
        """步骤3：创建内容区域"""
        print("📱 创建内容区域...")
        try:
            self.create_content_area()
            self.root.after(50, self.step4_create_status)
        except Exception as e:
            print(f"❌ 创建内容区域失败: {e}")
            self.root.after(50, self.step4_create_status)
    
    def step4_create_status(self):
        """步骤4：创建状态栏"""
        print("📊 创建状态栏...")
        try:
            self.create_status_bar()
            self.root.after(50, self.step5_finalize)
        except Exception as e:
            print(f"❌ 创建状态栏失败: {e}")
            self.root.after(50, self.step5_finalize)
    
    def step5_finalize(self):
        """步骤5：完成初始化"""
        print("✅ 界面创建完成！")
        
        # 移除加载提示
        self.bg_canvas.delete("loading")
        
        # 启动时间更新
        self.update_time()
        
        # 默认选择第一个选项卡
        if self.tab_buttons:
            self.switch_tab(0)
    
    def create_tab_interface(self):
        """创建选项卡界面（在渐变背景上）- 已废弃，使用分步骤创建"""
        pass  # 保留以防兼容性问题

    def create_header(self):
        """创建现代化顶部标题区域"""
        # 删除之前的标题元素（如果存在）
        self.bg_canvas.delete("header_text")

        # 创建现代化的头部容器
        header_height = 80
        self.bg_canvas.create_rectangle(
            0, 0, self.bg_canvas.winfo_width(), header_height,
            fill="#34495e", outline="", tags="header_text"
        )
        
        # 左上角显示 logo 图片
        try:
            # 构造 logo 图片路径
            logo_path = os.path.join(os.path.dirname(__file__), "picture", "CVTE logo.png")
            # 只加载一次 logo，避免重复创建 PhotoImage
            if not hasattr(self, '_logo_image'):
                from PIL import Image, ImageTk
                logo_img = Image.open(logo_path)
                # 最大显示宽高（像素），不改变图片比例
                max_w, max_h = 100, 50
                w, h = logo_img.size
                # 计算缩放比例，保证图片不会超过最大宽高且不拉伸
                scale = min(max_w / w, max_h / h, 1.0)
                if scale < 1.0:
                    new_w = int(w * scale)
                    new_h = int(h * scale)
                    # 按比例缩放图片
                    logo_img = logo_img.resize((new_w, new_h), Image.Resampling.LANCZOS)
                # 转为 Tkinter 可用的图片对象
                self._logo_image = ImageTk.PhotoImage(logo_img)
            # 在画布左上角显示 logo
            self.bg_canvas.create_image(
                25, 25,
                image=self._logo_image,
                anchor='nw',
                tags="header_text"
            )
        except Exception as e:
            print(f"❌ 加载 logo 图片失败: {e}")
            # 如果logo加载失败，显示文字标题
            self.bg_canvas.create_text(
                25, 40,
                text="Power Test System",
                anchor='w',
                font=('Microsoft YaHei', 16, 'bold'),
                fill='white',
                tags="header_text"
            )
        
        # 系统标题
        self.bg_canvas.create_text(
            150, 30,
            text="电源测试设备集成控制系统",
            anchor='w',
            font=('Microsoft YaHei', 18, 'bold'),
            fill='white',
            tags="header_text"
        )
        
        # # 副标题
        # self.bg_canvas.create_text(
        #     150, 55,
        #     text="Power Test Integrate System v2.0",
        #     anchor='w',
        #     font=('Microsoft YaHei', 10),
        #     fill='#bdc3c7',
        #     tags="header_text"
        # )

    def create_tabs(self):
        """创建整洁的左侧垂直按钮列表"""
        tab_names = ["测试主界面", "自定义功能", "仪器指令", "手动控制", "设备端口", "系统运行日志",  "数据同步", "系统信息", "帮助"]
        
        # 统一的按钮区域参数
        button_width = 150
        button_height = 50
        start_x = 15
        start_y = 120  # 头部下方
        button_spacing = 8  # 紧凑间距
        
        self.tab_buttons = []
        
        print(f"🔘 创建 {len(tab_names)} 个整洁按钮...")
        
        for i, tab_name in enumerate(tab_names):
            y_position = start_y + i * (button_height + button_spacing)
            print(f"   创建按钮 {i+1}: {tab_name}")
            
            # 创建整洁的按钮
            tab_btn = tk.Button(
                self.bg_canvas,
                text=tab_name,
                width=18,
                height=2,
                bg='#495057',
                fg='#ffffff',
                font=('Microsoft YaHei UI', 10, 'normal'),
                relief='flat',
                bd=0,
                cursor='hand2',
                activebackground='#007bff',
                activeforeground='white',
                command=lambda idx=i: self.switch_tab(idx)
            )
            
            # 将按钮放置在Canvas上
            btn_window = self.bg_canvas.create_window(
                start_x, y_position, 
                window=tab_btn, 
                anchor='nw',
                width=button_width,
                height=button_height
            )
            
            # 绑定悬停事件
            tab_btn.bind('<Enter>', lambda e, btn=tab_btn, idx=i: self.on_tab_enter(btn, idx))
            tab_btn.bind('<Leave>', lambda e, btn=tab_btn, idx=i: self.on_tab_leave(btn, idx))
            
            self.tab_buttons.append(tab_btn)
            print(f"      ✅ 按钮 {i+1} 创建完成")
        
        # 默认选中第一个选项卡
        if self.tab_buttons:
            self.switch_tab(0)
        
        print(f"✅ 所有 {len(self.tab_buttons)} 个按钮创建完成")
    
    def on_tab_enter(self, button, idx):
        """按钮悬停进入效果"""
        if idx != self.current_tab:
            button.config(bg='#007bff', fg='white')
    
    def on_tab_leave(self, button, idx):
        """按钮悬停离开效果"""
        if idx != self.current_tab:
            button.config(bg='#495057', fg='#ffffff')
        else:
            button.config(bg='#007bff', fg='white')

    def create_content_area(self):
        """创建放大的清爽整洁的内容区域"""
        # 获取当前窗口尺寸
        self.root.update_idletasks()
        window_width = self.root.winfo_width()
        window_height = self.root.winfo_height()
        
        # 如果窗口尺寸无效，使用默认值
        if window_width <= 1:
            window_width = 1200
        if window_height <= 1:
            window_height = 800
        
        # 放大的布局参数 - 与create_simple_content_area保持一致
        content_x = 140   # 减少左边距 (180 -> 140)
        content_y = 90    # 减少上边距 (120 -> 90) 
        content_width = max(600, window_width - 160)   # 增加宽度利用 (content_x + 20 -> 160)
        content_height = max(400, window_height - 120) # 增加高度利用 (content_y + 80 -> 120)
        
        print(f"📱 创建放大内容区域: {content_width}x{content_height} 位置({content_x}, {content_y})")
        
        # 删除旧的内容区域
        self.bg_canvas.delete("content_bg")
        if hasattr(self, 'content_window'):
            self.bg_canvas.delete(self.content_window)
        
        # 创建清爽的背景
        self.create_clean_background(content_x, content_y, content_width, content_height)
        
        # 创建内容框架
        if hasattr(self, 'content_frame') and self.content_frame:
            self.content_frame.destroy()
            
        self.content_frame = tk.Frame(
            self.bg_canvas, 
            bg='#ffffff',  # 纯白背景
            relief='flat', 
            bd=0
        )
        
        # 用 create_window 放置内容区
        self.content_window = self.bg_canvas.create_window(
            content_x + 5, content_y + 5, 
            window=self.content_frame, 
            anchor='nw',
            width=content_width - 10,
            height=content_height - 10
        )
        
        print(f"✅ 内容区域创建完成，Window ID: {self.content_window}")
        
        # 默认显示欢迎内容
        self.show_welcome_content()
        
        # 绑定窗口变化时动态调整内容区大小 - 使用放大参数
        def _resize_content(event=None):
            if hasattr(self, 'content_window') and event and event.widget == self.root:
                win_w = self.bg_canvas.winfo_width()
                win_h = self.bg_canvas.winfo_height()
                # 使用与create_simple_content_area相同的放大参数
                new_w = max(600, win_w - 160)  # 更大的内容区域
                new_h = max(400, win_h - 120)  # 更大的内容区域
                self.bg_canvas.itemconfig(self.content_window, width=new_w, height=new_h)
                print(f"📐 放大内容区域自动调整: {new_w}x{new_h}")
                
                # 同时重绘背景
                self.draw_background()
        
        self.root.bind('<Configure>', _resize_content)
    
    def create_clean_background(self, x, y, width, height):
        """创建清爽简洁的背景效果"""
        try:
            # 简单的阴影效果
            shadow_offset = 2
            self.bg_canvas.create_rectangle(
                x + shadow_offset, y + shadow_offset,
                x + width + shadow_offset, y + height + shadow_offset,
                fill="#e9ecef", outline="", tags="content_bg"
            )
            
            # 主体背景（纯白色）
            self.bg_canvas.create_rectangle(
                x, y, x + width, y + height,
                fill="#ffffff", outline="#dee2e6", width=1, tags="content_bg"
            )
            
            print(f"✅ 清爽背景创建完成: {width}x{height}")
            
        except Exception as e:
            print(f"❌ 创建背景时出错: {e}")
            # 降级方案：创建简单矩形
            self.bg_canvas.create_rectangle(
                x, y, x + width, y + height,
                fill="#ffffff", outline="#cccccc", width=1, tags="content_bg"
            )
            
            # 移除复杂的stipple效果，使用简单边框
            self.bg_canvas.create_rectangle(
                x, y, x + width, y + height,
                fill="", outline="#ecf0f1", width=1, tags="content_bg"
            )
        except Exception as e:
            print(f"❌ 透明背景创建失败: {e}")
            # 如果透明效果失败，使用简单背景
            self.bg_canvas.create_rectangle(
                x, y, x + width, y + height,
                fill="#ffffff", outline="#bdc3c7", width=1, tags="content_bg"
            )
    
    def create_status_bar(self):
        """创建现代化状态栏（增加底部空间和时间显示）"""
        self.root.update_idletasks()
        window_width = self.root.winfo_width()
        window_height = self.root.winfo_height()
        
        if window_width <= 1:
            window_width = 1200
        if window_height <= 1:
            window_height = 800
        
        # 删除旧的状态栏元素
        self.bg_canvas.delete("status_bar")
        
        # 状态栏位置和尺寸 - 增加高度并留更多底部空间
        status_height = 50  # 从35增加到50
        status_y = window_height - status_height - 15  # 底部留15像素空间
        
        # 状态栏背景
        self.bg_canvas.create_rectangle(
            0, status_y, window_width, status_y + status_height,
            fill="#2c3e50", outline="", tags="status_bar"
        )
        
        # 添加分割线
        self.bg_canvas.create_line(
            0, status_y, window_width, status_y,
            fill="#34495e", width=1, tags="status_bar"
        )
        
        # 系统状态文本
        self.status_text = self.bg_canvas.create_text(
            20, status_y + status_height//2,
            text="系统就绪 | Ready",
            anchor='w',
            font=('Microsoft YaHei', 11),
            fill='#ecf0f1',
            tags="status_bar"
        )
        
        # 连接状态指示器
        connection_x = 300
        self.connection_text = self.bg_canvas.create_text(
            connection_x, status_y + status_height//2,
            text="● 设备未连接",
            anchor='w', 
            font=('Microsoft YaHei', 10),
            fill='#e74c3c',
            tags="status_bar"
        )
        
        # 当前时间显示区域（右侧显示）
        time_x = window_width - 20
        self.time_text = self.bg_canvas.create_text(
            time_x, status_y + status_height//2,
            text="",
            anchor='e',
            font=('Consolas', 12, 'bold'),
            fill='#3498db',
            tags="status_bar"
        )
        
        # 版本信息移到时间左侧
        version_x = window_width - 180
        self.version_text = self.bg_canvas.create_text(
            version_x, status_y + status_height//2,
            text="v2.0",
            anchor='e',
            font=('Microsoft YaHei', 9),
            fill='#95a5a6',
            tags="status_bar"
        )
        
        print(f"✅ 现代化状态栏创建完成，位置: y={status_y}, 高度: {status_height}, 底部留空: 15px")
        
        # 立即更新时间显示，确保界面一致性
        self.update_time()
    
    def show_welcome_content(self):
        """显示现代化欢迎界面（透明效果）"""
        # 清空内容框架
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        # 欢迎标题 - 透明背景
        welcome_frame = tk.Frame(self.content_frame, bg='')
        welcome_frame.pack(fill=tk.BOTH, expand=True, padx=40, pady=40)
        
        # 主标题
        title_label = tk.Label(welcome_frame, 
                              text="欢迎使用电源测试集成系统",
                              font=('Microsoft YaHei', 24, 'bold'),
                              bg='', fg='#1a365d')
        title_label.pack(pady=(0, 20))
        
        # 副标题
        subtitle_label = tk.Label(welcome_frame,
                                 text="Power Test Integrate System v2.0",
                                 font=('Microsoft YaHei', 14),
                                 bg='', fg='#4a5568')
        subtitle_label.pack(pady=(0, 40))
        
        # 功能介绍卡片容器 - 透明背景
        cards_frame = tk.Frame(welcome_frame, bg='')
        cards_frame.pack(fill=tk.X, pady=20)
        
        # 创建功能卡片
        features = [
            ("🔧", "设备管理", "管理和配置测试设备"),
            ("📊", "数据分析", "实时监控和数据分析"),
            ("⚡", "自动测试", "自动化测试流程"),
            ("📈", "报告生成", "专业测试报告")
        ]
        
        for i, (icon, title, desc) in enumerate(features):
            card = self.create_feature_card(cards_frame, icon, title, desc)
            card.grid(row=i//2, column=i%2, padx=20, pady=15, sticky='ew')
        
        cards_frame.grid_columnconfigure(0, weight=1)
        cards_frame.grid_columnconfigure(1, weight=1)
        
        # 底部提示
        tip_label = tk.Label(welcome_frame,
                            text="请选择左侧菜单开始使用系统功能",
                            font=('Microsoft YaHei', 12),
                            bg='', fg='#6c757d')
        tip_label.pack(pady=(40, 0))
    
    def create_feature_card(self, parent, icon, title, description):
        """创建功能介绍卡片（毛玻璃效果）"""
        # 外层容器 - 透明
        card_container = tk.Frame(parent, bg='')
        
        # 内层卡片 - 半透明白色背景
        card_frame = tk.Frame(card_container, bg='#ffffff', relief='solid', bd=1)
        card_frame.pack(fill=tk.BOTH, expand=True, padx=3, pady=3)
        
        # 让卡片半透明
        card_frame.configure(bg='#f8f9fa')  # 浅色半透明
        
        # 图标
        icon_label = tk.Label(card_frame, text=icon, 
                             font=('Segoe UI Emoji', 18),
                             bg='#f8f9fa', fg='#3498db')
        icon_label.pack(pady=(12, 4))
        
        # 标题
        title_label = tk.Label(card_frame, text=title,
                              font=('Microsoft YaHei', 11, 'bold'),
                              bg='#f8f9fa', fg='#2c3e50')
        title_label.pack(pady=(0, 4))
        
        # 描述
        desc_label = tk.Label(card_frame, text=description,
                             font=('Microsoft YaHei', 8),
                             bg='#f8f9fa', fg='#6c757d')
        desc_label.pack(pady=(0, 12))
        
        return card_container
        
        print("✅ 最大化内容区域创建完成")

    def create_status_bar(self):
        """创建紧凑的响应式状态栏（仅显示时间）"""
        # 获取当前窗口尺寸
        self.root.update_idletasks()
        window_width = self.root.winfo_width()
        window_height = self.root.winfo_height()
        
        # 如果窗口尺寸无效，使用默认值
        if window_width <= 1:
            window_width = 1200
        if window_height <= 1:
            window_height = 800
        
        # 紧凑的状态栏位置 - 只留够显示时间的空间
        status_y = window_height - 25  # 距离底部25像素（原来50）
        time_x = window_width - 30     # 距离右边30像素（原来50）
        
        print(f"📊 创建紧凑状态栏: 位置 y={status_y}, 时间位置 x={time_x}")
        print("✅ 渐变背景绘制完成")
        
        # 窗口调整大小的处理在create_content_area中统一处理
        self.status_text = self.bg_canvas.create_text(
            30, status_y,  # 位置更靠左
            text=f"当前: {'测试主界面' if not hasattr(self, 'current_tab') else self.get_tab_name(self.current_tab)}",
            font=('Microsoft YaHei UI', 8),  # 字体减小
            fill='#B0C4DE',  # 更淡的颜色
            anchor='w',
            tags="status_bar"
        )
        win_w = self.bg_canvas.winfo_width()
        win_h = self.bg_canvas.winfo_height()
    
    def switch_tab(self, tab_index):
        """切换选项卡，使用整洁样式"""
        tab_names = ["测试主界面", "自定义功能", "仪器指令", "手动控制", "设备端口", "系统运行日志", "数据同步", "系统信息", "帮助"]
        print(f"🔄 切换到选项卡 {tab_index}: {tab_names[tab_index]}")

        # 更新按钮样式
        for i, btn in enumerate(self.tab_buttons):
            if i == tab_index:
                btn.config(bg='#007bff', fg='white', font=('Microsoft YaHei UI', 10, 'bold'))
            else:
                btn.config(bg='#495057', fg='#ffffff', font=('Microsoft YaHei UI', 10, 'normal'))

        # 更新当前选项卡索引
        self.current_tab = tab_index

        # 加载对应的选项卡内容
        self.load_tab_content(tab_index)

    def load_tab_content(self, tab_index):
        """加载选项卡内容（确保底部空间一致）"""
        # 清除之前的内容
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        if tab_index == 0:
            self.create_test_main_content()
        elif tab_index == 1:
            self.create_custom_function_content()
        elif tab_index == 2:
            self.create_instrument_command_content()
        elif tab_index == 3:
            self.create_manual_control_content()
        elif tab_index == 4:
            self.create_device_port_content()
        else:
            # 其余标签显示占位内容
            placeholder = tk.Label(self.content_frame, text="功能开发中...", font=("Microsoft YaHei UI", 14), fg="#888", bg="#99CCFF")
            placeholder.pack(expand=True)
            
        # 延迟强制保持布局一致性
        self.root.after(100, self.force_layout_consistency)
        
    def force_layout_consistency(self):
        """强制保持布局一致性 - 修复底部空间变化问题"""
        try:
            print("🔧 强制保持布局一致性...")
            
            # 确保内容区域尺寸一致
            if hasattr(self, 'content_window') and self.content_window:
                self.root.update_idletasks()
                
                # 获取当前窗口尺寸
                win_w = self.bg_canvas.winfo_width() if self.bg_canvas else 1200
                win_h = self.bg_canvas.winfo_height() if self.bg_canvas else 800
                
                # 固定的布局参数 - 关键在于保持一致
                SIDEBAR_WIDTH = 220
                CONTENT_PADDING = 20 
                BOTTOM_SPACE = 180  # 固定180像素底部空间
                
                # 计算内容区域尺寸
                content_width = max(200, win_w - SIDEBAR_WIDTH - CONTENT_PADDING)
                content_height = max(100, win_h - BOTTOM_SPACE - CONTENT_PADDING)
                
                # 强制应用固定尺寸
                self.bg_canvas.itemconfig(
                    self.content_window,
                    width=content_width,
                    height=content_height
                )
                
                print(f"🔧 强制布局: {content_width}x{content_height}, 底部固定: {BOTTOM_SPACE}px")
                
            # 确保状态栏位置正确
            if hasattr(self, 'time_text') or hasattr(self, 'status_text'):
                self.create_status_bar()
                
        except Exception as e:
            print(f"❌ 强制布局一致性失败: {e}")

    def create_test_main_content(self):
        """创建测试主界面内容"""
        # 标题
        title_label = tk.Label(
            self.content_frame,
            text="测试主界面",
            font=('Microsoft YaHei UI', 14, 'bold'),
            fg='#1e3a8a',
            bg='#99CCFF'
        )
        title_label.pack(pady=10)

        # 功能按钮区域 - 移除白色背景
        button_frame = tk.Frame(self.content_frame, bg='#99CCFF')
        button_frame.pack(fill='x', padx=20, pady=10)
        buttons = [
            ("停止测试", "#dc3545"),
            ("暂停测试", "#ffc107"),
            ("数据采集", "#17a2b8"),
            ("实时监控", "#6f42c1"),
            ("报告生成", "#fd7e14")
        ]
        for i, (text, color) in enumerate(buttons):
            btn = tk.Button(
                button_frame,
                text=text,
                bg=color,
                fg='white',
                font=('Microsoft YaHei UI', 10, 'bold'),
                width=12,
                height=2,
                relief='raised',
                bd=2,
                cursor='hand2',
                command=lambda t=text: print(f"点击: {t}")
            )
            btn.grid(row=i//3, column=i%3, padx=10, pady=5, sticky='w')
        # 状态信息区域
        info_frame = tk.Frame(self.content_frame, bg='#99CCFF')
        info_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        status_label = tk.Label(
            info_frame,
            text="📈 系统状态",
            font=('Microsoft YaHei', 12, 'bold'),
            fg='#1e3a8a',
            bg='#F8FBFF'
        )
        status_label.pack(anchor='w')
        
        status_info = [
            "🔌 设备连接状态: 已连接",
            "📊 数据采集状态: 就绪",
            "🎯 测试进度: 0%",
            "⏱️ 运行时间: 00:00:00",
            "💾 数据存储: 正常",
            "🌐 网络状态: 在线"
        ]
        
        for info in status_info:
            info_label = tk.Label(
                info_frame,
                text=info,
                font=('Microsoft YaHei', 10),
                fg='#2563eb',
                bg='#F8FBFF'
            )
            info_label.pack(anchor='w', pady=2)
    
    def create_custom_function_content(self):
        """创建自定义功能内容"""
        title_label = tk.Label(
            self.content_frame,
            text="🛠️ 自定义功能",
            font=('Microsoft YaHei', 14, 'bold'),
            fg='#1e3a8a',
            bg='#F8FBFF'
        )
        title_label.pack(pady=10, anchor='w', padx=20)
        
        functions = [
            "• 自定义测试序列编辑器",
            "• 参数配置管理",
            "• 用户脚本执行",
            "• 数据处理插件",
            "• 测试模板管理",
            "• 自动化流程设计"
        ]
        
        for func in functions:
            func_label = tk.Label(
                self.content_frame,
                text=func,
                font=('Microsoft YaHei UI', 11),
                fg='#374151',
                bg='#F8FBFF'
            )
            func_label.pack(anchor='w', padx=40, pady=5)
    
    def create_instrument_command_content(self):
        """集成仪器指令选项卡内容"""
        # 清空内容区
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        # 动态导入并挂载仪器指令界面
        import sys, os
        tab_dir = os.path.join(os.path.dirname(__file__), "interface", "tabs")
        if tab_dir not in sys.path:
            sys.path.append(tab_dir)
        import traceback
        # 自动创建 __init__.py 保证包可导入
        init_file = os.path.join(tab_dir, "__init__.py")
        if not os.path.exists(init_file):
            with open(init_file, "w", encoding="utf-8") as f:
                f.write("")
        try:
            # from instrument_command import InstrumentCommandTab  # 已禁用，防止启动报错
            self.content_frame.configure(bg='#F8FBFF')
            # InstrumentCommandTab(self.content_frame)  # 已禁用，防止启动报错
        except Exception as e:
            err_label = tk.Label(self.content_frame, text=f"仪器指令界面加载失败:\n{e}", fg='red')
            err_label.pack(padx=20, pady=20)
            traceback.print_exc()
    
    def create_manual_control_content(self):
        """创建手动控制内容"""
        title_label = tk.Label(
            self.content_frame,
            text="🎮 手动控制",
            font=('Microsoft YaHei UI', 14, 'bold'),
            fg='#1e3a8a',
            bg='#F8FBFF'
        )
        title_label.pack(pady=10, anchor='w', padx=20)
        
        # 控制按钮
        control_frame = tk.Frame(self.content_frame, bg='')
        control_frame.pack(fill='x', padx=20, pady=10)
        
        controls = [
            ("电源开", "#28a745"),
            ("电源关", "#dc3545"),
            ("复位", "#ffc107"),
            ("校准", "#17a2b8"),
            ("自检", "#6f42c1"),
            ("清零", "#fd7e14")
        ]
        
        for i, (text, color) in enumerate(controls):
            btn = tk.Button(
                control_frame,
                text=text,
                bg=color,
                fg='white',
                font=('Microsoft YaHei UI', 10, 'bold'),
                width=10,
                height=2,
                cursor='hand2',
                command=lambda t=text: print(f"手动控制: {t}")
            )
            btn.grid(row=i//3, column=i%3, padx=10, pady=5)
        
        # 参数调节区域
        param_label = tk.Label(
            self.content_frame,
            text="参数调节:",
            font=('Microsoft YaHei', 10, 'bold'),
            fg='#1f2937',
            bg='#F8FBFF'
        )
        param_label.pack(anchor='w', padx=20, pady=(20, 5))
        
        params = ["电压: 5.0V", "电流: 1.0A", "频率: 1000Hz", "功率: 5.0W"]
        for param in params:
            param_frame = tk.Frame(self.content_frame, bg='')
            param_frame.pack(fill='x', padx=40, pady=2)
            
            param_label = tk.Label(
                param_frame,
                text=param,
                font=('Microsoft YaHei', 10),
                fg='#374151',
                bg='#F8FBFF',
                width=15
            )
            param_label.pack(side='left')
            
            scale = tk.Scale(
                param_frame,
                from_=0,
                to=100,
                orient='horizontal',
                length=200,
                bg='#F8FBFF'
            )
            scale.pack(side='left', padx=10)
    
    def create_device_port_content(self):
        """创建设备端口内容"""
        title_label = tk.Label(
            self.content_frame,
            text="🔌 设备端口",
            font=('Microsoft YaHei UI', 14, 'bold'),
            fg='#1e3a8a',
            bg='#F8FBFF'
        )
        title_label.pack(pady=10, anchor='w', padx=20)
        
        # 端口列表
        ports = [
            ("COM1 - USB串口", "已连接", "#28a745"),
            ("COM3 - 蓝牙串口", "未连接", "#dc3545"),
            ("TCP/IP - 192.168.1.100:5025", "已连接", "#28a745"),
            ("USB - 设备ID: 0x1234", "已连接", "#28a745")
        ]
        
        for port, status, color in ports:
            port_frame = tk.Frame(self.content_frame, bg='')
            port_frame.pack(fill='x', padx=20, pady=5)
            
            port_label = tk.Label(
                port_frame,
                text=f"• {port}",
                font=('Microsoft YaHei UI', 10),
                fg='#374151',
                bg='#F8FBFF',
                width=40
            )
            port_label.pack(side='left')
            
            status_label = tk.Label(
                port_frame,
                text=status,
                font=('Microsoft YaHei UI', 10, 'bold'),
                fg=color,
                bg='#F8FBFF'
            )
            status_label.pack(side='left', padx=10)
        
        # 连接控制按钮
        btn_frame = tk.Frame(self.content_frame, bg='#ffffff')
        btn_frame.pack(fill='x', padx=20, pady=20)
        
        buttons = [
            ("刷新端口", "#6c757d"),
            ("连接设备", "#007bff"),
            ("断开连接", "#dc3545"),
            ("端口配置", "#17a2b8")
        ]
        
        for text, color in buttons:
            btn = tk.Button(
                btn_frame,
                text=text,
                bg=color,
                fg='white',
                font=('Microsoft YaHei UI', 10),
                width=12,
                cursor='hand2',
                command=lambda t=text: print(f"端口操作: {t}")
            )
            btn.pack(side='left', padx=10)
    
    def create_navigation_bar(self, parent):
        """已废弃 - 使用新的选项卡界面"""
        pass
    
    def create_text_logo(self, logo_frame):
        """已废弃 - 使用新的选项卡界面"""
        pass
    
    def create_content_display(self, parent):
        """已废弃 - 使用新的选项卡界面"""
        pass
    
    def create_status_area(self, parent):
        """已废弃 - 使用新的选项卡界面"""
        pass
    
    
    def create_placeholder_content(self, tab_name):
        """已废弃 - 使用新的内容创建方法"""
        pass
    
    def update_time(self):
        """更新时间显示"""
        try:
            if hasattr(self, 'time_label') and self.time_label and self.time_label.winfo_exists():
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.time_label.config(text=current_time)
        except tk.TclError:
            # 时间标签可能已被删除，尝试重新创建状态栏
            print("⚠️ 时间标签丢失，重新创建状态栏")
            try:
                self.create_status_bar()
            except:
                pass
        except Exception as e:
            print(f"❌ 背景绘制错误: {e}")
            self.bg_canvas.config(bg='#CCCCCC')


def main():
    """简化的主函数，强制使用放大版界面"""
    print("🚀 启动电源测试设备集成控制系统...")
    
    # 创建根窗口
    root = tk.Tk()
    root.title("电源测试设备集成控制系统")
    
    # 强制设置窗口可调整大小
    root.geometry("1200x800")
    root.resizable(True, True)
    root.minsize(800, 600)
    root.maxsize(2560, 1440)
    root.state('normal')
    
    print(f"✅ 窗口配置完成:")
    print(f"   - 初始大小: 1200x800")
    print(f"   - 可调整大小: {root.resizable()}")
    print(f"   - 窗口状态: {root.state()}")
    
    # 创建背景画布
    bg_canvas = tk.Canvas(root, bg="#e3f2fd", highlightthickness=0)
    bg_canvas.pack(fill='both', expand=True)
    
    # 创建主界面对象
    interface = SimpleTkinterToolsInterface()
    interface.root = root
    interface.bg_canvas = bg_canvas
    
    # 强制使用简化界面（确保使用放大版本）
    print("🎯 强制使用放大版简化界面...")
    interface.create_simplified_interface()
    
    print("\n🧪 请验证白色内容区域是否已放大:")
    print("   - 白色区域应该比之前明显更大")
    print("   - 左侧按钮应该更紧凑")
    print("   - 可以拖拽窗口边缘测试响应性")
    
    # 运行主循环
    root.mainloop()


if __name__ == "__main__":
    main()
