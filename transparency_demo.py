"""
透明效果演示程序
展示从普通界面到毛玻璃效果的演进
"""
import tkinter as tk
from tkinter import ttk
import sys
import os

def create_transparency_demo():
    """创建透明效果演示"""
    root = tk.Tk()
    root.title("透明效果演示 - 从普通到毛玻璃")
    root.geometry("1200x800")
    root.configure(bg='#3498db')
    
    # 创建渐变背景
    canvas = tk.Canvas(root, bg='#3498db', highlightthickness=0)
    canvas.pack(fill=tk.BOTH, expand=True)
    
    def draw_gradient():
        width = canvas.winfo_width()
        height = canvas.winfo_height()
        if width <= 1 or height <= 1:
            root.after(100, draw_gradient)
            return
            
        # 绘制渐变
        steps = 100
        for i in range(steps):
            ratio = i / steps
            r = int(52 + (184 - 52) * ratio)
            g = int(152 + (212 - 152) * ratio)
            b = int(219 + (240 - 219) * ratio)
            color = f"#{r:02x}{g:02x}{b:02x}"
            
            y1 = int(height * i / steps)
            y2 = int(height * (i + 1) / steps)
            canvas.create_rectangle(0, y1, width, y2, fill=color, outline=color)
    
    root.after(100, draw_gradient)
    
    # 标题
    canvas.create_text(600, 50, text="透明效果演示", 
                      font=('Microsoft YaHei', 20, 'bold'), 
                      fill='white')
    
    # 演示区域1：普通白色背景
    demo1_frame = tk.Frame(canvas, bg='#ffffff', relief='solid', bd=2)
    canvas.create_window(150, 150, window=demo1_frame, width=200, height=150, anchor='nw')
    tk.Label(demo1_frame, text="普通白色背景", 
             font=('Microsoft YaHei', 12, 'bold'), 
             bg='#ffffff', fg='#333333').pack(pady=20)
    tk.Label(demo1_frame, text="完全不透明\n遮挡背景", 
             font=('Microsoft YaHei', 10), 
             bg='#ffffff', fg='#666666').pack()
    
    # 演示区域2：半透明效果
    demo2_frame = tk.Frame(canvas, bg='#f8f9fa', relief='solid', bd=1)
    canvas.create_window(400, 150, window=demo2_frame, width=200, height=150, anchor='nw')
    tk.Label(demo2_frame, text="半透明效果", 
             font=('Microsoft YaHei', 12, 'bold'), 
             bg='#f8f9fa', fg='#333333').pack(pady=20)
    tk.Label(demo2_frame, text="浅色背景\n部分透明感", 
             font=('Microsoft YaHei', 10), 
             bg='#f8f9fa', fg='#666666').pack()
    
    # 演示区域3：stipple点状透明
    canvas.create_rectangle(650, 150, 850, 300, 
                           fill="#ffffff", outline="#333333", width=2,
                           stipple="gray25")
    canvas.create_text(750, 190, text="点状透明效果", 
                      font=('Microsoft YaHei', 12, 'bold'), 
                      fill='#333333')
    canvas.create_text(750, 250, text="使用stipple属性\n创建透明纹理", 
                      font=('Microsoft YaHei', 10), 
                      fill='#333333')
    
    # 演示区域4：毛玻璃效果
    # 阴影层
    canvas.create_rectangle(904, 154, 1154, 304, 
                           fill="#2c3e50", outline="",
                           stipple="gray12")
    # 主体层
    canvas.create_rectangle(900, 150, 1150, 300, 
                           fill="#ffffff", outline="#e8f4fd", width=2,
                           stipple="gray25")
    # 高光
    canvas.create_line(901, 151, 1149, 151, fill="#ffffff", width=1, stipple="gray50")
    canvas.create_line(901, 151, 901, 299, fill="#ffffff", width=1, stipple="gray50")
    
    canvas.create_text(1025, 190, text="毛玻璃效果", 
                      font=('Microsoft YaHei', 12, 'bold'), 
                      fill='#333333')
    canvas.create_text(1025, 250, text="多层叠加\n阴影+纹理+高光", 
                      font=('Microsoft YaHei', 10), 
                      fill='#333333')
    
    # 设备端口演示
    canvas.create_text(600, 380, text="设备端口配置透明效果演示", 
                      font=('Microsoft YaHei', 16, 'bold'), 
                      fill='white')
    
    # 创建设备卡片演示
    def create_device_demo(x, y, title, color):
        # 阴影
        canvas.create_rectangle(x+3, y+3, x+243, y+83, 
                               fill="#2c3e50", outline="", 
                               stipple="gray12")
        # 主体
        canvas.create_rectangle(x, y, x+240, y+80, 
                               fill="#f8f9fa", outline="#dddddd", width=1)
        # 头部
        canvas.create_rectangle(x, y, x+240, y+25, 
                               fill=color, outline="")
        # 文字
        canvas.create_text(x+15, y+12, text=title, 
                          font=('Microsoft YaHei', 9, 'bold'), 
                          fill='white', anchor='w')
        canvas.create_text(x+15, y+45, text="TCPIP::192.168.1.10X::INSTR", 
                          font=('Consolas', 8), 
                          fill='#333333', anchor='w')
        canvas.create_text(x+15, y+60, text="● 未连接", 
                          font=('Microsoft YaHei', 8), 
                          fill='#e74c3c', anchor='w')
    
    create_device_demo(200, 450, "示波器", "#e74c3c")
    create_device_demo(500, 450, "AC Source", "#3498db")
    create_device_demo(200, 570, "电子负载", "#2ecc71")
    create_device_demo(500, 570, "控制盒", "#f39c12")
    
    # 说明文字
    canvas.create_text(600, 700, text="透明效果让界面更有层次感，背景渐变可以透过来", 
                      font=('Microsoft YaHei', 12), 
                      fill='white')
    
    root.mainloop()

if __name__ == "__main__":
    create_transparency_demo()
