"""
tkintertools风格主界面 - 蓝色渐变毛玻璃效果
按照tkintertools的设计风格，包含渐变背景和现代化按钮
"""
import tkinter as tk
from tkinter import ttk
from datetime import datetime
import sys
import os
import math面 - 蓝色渐变风格
按照截图设计，包含CVTE logo和浏览器标签页样式按钮
"""
import tkinter as tk
from tkinter import ttk
from datetime import datetime
import sys
import os
from interface.tab_style_button import TabStyleButton

class ModernMainInterface:
    """现代化主界面"""
    
    def __init__(self, root):
        self.root = root
        self.current_tab = 0
        self.version_label = None
        self.time_label = None
        self.tab_frames = {}  # 初始化tab_frames
        self.setup_window()
        self.create_interface()
        self.update_time()
    
    def setup_window(self):
        """设置窗口属性"""
        self.root.title("电源测试设备集成控制系统")
        self.root.geometry("1200x800")
        self.root.configure(bg='#7BA7D9')  # 蓝色背景
        
        # 设置窗口最小尺寸
        self.root.minsize(1000, 600)
        
        # 让窗口在屏幕中央打开
        self.center_window()
    
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
        # 创建顶部白色框架（包含logo和标签按钮）
        top_frame = tk.Frame(self.root, bg='#FFFFFF', height=120)
        top_frame.pack(fill=tk.X, padx=10, pady=(10, 0))
        top_frame.pack_propagate(False)
        
        # CVTE Logo区域
        logo_frame = tk.Frame(top_frame, bg='#FFFFFF', width=200, height=120)
        logo_frame.pack(side=tk.LEFT, fill=tk.Y)
        logo_frame.pack_propagate(False)
        
        # 检查是否存在CVTE logo图片
        logo_path = "CVTE logo1.png"
        if os.path.exists(logo_path):
            try:
                from PIL import Image, ImageTk
                # 加载并调整logo尺寸
                img = Image.open(logo_path)
                img = img.resize((180, 80), Image.Resampling.LANCZOS)
                self.logo_photo = ImageTk.PhotoImage(img)
                
                logo_label = tk.Label(logo_frame, image=self.logo_photo, bg='#FFFFFF')
                logo_label.pack(expand=True)
            except ImportError:
                # 如果没有PIL，使用文字logo
                self.create_text_logo(logo_frame)
        else:
            # 使用文字logo
            self.create_text_logo(logo_frame)
        
        # 标签按钮区域
        button_area = tk.Frame(top_frame, bg='#FFFFFF')
        button_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(50, 20))
        
        # 按钮容器 - 垂直居中
        btn_container = tk.Frame(button_area, bg='#FFFFFF')
        btn_container.pack(expand=True, anchor='center')
        
        # 创建标签页样式按钮
        tab_names = ["测试主界面", "自定义功能", "仪器指令", "手动控制", "设备端口"]
        self.buttons = []
        
        for i, name in enumerate(tab_names):
            btn = TabStyleButton(
                btn_container,
                text=name,
                width=120,
                height=50,
                corner_radius=18,  # 增大圆角半径，更接近长方形椭圆效果
                bg_color='#4A7FB8',  # 深蓝色
                fg_color='white',
                hover_bg='#5A8FC8',
                hover_fg='white',
                active_bg='#FFFFFF',
                active_fg='#4A7FB8',
                border_color='#ddd',
                border_width=1,
                font=('Microsoft YaHei', 11, 'bold'),
                command=lambda idx=i: self.switch_tab(idx)
            )
            btn.pack(side=tk.LEFT, padx=3, pady=25)  # 减少间距让标签更紧密
            self.buttons.append(btn)
            print(f"✅ 创建按钮: {name}")
        
        # 主内容区域
        self.content_frame = tk.Frame(self.root, bg='#FFFFFF', relief='flat', bd=0)
        self.content_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=(5, 10))
        
        # 创建右下角状态区域
        self.create_status_area()
        
        # 加载标签内容
        self.load_tab_content()
        
        # 设置第一个按钮为选中状态
        if self.buttons:
            self.buttons[0].set_active(True)
    
    def create_text_logo(self, logo_frame):
        """创建文字logo"""
        logo_label = tk.Label(logo_frame, text="CVTE", 
                             font=('Arial', 28, 'bold'),
                             bg='#FFFFFF', fg='#E31E24')  # 红色CVTE
        logo_label.pack(expand=True)
    
    def create_status_area(self):
        """创建右下角状态区域"""
        # 状态栏容器
        status_container = tk.Frame(self.root, bg='#7BA7D9', height=30)
        status_container.pack(fill=tk.X, side=tk.BOTTOM)
        status_container.pack_propagate(False)
        
        # 右侧状态信息框架
        right_status = tk.Frame(status_container, bg='#7BA7D9')
        right_status.pack(side=tk.RIGHT, padx=10, pady=5)
        
        # 版本信息
        version = self.get_version_info()
        self.version_label = tk.Label(right_status, text=f"版本: {version}",
                                     font=('Microsoft YaHei', 9),
                                     bg='#7BA7D9', fg='#FFFFFF')
        self.version_label.pack(side=tk.RIGHT, padx=(0, 20))
        
        # 时间信息
        self.time_label = tk.Label(right_status, text="",
                                  font=('Microsoft YaHei', 9),
                                  bg='#7BA7D9', fg='#FFFFFF')
        self.time_label.pack(side=tk.RIGHT, padx=(0, 10))
    
    def get_version_info(self):
        """获取版本信息"""
        try:
            # 尝试从主文件获取版本信息
            sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            import main_new
            return main_new.VERSION
        except:
            return "V1.0"
    
    def update_time(self):
        """更新时间显示"""
        if self.time_label:
            current_time = datetime.now().strftime("%H:%M:%S")
            self.time_label.config(text=current_time)
        
        # 每秒更新一次
        self.root.after(1000, self.update_time)
    
    def load_tab_content(self):
        """加载标签内容"""
        # 导入各个标签页
        try:
            from interface.tabs.test_main import TestMainTab
            from interface.tabs.custom_function import CustomFunctionTab
            from interface.tabs.instrument_command import InstrumentCommandTab
            from interface.tabs.manual_control import ManualControlTab
            from interface.tabs.device_port import DevicePortTab
            
            # 创建各个标签页的内容框架
            self.tab_frames = {}
            self.tab_classes = {
                "测试主界面": TestMainTab,
                "自定义功能": CustomFunctionTab,
                "仪器指令": InstrumentCommandTab,
                "手动控制": ManualControlTab,
                "设备端口": DevicePortTab
            }
            
            # 预创建所有标签页框架
            for tab_name, tab_class in self.tab_classes.items():
                frame = tk.Frame(self.content_frame, bg='#FFFFFF')
                self.tab_frames[tab_name] = frame
                # 初始化标签页内容
                tab_class(frame)
            
            # 显示第一个标签页
            self.show_content("测试主界面")
            
        except Exception as e:
            print(f"加载标签内容时出错: {e}")
            # 如果加载失败，显示默认内容
            self.show_default_content("测试主界面")
    
    def switch_tab(self, index):
        """切换标签"""
        tab_names = ["测试主界面", "自定义功能", "仪器指令", "手动控制", "设备端口"]
        tab_name = tab_names[index]
        
        print(f"切换到标签: {tab_name}")
        
        # 重置所有按钮状态
        for btn in self.buttons:
            btn.set_active(False)
        
        # 设置当前按钮为选中
        self.buttons[index].set_active(True)
        
        # 显示对应内容
        self.show_content(tab_name)
    
    def show_content(self, tab_name):
        """显示标签内容"""
        # 隐藏所有标签页
        for frame in self.tab_frames.values():
            frame.pack_forget()
        
        # 显示选中的标签页
        if tab_name in self.tab_frames:
            self.tab_frames[tab_name].pack(fill=tk.BOTH, expand=True)
        else:
            self.show_default_content(tab_name)
    
    def show_default_content(self, tab_name):
        """显示默认内容"""
        # 清除之前的内容
        for widget in self.content_frame.winfo_children():
            if not hasattr(widget, '_is_tab_frame'):
                widget.destroy()
        
        # 显示默认内容
        default_frame = tk.Frame(self.content_frame, bg='#FFFFFF')
        default_frame.pack(fill=tk.BOTH, expand=True)
        default_frame._is_tab_frame = True
        
        content_label = tk.Label(default_frame, 
                               text=f"当前标签: {tab_name}\n\n这是 {tab_name} 的内容区域",
                               font=('Microsoft YaHei', 14),
                               bg='#FFFFFF', fg='#333333')
        content_label.pack(expand=True)

def main():
    """主函数"""
    print("🚀 启动现代化界面...")
    
    root = tk.Tk()
    app = ModernMainInterface(root)
    
    print("✅ 现代化界面启动完成")
    print("🎯 界面采用蓝色渐变风格，包含CVTE logo和浏览器标签页样式按钮")
    
    root.mainloop()

if __name__ == "__main__":
    main()
