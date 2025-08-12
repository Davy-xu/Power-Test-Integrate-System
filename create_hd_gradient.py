#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成高质量的渐变背景图片
"""

import tkinter as tk

def create_hd_gradient():
    """创建高清渐变背景"""
    print("🎨 生成高清渐变背景...")
    
    # 高清尺寸
    width = 1920
    height = 1080
    
    # 创建临时窗口
    root = tk.Tk()
    root.withdraw()
    
    # 创建PhotoImage
    img = tk.PhotoImage(width=width, height=height)
    
    print(f"🖼️ 生成尺寸: {width}x{height}")
    
    # 分块处理以提高性能
    chunk_size = 50
    total_chunks = height // chunk_size + (1 if height % chunk_size else 0)
    
    for chunk in range(total_chunks):
        start_y = chunk * chunk_size
        end_y = min((chunk + 1) * chunk_size, height)
        
        chunk_data = []
        for y in range(start_y, end_y):
            row_colors = []
            for x in range(width):
                # 计算渐变比例
                ratio = y / height
                
                # 使用三段式渐变
                if ratio < 0.3:
                    # 顶部：浅天空蓝到中蓝
                    local_ratio = ratio / 0.3
                    smooth_ratio = local_ratio * local_ratio * 0.5
                    start_r, start_g, start_b = 160, 220, 255  # 更亮的天空蓝
                    end_r, end_g, end_b = 100, 180, 240
                elif ratio < 0.7:
                    # 中部：中蓝到深蓝
                    local_ratio = (ratio - 0.3) / 0.4
                    smooth_ratio = local_ratio * local_ratio
                    start_r, start_g, start_b = 100, 180, 240
                    end_r, end_g, end_b = 60, 120, 200
                else:
                    # 底部：深蓝到深海蓝
                    local_ratio = (ratio - 0.7) / 0.3
                    smooth_ratio = local_ratio * local_ratio * 1.5
                    start_r, start_g, start_b = 60, 120, 200
                    end_r, end_g, end_b = 20, 40, 80
                
                r = int(start_r + (end_r - start_r) * smooth_ratio)
                g = int(start_g + (end_g - start_g) * smooth_ratio)
                b = int(start_b + (end_b - start_b) * smooth_ratio)
                
                # 添加轻微的水平变化（光效）
                light_factor = 1.0 + 0.05 * (1 - abs(x - width/2) / (width/2))
                r = int(r * light_factor)
                g = int(g * light_factor)
                b = int(b * light_factor)
                
                # 确保颜色值在有效范围内
                r = max(0, min(255, r))
                g = max(0, min(255, g))
                b = max(0, min(255, b))
                
                color = f"#{r:02x}{g:02x}{b:02x}"
                row_colors.append(color)
            
            # 添加整行数据
            row_data = " ".join(row_colors)
            chunk_data.append(row_data)
        
        # 批量设置像素
        for i, row_data in enumerate(chunk_data):
            img.put(row_data, (0, start_y + i))
        
        # 显示进度
        progress = (chunk + 1) / total_chunks * 100
        print(f"   生成进度: {chunk + 1}/{total_chunks} ({progress:.1f}%)")
    
    # 保存高清背景
    img.write("d:/Power Test Integrate System/gradient_hd.gif")
    print("✅ 高清渐变图片已保存: gradient_hd.gif")
    
    root.destroy()

def create_standard_gradient():
    """创建标准尺寸渐变背景"""
    print("🎨 生成标准渐变背景...")
    
    width = 1200
    height = 800
    
    root = tk.Tk()
    root.withdraw()
    
    img = tk.PhotoImage(width=width, height=height)
    
    print(f"🖼️ 生成尺寸: {width}x{height}")
    
    for y in range(height):
        row_colors = []
        for x in range(width):
            # 计算渐变比例
            ratio = y / height
            smooth_ratio = ratio * ratio * 0.8  # 较柔和的过渡
            
            # 颜色计算
            start_r, start_g, start_b = 140, 210, 255  # 清爽天空蓝
            end_r, end_g, end_b = 30, 50, 90    # 深海蓝
            
            r = int(start_r + (end_r - start_r) * smooth_ratio)
            g = int(start_g + (end_g - start_g) * smooth_ratio)
            b = int(start_b + (end_b - start_b) * smooth_ratio)
            
            # 确保颜色值在有效范围内
            r = max(0, min(255, r))
            g = max(0, min(255, g))
            b = max(0, min(255, b))
            
            color = f"#{r:02x}{g:02x}{b:02x}"
            row_colors.append(color)
        
        row_data = " ".join(row_colors)
        img.put(row_data, (0, y))
        
        if y % 100 == 0:
            print(f"   生成进度: {y}/{height} ({y/height*100:.1f}%)")
    
    img.write("d:/Power Test Integrate System/gradient_standard.gif")
    print("✅ 标准渐变图片已保存: gradient_standard.gif")
    
    root.destroy()

if __name__ == "__main__":
    try:
        # 生成标准尺寸背景
        create_standard_gradient()
        
        # 生成高清背景
        create_hd_gradient()
        
        print("\n🎉 所有渐变图片生成完成！")
        print("📁 生成的文件:")
        print("   • gradient_standard.gif - 1200x800 标准背景")
        print("   • gradient_hd.gif - 1920x1080 高清背景")
        print("   • gradient_background.gif - 800x600 原始背景")
        
    except Exception as e:
        print(f"❌ 生成图片时出错: {e}")
        import traceback
        traceback.print_exc()
