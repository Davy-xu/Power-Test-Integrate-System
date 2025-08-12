"""
测试主界面选项卡
"""
import tkinter as tk
from tkinter import ttk


class TestMainTab:
    """测试主界面选项卡"""
    
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        self.status_text = None
        # 创建选项卡内容
        self.create_content()

    
    def create_content(self):
        """创建测试主界面内容"""
        # 直接在传入的parent_frame中创建内容
        # 创建标题
        title_label = tk.Label(self.parent_frame, 
                              text="测试主界面", 
                              font=('Microsoft YaHei', 16, 'bold'),
                              bg='#ffffff',
                              fg='#333333')
        title_label.pack(pady=20)
        
        # 创建测试内容
        content_label = tk.Label(self.parent_frame, 
                                text="这里是测试主界面的内容区域", 
                                font=('Microsoft YaHei', 12),
                                bg='#ffffff',
                                fg='#666666')
        content_label.pack(pady=10)
        
