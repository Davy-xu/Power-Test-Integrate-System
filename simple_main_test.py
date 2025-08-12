#!/usr/bin/env python3
"""
直接替换主函数的简化版本
"""
import tkinter as tk
from tkinter import ttk
from datetime import datetime
import sys
import os

def create_simple_main():
    """创建简化的主界面"""
    print("🚀 启动简化版电源测试集成系统...")
    
    # 创建根窗口
    root = tk.Tk()
    root.title("电源测试设备集成控制系统")
    
    # 强制设置窗口属性
    root.geometry("1200x800")
    root.resizable(True, True)
    root.minsize(800, 600)
    root.maxsize(2560, 1440)
    
    # 尝试多种方法确保窗口可调整大小
    try:
        root.wm_resizable(True, True)
    except:
        pass
    
    try:
        root.attributes('-zoomed', False)  # Linux
    except:
        pass
    
    try:
        root.state('normal')
    except:
        pass
    
    print(f"✅ 窗口配置:")
    print(f"   - 几何设置: {root.geometry()}")
    print(f"   - 可调整大小: {root.resizable()}")
    print(f"   - 窗口状态: {root.state()}")
    
    # 创建主框架
    main_frame = tk.Frame(root, bg='#e3f2fd')
    main_frame.pack(fill='both', expand=True)
    
    # 标题
    title_label = tk.Label(main_frame,
                          text="电源测试设备集成控制系统",
                          font=('Microsoft YaHei UI', 18, 'bold'),
                          bg='#e3f2fd', fg='#1565c0')
    title_label.pack(pady=30)
    
    # 左侧按钮框架
    left_frame = tk.Frame(main_frame, bg='#bbdefb', width=200)
    left_frame.pack(side='left', fill='y', padx=10, pady=10)
    left_frame.pack_propagate(False)
    
    # 按钮列表
    buttons = ["测试主界面", "自定义功能", "仪器指令", "手动控制", 
               "设备端口", "系统运行日志", "数据同步", "系统信息", "帮助"]
    
    for i, btn_text in enumerate(buttons):
        btn = tk.Button(left_frame,
                       text=btn_text,
                       font=('Microsoft YaHei UI', 10),
                       bg='#42a5f5' if i == 0 else '#90caf9',
                       fg='white' if i == 0 else '#0d47a1',
                       relief='flat',
                       width=15,
                       height=2)
        btn.pack(pady=5, padx=10)
    
    # 右侧内容框架
    content_frame = tk.Frame(main_frame, bg='white', relief='raised', bd=1)
    content_frame.pack(side='right', fill='both', expand=True, padx=10, pady=10)
    
    # 内容标题
    content_title = tk.Label(content_frame,
                            text="测试主界面",
                            font=('Microsoft YaHei UI', 14, 'bold'),
                            bg='white', fg='#1565c0')
    content_title.pack(pady=20)
    
    # 状态信息
    status_frame = tk.Frame(content_frame, bg='#f5f5f5', relief='groove', bd=1)
    status_frame.pack(fill='x', padx=20, pady=10)
    
    status_info = tk.Label(status_frame,
                          text="系统状态\n✓ 设备连接状态: 已连接\n✓ 数据采集状态: 就绪\n⦿ 测试进度: 0%\n⏰ 运行时间: 00:00:00",
                          font=('Microsoft YaHei UI', 10),
                          bg='#f5f5f5', fg='#424242',
                          justify='left')
    status_info.pack(pady=10, padx=10)
    
    # 窗口信息显示
    window_info_label = tk.Label(content_frame,
                                text="",
                                font=('Microsoft YaHei UI', 9),
                                bg='white', fg='#666666')
    window_info_label.pack(pady=10)
    
    # 底部状态栏
    status_bar = tk.Frame(root, bg='#263238', height=30)
    status_bar.pack(side='bottom', fill='x')
    status_bar.pack_propagate(False)
    
    current_label = tk.Label(status_bar,
                            text="当前: 测试主界面",
                            font=('Microsoft YaHei UI', 9),
                            bg='#263238', fg='#b0bec5')
    current_label.pack(side='left', padx=10, pady=5)
    
    time_label = tk.Label(status_bar,
                         text="",
                         font=('Microsoft YaHei UI', 9),
                         bg='#263238', fg='#b0bec5')
    time_label.pack(side='right', padx=10, pady=5)
    
    # 更新时间和窗口信息
    def update_info():
        try:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            time_label.config(text=current_time)
            
            width = root.winfo_width()
            height = root.winfo_height()
            state = root.state()
            
            window_info = f"窗口信息: {width}×{height} | 状态: {state} | 可调整: {root.resizable()}"
            window_info_label.config(text=window_info)
            
            root.after(1000, update_info)
        except:
            pass
    
    update_info()
    
    print("\n🧪 测试窗口调整大小:")
    print("1. 拖拽窗口边缘")
    print("2. 双击标题栏")
    print("3. 使用最大化按钮")
    print("4. 观察窗口信息更新\n")
    
    # 运行主循环
    root.mainloop()

if __name__ == "__main__":
    create_simple_main()
