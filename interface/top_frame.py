"""
顶部组件模块
包含CVTE logo和系统标题
"""
import tkinter as tk
from tkinter import ttk


class TopFrame:
    """顶部框架组件"""
    
    def __init__(self, parent):
        self.parent = parent
        self.top_frame = ttk.Frame(parent, style='Dark.TFrame')
        self.logo_photo = None
        self.setup_top_frame()
    
    def setup_top_frame(self):
        """设置顶部框架"""
        # 在CVTE logo上面添加浅色分割线
        separator = tk.Frame(self.parent, height=1, bg='#d0d0d0')
        separator.pack(fill=tk.X, pady=(0, 10))
        
        self.top_frame.pack(fill=tk.X, pady=(0, 10))
        
        # 添加CVTE logo
        self.add_logo()
        
        # 添加居中的系统标题
        self.add_title()
    
    def add_logo(self):
        """添加CVTE logo"""
        try:
            from PIL import Image, ImageTk
            # 加载并调整logo图片大小
            logo_image = Image.open(r"D:\Power Test Integrate System\CVTE logo1.png")
            # 调整logo大小，保持宽高比
            logo_image = logo_image.resize((120, 40), Image.Resampling.LANCZOS)
            self.logo_photo = ImageTk.PhotoImage(logo_image)
            
            # 创建logo标签并放置在左侧
            logo_label = tk.Label(self.top_frame, image=self.logo_photo, bg='#f5f5f5')
            logo_label.pack(side=tk.LEFT, anchor=tk.W, padx=(20, 0))
        except ImportError:
            # 如果没有PIL库，显示文本logo
            logo_label = ttk.Label(self.top_frame, text="CVTE", style='Title.TLabel')
            logo_label.pack(side=tk.LEFT, anchor=tk.W, padx=(20, 0))
        except Exception as e:
            # 如果图片加载失败，显示文本logo
            logo_label = ttk.Label(self.top_frame, text="CVTE", style='Title.TLabel')
            logo_label.pack(side=tk.LEFT, anchor=tk.W, padx=(20, 0))
    
    def add_title(self):
        """添加系统标题"""
        title_label = ttk.Label(self.top_frame, text="电源测试设备集成控制系统", 
                               style='System.Title.TLabel')
        title_label.pack(expand=True)
