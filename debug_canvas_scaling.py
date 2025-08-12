#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
调试图片缩放问题的测试程序
"""

import tkinter as tk
import os
import time

def debug_canvas_scaling():
    """调试Canvas中的图片缩放"""
    root = tk.Tk()
    root.title("🔍 Canvas缩放调试")
    root.geometry("800x600")
    
    # 创建Canvas
    canvas = tk.Canvas(root, highlightthickness=0, bg='lightgray')
    canvas.pack(fill=tk.BOTH, expand=True)
    
    # 添加一些界面元素（模拟主界面）
    label1 = tk.Label(canvas, text="标题文字", bg='blue', fg='white')
    canvas.create_window(400, 50, window=label1)
    
    label2 = tk.Label(canvas, text="侧边栏", bg='green', fg='white')
    canvas.create_window(100, 200, window=label2)
    
    # 状态显示
    status_var = tk.StringVar()
    status_label = tk.Label(root, textvariable=status_var, bg='yellow')
    status_label.pack(side=tk.BOTTOM, fill=tk.X)
    
    bg_image = None
    original_path = None
    
    # 寻找背景图片
    image_files = ["gradient_background.png", "gradient_simple.gif"]
    for image_file in image_files:
        if os.path.exists(image_file):
            original_path = image_file
            break
    
    def draw_background():
        """绘制背景"""
        nonlocal bg_image
        
        print("=" * 50)
        print("🔍 开始调试背景绘制...")
        
        # 强制更新
        root.update_idletasks()
        time.sleep(0.1)  # 确保更新完成
        
        # 获取Canvas尺寸
        canvas_width = canvas.winfo_width()
        canvas_height = canvas.winfo_height()
        root_width = root.winfo_width()
        root_height = root.winfo_height()
        
        print(f"📊 Canvas尺寸: {canvas_width}x{canvas_height}")
        print(f"📊 窗口尺寸: {root_width}x{root_height}")
        
        status_var.set(f"Canvas: {canvas_width}x{canvas_height} | 窗口: {root_width}x{root_height}")
        
        if canvas_width <= 1 or canvas_height <= 1:
            print("⚠️ Canvas尺寸无效，使用默认尺寸")
            canvas_width, canvas_height = 800, 600
        
        # 清除旧背景
        canvas.delete("background")
        
        if original_path and original_path.endswith('.png'):
            try:
                from PIL import Image, ImageTk
                print(f"🖼️ 加载PNG: {original_path}")
                
                # 加载原始图片
                pil_image = Image.open(original_path)
                original_size = pil_image.size
                print(f"📐 原始尺寸: {original_size[0]}x{original_size[1]}")
                
                # 缩放图片
                print(f"🔄 缩放到: {canvas_width}x{canvas_height}")
                scaled_image = pil_image.resize((canvas_width, canvas_height), Image.Resampling.LANCZOS)
                bg_image = ImageTk.PhotoImage(scaled_image)
                
                # 显示背景
                canvas.create_image(canvas_width//2, canvas_height//2, 
                                  image=bg_image, anchor='center', tags="background")
                
                print("✅ PNG背景绘制成功")
                
            except Exception as e:
                print(f"❌ PNG处理失败: {e}")
                
        elif original_path and original_path.endswith('.gif'):
            try:
                print(f"🖼️ 加载GIF: {original_path}")
                bg_image = tk.PhotoImage(file=original_path)
                
                canvas.create_image(canvas_width//2, canvas_height//2, 
                                  image=bg_image, anchor='center', tags="background")
                print("✅ GIF背景绘制成功")
                
            except Exception as e:
                print(f"❌ GIF处理失败: {e}")
        else:
            print("⚠️ 未找到背景图片")
    
    def on_resize(event):
        """窗口缩放事件"""
        if event.widget == root:
            print(f"\n🔄 窗口缩放: {event.width}x{event.height}")
            # 延迟重绘
            root.after(100, draw_background)
    
    # 绑定事件
    root.bind('<Configure>', on_resize)
    
    # 初始绘制（延迟执行）
    root.after(200, draw_background)
    
    # 添加手动重绘按钮
    def manual_redraw():
        print("\n🔄 手动重绘背景")
        draw_background()
    
    button = tk.Button(root, text="手动重绘", command=manual_redraw)
    button.pack(side=tk.TOP)
    
    print("🚀 调试程序启动，请调整窗口大小观察输出")
    root.mainloop()

if __name__ == "__main__":
    debug_canvas_scaling()
