#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
使用tkinter创建渐变背景图片
"""

import tkinter as tk
from tkinter import Canvas
import os

def create_gradient_with_tkinter():
    """使用tkinter创建渐变图片"""
    print("🎨 使用tkinter创建渐变背景...")
    
    # 创建临时窗口
    root = tk.Tk()
    root.withdraw()  # 隐藏窗口
    
    # 设置图片尺寸
    width = 1920
    height = 1080
    
    # 创建Canvas
    canvas = Canvas(root, width=width, height=height, highlightthickness=0)
    
    # 绘制渐变
    steps = 200  # 渐变步数
    for i in range(steps):
        # 计算渐变比例
        ratio = i / steps
        y_start = int(i * height / steps)
        y_end = int((i + 1) * height / steps)
        
        # 颜色计算：从浅蓝到深蓝
        start_r, start_g, start_b = 135, 206, 250  # 浅天空蓝
        end_r, end_g, end_b = 25, 42, 86   # 深海蓝
        
        # 使用平滑过渡
        smooth_ratio = ratio * ratio
        
        r = int(start_r + (end_r - start_r) * smooth_ratio)
        g = int(start_g + (end_g - start_g) * smooth_ratio)
        b = int(start_b + (end_b - start_b) * smooth_ratio)
        
        # 确保颜色值在有效范围内
        r = max(0, min(255, r))
        g = max(0, min(255, g))
        b = max(0, min(255, b))
        
        color = f"#{r:02x}{g:02x}{b:02x}"
        
        # 绘制矩形
        canvas.create_rectangle(
            0, y_start, width, y_end,
            fill=color, outline=color
        )
    
    # 更新Canvas
    canvas.update()
    
    try:
        # 尝试保存为PostScript，然后转换
        canvas.postscript(file="d:/Power Test Integrate System/gradient.eps")
        print("✅ 已生成PostScript文件: gradient.eps")
        
        # 创建一个简化的图片文件（使用PhotoImage）
        # 这里我们直接返回Canvas，在程序中使用
        
    except Exception as e:
        print(f"❌ 保存图片时出错: {e}")
    
    root.destroy()
    print("✅ 渐变创建完成")

if __name__ == "__main__":
    create_gradient_with_tkinter()
