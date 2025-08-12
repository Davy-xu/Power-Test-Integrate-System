"""
手动控制选项卡
"""
import tkinter as tk
from tkinter import ttk
import sys
import os

# 导入圆角矩形按钮组件
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from rounded_rect_button import RoundedRectButton


class ManualControlTab:
    """手动控制选项卡"""
    
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        self.create_content()
    
    def create_content(self):
        """创建手动控制内容"""
        # 添加标题
        title_label = tk.Label(self.parent_frame, text="手动控制", 
                              font=('Microsoft YaHei', 16, 'bold'),
                              bg='#ffffff', fg='#333333')
        title_label.pack(pady=20)
        
        # 控制面板框架
        control_panel_frame = tk.LabelFrame(self.parent_frame, text="控制面板", 
                                           bg='#f8f8f8', fg='#333333',
                                           font=('Microsoft YaHei', 12, 'bold'))
        control_panel_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        control_panel_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        content_frame = ttk.Frame(control_panel_frame, style='Dark.TFrame')
        content_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # 左侧控制区域
        self.create_control_area(content_frame)
        
        # 右侧监控区域
        self.create_monitor_area(content_frame)
    
    def create_control_area(self, parent):
        """创建控制区域"""
        left_control = ttk.Frame(parent, style='Dark.TFrame')
        left_control.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)
        
        # 电压控制
        self.create_voltage_control(left_control)
        
        # 电流控制
        self.create_current_control(left_control)
    
    def create_voltage_control(self, parent):
        """创建电压控制"""
        voltage_frame = tk.LabelFrame(parent, text="电压控制", 
                                     bg='#2d2d2d', fg='white',
                                     font=('Microsoft YaHei', 10, 'bold'))
        voltage_frame.pack(fill=tk.X, pady=5)
        
        voltage_content = ttk.Frame(voltage_frame, style='Dark.TFrame')
        voltage_content.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(voltage_content, text="电压值 (V):", style='White.TLabel').grid(row=0, column=0, sticky=tk.W)
        voltage_entry = ttk.Entry(voltage_content, style='Dark.TEntry', width=15)
        voltage_entry.grid(row=0, column=1, padx=5)
        
        # 电压设置按钮容器
        voltage_btn_container = tk.Frame(voltage_content, bg='#2d2d2d', width=80, height=35)
        voltage_btn_container.grid(row=0, column=2, padx=5)
        voltage_btn_container.grid_propagate(False)
        
        # 电压设置按钮 - 圆角矩形
        voltage_btn = RoundedRectButton(
            voltage_btn_container,
            text="设置",
            width=70,
            height=30,
            corner_radius=8,
            bg_color="#4A7FB8",
            fg_color='white',
            hover_bg="#5A8FC8",
            hover_fg='white',
            font=('Microsoft YaHei', 9, 'bold'),
            command=lambda: print("设置电压")
        )
        voltage_btn.pack(expand=True)
    
    def create_current_control(self, parent):
        """创建电流控制"""
        current_frame = tk.LabelFrame(parent, text="电流控制", 
                                     bg='#2d2d2d', fg='white',
                                     font=('Microsoft YaHei', 10, 'bold'))
        current_frame.pack(fill=tk.X, pady=5)
        
        current_content = ttk.Frame(current_frame, style='Dark.TFrame')
        current_content.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(current_content, text="电流值 (A):", style='White.TLabel').grid(row=0, column=0, sticky=tk.W)
        current_entry = ttk.Entry(current_content, style='Dark.TEntry', width=15)
        current_entry.grid(row=0, column=1, padx=5)
        
        # 电流设置按钮容器
        current_btn_container = tk.Frame(current_content, bg='#2d2d2d', width=80, height=35)
        current_btn_container.grid(row=0, column=2, padx=5)
        current_btn_container.grid_propagate(False)
        
        # 电流设置按钮 - 圆角矩形
        current_btn = RoundedRectButton(
            current_btn_container,
            text="设置",
            width=70,
            height=30,
            corner_radius=8,
            bg_color="#4A7FB8",
            fg_color='white',
            hover_bg="#5A8FC8",
            hover_fg='white',
            font=('Microsoft YaHei', 9, 'bold'),
            command=lambda: print("设置电流")
        )
        current_btn.pack(expand=True)
    
    def create_monitor_area(self, parent):
        """创建监控区域"""
        right_control = ttk.Frame(parent, style='Dark.TFrame')
        right_control.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10)
        
        # 实时监控
        monitor_frame = tk.LabelFrame(right_control, text="实时监控", 
                                     bg='#2d2d2d', fg='white',
                                     font=('Microsoft YaHei', 10, 'bold'))
        monitor_frame.pack(fill=tk.BOTH, expand=True)
        
        monitor_content = ttk.Frame(monitor_frame, style='Dark.TFrame')
        monitor_content.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        monitor_labels = ["电压:", "电流:", "功率:", "频率:"]
        for i, label in enumerate(monitor_labels):
            ttk.Label(monitor_content, text=label, style='White.TLabel').grid(row=i, column=0, sticky=tk.W, pady=2)
            value_label = tk.Label(monitor_content, text="0.00", 
                                  bg='#404040', fg='white', relief='sunken',
                                  font=('Consolas', 10))
            value_label.grid(row=i, column=1, sticky=tk.EW, padx=5, pady=2)
        
        monitor_content.columnconfigure(1, weight=1)
