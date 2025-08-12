#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
窗口最大化/最小化/恢复防卡顿测试
测试窗口状态变化时的性能表现
"""
import tkinter as tk
from datetime import datetime
import time
import threading

class WindowStateTest:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("窗口状态变化防卡顿测试")
        self.root.geometry("1000x700")
        self.root.configure(bg='#2d2d30')
        
        self.test_count = 0
        self.performance_data = []
        
        self.setup_test_ui()
        self.bind_window_events()
        self.start_performance_monitor()
        
    def setup_test_ui(self):
        """设置测试界面"""
        # 创建主画布
        self.canvas = tk.Canvas(self.root, bg='#3c3c3c', highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # 标题
        self.canvas.create_text(
            500, 50, text="窗口状态变化防卡顿测试",
            font=('Microsoft YaHei', 18, 'bold'),
            fill='white', anchor='center'
        )
        
        # 测试说明
        instructions = [
            "测试目的：验证窗口最大化/最小化/恢复时是否会卡顿",
            "",
            "测试操作：",
            "1. 点击窗口标题栏的最大化按钮 □",
            "2. 再次点击恢复窗口大小",
            "3. 点击最小化按钮 —",
            "4. 从任务栏恢复窗口",
            "5. 多次重复上述操作",
            "",
            "观察要点：",
            "• 操作是否流畅，无明显卡顿",
            "• 界面元素是否正确显示",
            "• 性能计数器是否正常更新",
            "• 时间显示是否连续",
            "",
            "性能信息："
        ]
        
        for i, instruction in enumerate(instructions):
            y_pos = 100 + i * 25
            color = '#ffffff' if not instruction.startswith(('•', '1.', '2.', '3.', '4.', '5.')) else '#4a9eff'
            weight = 'bold' if instruction.endswith('：') else 'normal'
            
            self.canvas.create_text(
                50, y_pos, text=instruction,
                font=('Microsoft YaHei', 11, weight),
                fill=color, anchor='w'
            )
        
        # 性能信息显示区域
        self.performance_y = 100 + len(instructions) * 25
        self.create_performance_display()
        
        # 创建底部状态栏
        self.create_status_bar()
        
        # 启动时间更新
        self.update_time()
        
    def create_performance_display(self):
        """创建性能显示区域"""
        # 性能标题
        self.canvas.create_text(
            50, self.performance_y, text="实时性能监控：",
            font=('Microsoft YaHei', 12, 'bold'),
            fill='#4a9eff', anchor='w'
        )
        
        # 性能数据文本
        self.perf_texts = {}
        perf_items = [
            ("state_changes", "状态变化次数: 0"),
            ("last_operation", "最后操作: 无"),
            ("response_time", "响应时间: - ms"),
            ("avg_response", "平均响应: - ms"),
            ("status", "状态: 正常")
        ]
        
        for i, (key, text) in enumerate(perf_items):
            y_pos = self.performance_y + 30 + i * 25
            self.perf_texts[key] = self.canvas.create_text(
                70, y_pos, text=text,
                font=('Consolas', 10),
                fill='#cccccc', anchor='w'
            )
            
    def create_status_bar(self):
        """创建状态栏"""
        self.root.update_idletasks()
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        
        # 状态栏位置
        status_y = canvas_height - 65
        status_height = 50
        
        # 清除旧状态栏
        self.canvas.delete("status_bar")
        
        # 状态栏背景
        self.canvas.create_rectangle(
            0, status_y, canvas_width, status_y + status_height,
            fill='#2c3e50', outline='#34495e', width=1, tags="status_bar"
        )
        
        # 状态文本
        self.status_text = self.canvas.create_text(
            20, status_y + 25, text="测试准备中...",
            font=('Microsoft YaHei', 11), fill='#ecf0f1',
            anchor='w', tags="status_bar"
        )
        
        # 时间显示
        self.time_text = self.canvas.create_text(
            canvas_width - 20, status_y + 25, text="",
            font=('Consolas', 12, 'bold'), fill='#3498db',
            anchor='e', tags="status_bar"
        )
        
    def bind_window_events(self):
        """绑定窗口事件"""
        # 绑定窗口状态变化事件
        self.root.bind('<Configure>', self.on_window_configure)
        self.root.bind('<Map>', self.on_window_map)
        self.root.bind('<Unmap>', self.on_window_unmap)
        
        # 记录初始状态
        self.last_state = self.root.state()
        self.last_geometry = self.root.geometry()
        
    def on_window_configure(self, event):
        """窗口配置变化事件"""
        if event.widget == self.root:
            current_time = time.time()
            current_state = self.root.state()
            current_geometry = self.root.geometry()
            
            # 检测状态变化
            if hasattr(self, 'last_state') and self.last_state != current_state:
                self.record_state_change("状态变化", current_state, current_time)
                
            # 检测大小变化
            if hasattr(self, 'last_geometry') and self.last_geometry != current_geometry:
                self.record_state_change("大小变化", current_geometry, current_time)
                
            self.last_state = current_state
            self.last_geometry = current_geometry
            
            # 延迟更新状态栏
            self.root.after(100, self.create_status_bar)
            
    def on_window_map(self, event):
        """窗口映射事件（显示）"""
        self.record_state_change("窗口显示", "显示", time.time())
        
    def on_window_unmap(self, event):
        """窗口取消映射事件（隐藏/最小化）"""
        self.record_state_change("窗口隐藏", "最小化", time.time())
        
    def record_state_change(self, operation, detail, timestamp):
        """记录状态变化"""
        self.test_count += 1
        
        # 计算响应时间
        if hasattr(self, 'last_timestamp'):
            response_time = (timestamp - self.last_timestamp) * 1000  # 转换为毫秒
        else:
            response_time = 0
            
        self.last_timestamp = timestamp
        self.performance_data.append(response_time)
        
        # 保持最近100次数据
        if len(self.performance_data) > 100:
            self.performance_data.pop(0)
            
        # 计算平均响应时间
        avg_response = sum(self.performance_data) / len(self.performance_data) if self.performance_data else 0
        
        # 更新性能显示
        self.update_performance_display(operation, detail, response_time, avg_response)
        
        print(f"🔄 状态变化: {operation} -> {detail}, 响应时间: {response_time:.1f}ms")
        
    def update_performance_display(self, operation, detail, response_time, avg_response):
        """更新性能显示"""
        try:
            # 更新计数
            self.canvas.itemconfig(
                self.perf_texts["state_changes"],
                text=f"状态变化次数: {self.test_count}"
            )
            
            # 更新最后操作
            self.canvas.itemconfig(
                self.perf_texts["last_operation"],
                text=f"最后操作: {operation} ({detail})"
            )
            
            # 更新响应时间
            self.canvas.itemconfig(
                self.perf_texts["response_time"],
                text=f"响应时间: {response_time:.1f} ms"
            )
            
            # 更新平均响应时间
            self.canvas.itemconfig(
                self.perf_texts["avg_response"],
                text=f"平均响应: {avg_response:.1f} ms"
            )
            
            # 更新状态（根据响应时间判断）
            if avg_response < 50:
                status = "优秀"
                color = "#2ecc71"
            elif avg_response < 100:
                status = "良好"
                color = "#f39c12"
            else:
                status = "需要优化"
                color = "#e74c3c"
                
            self.canvas.itemconfig(
                self.perf_texts["status"],
                text=f"状态: {status}",
                fill=color
            )
            
        except Exception as e:
            print(f"❌ 性能显示更新失败: {e}")
            
    def update_time(self):
        """更新时间显示"""
        try:
            if hasattr(self, 'time_text'):
                current_time = datetime.now().strftime("%H:%M:%S")
                self.canvas.itemconfig(self.time_text, text=current_time)
                
            # 更新状态文本
            if hasattr(self, 'status_text'):
                if self.test_count == 0:
                    status = "测试准备中..."
                else:
                    status = f"测试进行中 | 已执行 {self.test_count} 次操作"
                self.canvas.itemconfig(self.status_text, text=status)
                
        except Exception as e:
            print(f"❌ 时间更新失败: {e}")
        
        # 每秒更新
        self.root.after(1000, self.update_time)
        
    def start_performance_monitor(self):
        """启动性能监控"""
        def monitor():
            while True:
                try:
                    # 每5秒报告一次性能
                    time.sleep(5)
                    if self.performance_data:
                        avg = sum(self.performance_data) / len(self.performance_data)
                        print(f"📊 性能报告: 平均响应时间 {avg:.1f}ms, 操作次数 {self.test_count}")
                except:
                    break
                    
        thread = threading.Thread(target=monitor, daemon=True)
        thread.start()
        
    def run(self):
        """运行测试"""
        print("🧪 启动窗口状态变化防卡顿测试")
        print("请执行以下操作来测试性能：")
        print("- 最大化窗口（点击 □ 按钮）")
        print("- 恢复窗口大小（再次点击按钮）")
        print("- 最小化窗口（点击 — 按钮）")
        print("- 从任务栏恢复窗口")
        print()
        
        self.root.mainloop()

if __name__ == "__main__":
    test = WindowStateTest()
    test.run()
