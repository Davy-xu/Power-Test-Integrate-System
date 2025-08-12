#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
界面移动一致性修复测试
确保移动界面前后显示完全一致
"""
import tkinter as tk
from datetime import datetime
import time

class WindowMoveConsistencyTest:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("界面移动一致性测试")
        self.root.geometry("1200x800")
        self.root.configure(bg='#2d2d30')
        
        self.setup_test_ui()
        self.track_window_events()
        
    def setup_test_ui(self):
        """设置测试界面"""
        # 创建主画布
        self.canvas = tk.Canvas(self.root, bg='#3c3c3c', highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # 测试说明标题
        self.canvas.create_text(
            600, 50, text="界面移动一致性测试",
            font=('Microsoft YaHei', 18, 'bold'),
            fill='white', anchor='center'
        )
        
        # 测试说明
        instructions = [
            "测试目的：验证移动界面前后显示是否一致",
            "测试步骤：",
            "1. 观察当前界面的底部状态栏和时间显示",
            "2. 拖动窗口标题栏移动界面位置",
            "3. 调整窗口大小（拖拽边框或角落）",
            "4. 检查底部状态栏和时间显示是否保持一致",
            "5. 观察时间是否持续更新",
            "",
            "预期结果：",
            "• 移动/调整窗口后，底部状态栏位置保持稳定",
            "• 时间显示始终在右下角，颜色为蓝色",
            "• 时间每秒自动更新，不会丢失或停止",
            "• 整体布局保持一致，无闪烁或错位"
        ]
        
        for i, instruction in enumerate(instructions):
            y_pos = 120 + i * 25
            color = '#ffffff' if not instruction.startswith(('•', '1.', '2.', '3.', '4.', '5.')) else '#4a9eff'
            weight = 'bold' if instruction.endswith('：') else 'normal'
            
            self.canvas.create_text(
                50, y_pos, text=instruction,
                font=('Microsoft YaHei', 11, weight),
                fill=color, anchor='w'
            )
        
        # 创建状态栏
        self.create_status_bar()
        
        # 绑定窗口事件
        self.root.bind('<Configure>', self.on_window_change)
        
        # 启动时间更新
        self.update_time()
        
    def create_status_bar(self):
        """创建测试状态栏"""
        # 获取画布尺寸
        self.root.update_idletasks()
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        
        # 状态栏位置（底部65像素：50像素高度+15像素边距）
        status_y = canvas_height - 65
        status_height = 50
        
        # 清除旧状态栏
        self.canvas.delete("status_bar")
        
        # 状态栏背景
        self.canvas.create_rectangle(
            0, status_y, canvas_width, status_y + status_height,
            fill='#2c3e50', outline='#34495e', width=1, tags="status_bar"
        )
        
        # 状态文本（左侧）
        self.status_text = self.canvas.create_text(
            20, status_y + 25, text="测试进行中 | 观察界面一致性",
            font=('Microsoft YaHei', 11), fill='#ecf0f1',
            anchor='w', tags="status_bar"
        )
        
        # 当前时间（右侧）
        self.time_text = self.canvas.create_text(
            canvas_width - 20, status_y + 25, text="",
            font=('Consolas', 12, 'bold'), fill='#3498db',
            anchor='e', tags="status_bar"
        )
        
        # 窗口信息（中间）
        window_info = f"窗口尺寸: {canvas_width}x{canvas_height}"
        self.window_info_text = self.canvas.create_text(
            canvas_width // 2, status_y + 25, text=window_info,
            font=('Consolas', 10), fill='#95a5a6',
            anchor='center', tags="status_bar"
        )
        
        print(f"✅ 测试状态栏创建完成: {canvas_width}x{canvas_height}, 状态栏y={status_y}")
        
    def update_time(self):
        """更新时间显示"""
        try:
            if hasattr(self, 'time_text'):
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.canvas.itemconfig(self.time_text, text=current_time)
                
            # 更新状态文本
            if hasattr(self, 'status_text'):
                status_messages = [
                    "测试进行中 | 观察界面一致性",
                    "状态栏测试 | 时间显示正常",
                    "移动测试 | 布局保持稳定",
                    "一致性检查 | 功能运行正常"
                ]
                status_index = int(time.time()) % len(status_messages)
                self.canvas.itemconfig(self.status_text, text=status_messages[status_index])
                
        except Exception as e:
            print(f"❌ 时间更新失败: {e}")
        
        # 每秒更新
        self.root.after(1000, self.update_time)
        
    def on_window_change(self, event=None):
        """窗口变化事件"""
        if event and event.widget == self.root:
            # 防抖：延迟重绘
            if hasattr(self, '_change_timer'):
                self.root.after_cancel(self._change_timer)
            self._change_timer = self.root.after(100, self.handle_window_change)
            
    def handle_window_change(self):
        """处理窗口变化"""
        try:
            print("🔄 窗口发生变化，重新调整状态栏...")
            
            # 重新创建状态栏以适应新尺寸
            self.create_status_bar()
            
            # 更新窗口信息
            if hasattr(self, 'window_info_text'):
                canvas_width = self.canvas.winfo_width()
                canvas_height = self.canvas.winfo_height()
                window_info = f"窗口尺寸: {canvas_width}x{canvas_height}"
                self.canvas.itemconfig(self.window_info_text, text=window_info)
                
        except Exception as e:
            print(f"❌ 窗口变化处理失败: {e}")
            
    def track_window_events(self):
        """跟踪窗口事件"""
        def on_move_start(event):
            print("📱 开始移动窗口...")
            
        def on_move_end(event):
            print("📱 窗口移动结束，检查一致性...")
            # 延迟检查，确保移动完成
            self.root.after(200, self.check_consistency)
            
        # 绑定窗口移动事件（Windows系统）
        self.root.bind('<Button-1>', on_move_start)
        self.root.bind('<ButtonRelease-1>', on_move_end)
        
    def check_consistency(self):
        """检查界面一致性"""
        try:
            # 检查时间文本是否存在且有效
            if hasattr(self, 'time_text'):
                current_time = self.canvas.itemcget(self.time_text, 'text')
                if current_time:
                    print(f"✅ 时间显示正常: {current_time}")
                else:
                    print("⚠️ 时间显示为空")
            else:
                print("❌ 时间文本对象不存在")
                
            # 检查状态栏是否正确显示
            status_items = self.canvas.find_withtag("status_bar")
            print(f"✅ 状态栏元素数量: {len(status_items)}")
            
        except Exception as e:
            print(f"❌ 一致性检查失败: {e}")
            
    def run(self):
        """运行测试"""
        print("🧪 启动界面移动一致性测试")
        print("请拖动窗口和调整大小来测试界面一致性")
        self.root.mainloop()

if __name__ == "__main__":
    test = WindowMoveConsistencyTest()
    test.run()
