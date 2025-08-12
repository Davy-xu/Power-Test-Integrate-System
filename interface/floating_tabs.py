"""
悬空标签组件
实现类似现代网站导航栏的悬空标签效果
使用增强版圆角平行四边形按钮
"""
import tkinter as tk
from tkinter import ttk
from .enhanced_parallelogram_button import EnhancedParallelogramButton


class FloatingTabFrame:
    """悬空标签框架"""
    
    def __init__(self, parent):
        self.parent = parent
        self.current_tab = 0
        self.tabs = []
        self.tab_frames = []
        self.tab_buttons = []
        
        # 创建主容器
        self.main_container = tk.Frame(parent, bg='#f5f5f5')
        self.main_container.pack(fill=tk.BOTH, expand=True)
        
        # 创建悬空标签栏
        self.create_floating_tab_bar()
        
        # 创建内容区域
        self.content_area = tk.Frame(self.main_container, bg='#ffffff', relief='flat', bd=0)
        self.content_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))
    
    def create_floating_tab_bar(self):
        """创建悬空标签栏"""
        # 标签栏容器 - 带背景间距实现悬空效果，增加高度
        self.tab_bar_container = tk.Frame(self.main_container, bg='#f5f5f5', height=80)
        self.tab_bar_container.pack(fill=tk.X, pady=(10, 5))
        self.tab_bar_container.pack_propagate(False)  # 重要：固定高度
        
        # 标签栏 - 居中放置
        self.tab_bar = tk.Frame(self.tab_bar_container, bg='#f5f5f5')
        self.tab_bar.pack(expand=True, pady=10)
    
    def add_tab(self, text, content_frame):
        """添加悬空标签"""
        tab_index = len(self.tabs)
        
        # 创建标签容器 - 固定尺寸确保按钮可见
        tab_container = tk.Frame(self.tab_bar, bg='#f5f5f5', width=130, height=55)
        tab_container.pack(side=tk.LEFT, padx=5)
        tab_container.pack_propagate(False)  # 重要：固定容器尺寸
        
        # 创建主按钮（简化，不使用阴影）
        tab_button = EnhancedParallelogramButton(
            tab_container,
            text=text,
            width=120,
            height=45,
            skew=15,
            bg_color='#4a90e2',
            fg_color='white',
            hover_bg='#357abd', 
            hover_fg='white',
            active_bg='#ffffff',
            active_fg='#4a90e2',
            command=lambda idx=tab_index: self.switch_tab(idx)
        )
        tab_button.pack(pady=5)  # 使用pack布局而不是place
        
        print(f"✅ 创建标签按钮: {text}")  # 调试信息
        
        # 存储标签信息
        self.tabs.append(text)
        self.tab_buttons.append(tab_button)
        self.tab_frames.append(content_frame)
        
        # 将内容框架添加到内容区域
        content_frame.pack(in_=self.content_area, fill=tk.BOTH, expand=True)
        
        # 如果是第一个标签，设为选中状态
        if tab_index == 0:
            self.switch_tab(0)
        else:
            content_frame.pack_forget()
    
    def switch_tab(self, tab_index):
        """切换标签"""
        if tab_index == self.current_tab:
            return
        
        # 重置当前标签状态
        if self.current_tab < len(self.tab_buttons):
            self.tab_frames[self.current_tab].pack_forget()
            self.tab_buttons[self.current_tab].set_active(False)
        
        # 显示新标签内容
        self.tab_frames[tab_index].pack(fill=tk.BOTH, expand=True)
        self.tab_buttons[tab_index].set_active(True)
        
        self.current_tab = tab_index


class FloatingTabNotebook:
    """悬空标签笔记本 - 替代ttk.Notebook"""
    
    def __init__(self, parent):
        self.floating_frame = FloatingTabFrame(parent)
        self.tabs = []
    
    def add(self, frame, text=""):
        """添加标签页"""
        self.floating_frame.add_tab(text, frame)
        self.tabs.append((frame, text))
    
    def pack(self, **kwargs):
        """布局方法"""
        self.floating_frame.main_container.pack(**kwargs)
    
    def grid(self, **kwargs):
        """网格布局方法"""
        self.floating_frame.main_container.grid(**kwargs)
