"""
主界面管理器
整合所有界面组件
"""
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import sys
import os

def get_version_info_from_main():
    """动态获取版本信息，避免循环导入"""
    try:
        # 添加父目录到路径
        sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        import main_new
        return main_new.get_version_info(), main_new.VERSION, main_new.BUILD_DATE
    except ImportError:
        return "V1.0 Unknown", "V1.0", "Unknown"

from .styles import StyleManager
from .top_frame import TopFrame
from .floating_tabs import FloatingTabNotebook
from .tabs.test_main import TestMainTab
from .tabs.custom_function import CustomFunctionTab
from .tabs.instrument_command import InstrumentCommandTab
from .tabs.manual_control import ManualControlTab
from .tabs.device_port import DevicePortTab


class MainInterface:
    """主界面管理器"""
    
    def __init__(self, root):
        self.root = root
        self.notebook = None
        self.style_manager = None
        self.top_frame = None
        self.menu_bar = None
        self.status_bar = None
        self.time_label = None
        
        # 设置窗口属性
        self.setup_window()
        
        # 初始化样式
        self.style_manager = StyleManager()
        
        # 创建主界面
        self.create_main_interface()
        
        # 启动时间更新
        self.update_time()
    
    def setup_window(self):
        """设置窗口属性"""
        self.root.title("电源测试设备集成控制系统")
        self.root.geometry("1200x800")
        self.root.configure(bg='#f5f5f5')  # 浅色背景匹配浏览器标签样式
        
        # 设置窗口最小尺寸，确保界面完整显示（增加高度以确保状态栏显示）
        self.root.minsize(1200, 800)
        
        # 让窗口在屏幕中央打开
        self.center_window()
        
        # 设置窗口图标（如果有的话）
        # self.root.iconbitmap("icon.ico")
    
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
    
    def create_main_interface(self):
        """创建主界面"""
        # 创建菜单栏
        self.create_menu_bar()
        
        # 创建主框架，减少边距以便在小窗口中完整显示
        main_frame = ttk.Frame(self.root, style='Dark.TFrame')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # 创建顶部框架（包含logo和标题）
        self.top_frame = TopFrame(main_frame)
        
        # 创建悬空标签笔记本，替代原来的ttk.Notebook
        self.notebook = FloatingTabNotebook(main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True, pady=(0, 5))
        
        # 创建各个选项卡
        self.create_tabs()
    
    def create_tabs(self):
        """创建所有选项卡"""
        # 为悬空标签系统创建标签页框架
        
        # 创建测试主界面选项卡
        test_frame = tk.Frame(bg='#ffffff')
        self.notebook.add(test_frame, text="测试主界面")
        TestMainTab(test_frame)  # 传入框架而不是notebook
        
        # 创建自定义功能选项卡
        custom_frame = tk.Frame(bg='#ffffff')
        self.notebook.add(custom_frame, text="自定义功能")
        CustomFunctionTab(custom_frame)
        
        # 创建仪器指令选项卡
        instrument_frame = tk.Frame(bg='#ffffff')
        self.notebook.add(instrument_frame, text="仪器指令")
        InstrumentCommandTab(instrument_frame)
        
        # 创建手动控制选项卡
        manual_frame = tk.Frame(bg='#ffffff')
        self.notebook.add(manual_frame, text="手动控制")
        ManualControlTab(manual_frame)
        
        # 创建设备端口选项卡
        device_frame = tk.Frame(bg='#ffffff')
        self.notebook.add(device_frame, text="设备端口")
        DevicePortTab(device_frame)
    
    def create_menu_bar(self):
        """创建顶部菜单栏"""
        # 创建菜单栏框架，背景色改为浅色主题
        self.menu_bar = tk.Frame(self.root, bg='#e8e8e8', height=35)
        self.menu_bar.pack(fill=tk.X, side=tk.TOP)
        self.menu_bar.pack_propagate(False)  # 固定高度
        
        # 创建关于按钮（放在左边）
        about_button = tk.Button(self.menu_bar,
                                text="关于",
                                bg='#d0d0d0',
                                fg='#333333',
                                font=('Microsoft YaHei', 10, 'normal'),
                                relief='flat',
                                borderwidth=0,
                                padx=15,
                                command=self.show_about)
        about_button.pack(side=tk.LEFT, padx=5, pady=5)
        
        # 创建帮助按钮（放在左边）
        help_button = tk.Button(self.menu_bar,
                               text="帮助",
                               bg='#d0d0d0',
                               fg='#333333',
                               font=('Microsoft YaHei', 10, 'normal'),
                               relief='flat',
                               borderwidth=0,
                               padx=15,
                               command=self.show_help)
        help_button.pack(side=tk.LEFT, padx=5, pady=5)
        
        # 右侧时间显示
        self.time_label = tk.Label(self.menu_bar, 
                                  text="00:00:00",
                                  bg='#e8e8e8',
                                  fg='#333333',
                                  font=('Microsoft YaHei', 10, 'normal'))
        self.time_label.pack(side=tk.RIGHT, padx=8, pady=5)
        
        # 右侧版本信息
        version_info, _, _ = get_version_info_from_main()
        version_label = tk.Label(self.menu_bar, 
                                text=version_info,
                                bg='#e8e8e8',
                                fg='#333333',
                                font=('Microsoft YaHei', 10, 'normal'))
        version_label.pack(side=tk.RIGHT, padx=8, pady=5)
        
        # 为按钮添加悬停效果
        self.add_hover_effect(help_button)
        self.add_hover_effect(about_button)
    
    def add_hover_effect(self, button):
        """为按钮添加悬停效果"""
        def on_enter(e):
            button.config(bg='#c0c0c0')  # 悬停时更深的灰色
            
        def on_leave(e):
            button.config(bg='#d0d0d0')  # 恢复到原背景色
            
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)
    
    def show_help(self):
        """显示帮助信息"""
        help_text = """电源测试设备集成控制系统 - 帮助

使用说明：
1. 测试主界面：进行各种电源测试操作
2. 自定义功能：配置自定义的测试功能
3. 仪器指令：发送SCPI指令到测试设备
4. 手动控制：手动控制电压、电流等参数
5. 设备端口：配置设备连接和通信端口

快捷键：
- F1：显示帮助
- Ctrl+Q：退出程序
- F5：刷新界面

如需更多帮助，请联系技术支持。"""
        
        messagebox.showinfo("帮助", help_text)
    
    def show_about(self):
        """显示关于信息"""
        _, version, build_date = get_version_info_from_main()
        about_text = f"""电源测试设备集成控制系统

版本：{version}
构建：{build_date}
发布日期：2025年8月5日 11:22

开发团队：CVTE
技术支持：support@cvte.com

本软件用于电源测试设备的集成控制，
提供完整的测试、监控和数据管理功能。

© 2025 CVTE. 保留所有权利。"""
        
        messagebox.showinfo("关于", about_text)
    
    def update_time(self):
        """更新时间显示"""
        if self.time_label:
            current_time = datetime.now().strftime("%H:%M:%S")
            self.time_label.config(text=current_time)
        
        # 每秒更新一次
        self.root.after(1000, self.update_time)
