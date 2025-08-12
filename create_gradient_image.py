#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
使用tkinter生成PPM格式的渐变背景图片
"""

import tkinter as tk

def create_gradient_ppm():
    """创建PPM格式的渐变背景图片"""
    print("🎨 生成PPM格式渐变图片...")
    
    width = 800
    height = 600
    
    # PPM文件头
    ppm_data = f"P3\n{width} {height}\n255\n"
    
    # 生成像素数据
    for y in range(height):
        for x in range(width):
            # 计算渐变比例
            ratio = y / height
            
            # 使用平滑过渡
            smooth_ratio = ratio * ratio
            
            # 颜色计算：从浅蓝到深蓝
            start_r, start_g, start_b = 135, 206, 250  # 浅天空蓝
            end_r, end_g, end_b = 25, 42, 86   # 深海蓝
            
            r = int(start_r + (end_r - start_r) * smooth_ratio)
            g = int(start_g + (end_g - start_g) * smooth_ratio)
            b = int(start_b + (end_b - start_b) * smooth_ratio)
            
            # 确保颜色值在有效范围内
            r = max(0, min(255, r))
            g = max(0, min(255, g))
            b = max(0, min(255, b))
            
            ppm_data += f"{r} {g} {b} "
        
        ppm_data += "\n"
        
        # 显示进度
        if y % 100 == 0:
            print(f"   生成进度: {y}/{height} ({y/height*100:.1f}%)")
    
    # 保存PPM文件
    with open("d:/Power Test Integrate System/gradient_background.ppm", "w") as f:
        f.write(ppm_data)
    
    print("✅ PPM渐变图片已保存: gradient_background.ppm")
    
    # 转换为GIF格式（tkinter原生支持）
    print("🔄 转换为GIF格式...")
    create_gradient_gif()

def create_gradient_gif():
    """创建GIF格式的渐变背景"""
    # 创建临时窗口
    root = tk.Tk()
    root.withdraw()
    
    width = 800
    height = 600
    
    # 创建PhotoImage
    img = tk.PhotoImage(width=width, height=height)
    
    print("🎨 生成GIF格式渐变...")
    
    # 逐行设置像素
    for y in range(height):
        row_colors = []
        for x in range(width):
            # 计算渐变比例
            ratio = y / height
            smooth_ratio = ratio * ratio
            
            # 颜色计算
            start_r, start_g, start_b = 135, 206, 250
            end_r, end_g, end_b = 25, 42, 86
            
            r = int(start_r + (end_r - start_r) * smooth_ratio)
            g = int(start_g + (end_g - start_g) * smooth_ratio)
            b = int(start_b + (end_b - start_b) * smooth_ratio)
            
            # 确保颜色值在有效范围内
            r = max(0, min(255, r))
            g = max(0, min(255, g))
            b = max(0, min(255, b))
            
            color = f"#{r:02x}{g:02x}{b:02x}"
            row_colors.append(color)
        
        # 设置整行像素
        row_data = " ".join(row_colors)
        img.put(row_data, (0, y))
        
        # 显示进度
        if y % 100 == 0:
            print(f"   生成进度: {y}/{height} ({y/height*100:.1f}%)")
    
    # 保存GIF文件
    img.write("d:/Power Test Integrate System/gradient_background.gif")
    print("✅ GIF渐变图片已保存: gradient_background.gif")
    
    root.destroy()

if __name__ == "__main__":
    try:
        create_gradient_ppm()
        print("\n🎉 渐变图片生成完成！")
        print("📁 生成的文件:")
        print("   • gradient_background.ppm - PPM格式")
        print("   • gradient_background.gif - GIF格式（推荐使用）")
        
    except Exception as e:
        print(f"❌ 生成图片时出错: {e}")
        import traceback
        traceback.print_exc()
