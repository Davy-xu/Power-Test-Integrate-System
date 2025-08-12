#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成蓝色渐变背景图片
"""

from PIL import Image, ImageDraw
import numpy as np

def create_gradient_image():
    """创建蓝色渐变背景图片"""
    # 图片尺寸
    width = 1920
    height = 1080
    
    print(f"🎨 生成渐变图片: {width}x{height}")
    
    # 创建图片
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)
    
    # 定义渐变颜色 - 从浅天空蓝到深海蓝
    start_color = (135, 206, 250)  # 浅天空蓝
    end_color = (25, 42, 86)       # 深海蓝
    
    # 创建垂直渐变
    for y in range(height):
        # 计算渐变比例
        ratio = y / height
        
        # 使用平滑的过渡曲线（二次函数）
        smooth_ratio = ratio * ratio
        
        # 计算当前行的颜色
        r = int(start_color[0] + (end_color[0] - start_color[0]) * smooth_ratio)
        g = int(start_color[1] + (end_color[1] - start_color[1]) * smooth_ratio)
        b = int(start_color[2] + (end_color[2] - start_color[2]) * smooth_ratio)
        
        # 确保颜色值在有效范围内
        r = max(0, min(255, r))
        g = max(0, min(255, g))
        b = max(0, min(255, b))
        
        # 绘制水平线
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    
    # 保存图片
    img.save('d:/Power Test Integrate System/gradient_background.png')
    print("✅ 渐变图片已保存: gradient_background.png")
    
    # 创建一个较小的版本用于预览
    preview_img = img.resize((400, 300))
    preview_img.save('d:/Power Test Integrate System/gradient_preview.png')
    print("✅ 预览图片已保存: gradient_preview.png")
    
    return img

def create_enhanced_gradient():
    """创建增强版渐变图片（带光效）"""
    width = 1920
    height = 1080
    
    print(f"🌟 生成增强版渐变图片: {width}x{height}")
    
    # 创建numpy数组用于更精细的控制
    img_array = np.zeros((height, width, 3), dtype=np.uint8)
    
    # 定义渐变颜色
    start_color = np.array([135, 206, 250])  # 浅天空蓝
    mid_color = np.array([70, 130, 200])     # 中蓝色
    end_color = np.array([25, 42, 86])       # 深海蓝
    
    for y in range(height):
        ratio = y / height
        
        # 使用分段渐变
        if ratio < 0.5:
            # 上半部分：从浅蓝到中蓝
            local_ratio = ratio * 2
            smooth_ratio = local_ratio * local_ratio
            color = start_color + (mid_color - start_color) * smooth_ratio
        else:
            # 下半部分：从中蓝到深蓝
            local_ratio = (ratio - 0.5) * 2
            smooth_ratio = local_ratio * local_ratio
            color = mid_color + (end_color - mid_color) * smooth_ratio
        
        # 添加轻微的光效
        light_intensity = np.sin(ratio * np.pi) * 0.1
        color = color + color * light_intensity
        
        # 确保颜色值在有效范围内
        color = np.clip(color, 0, 255)
        
        # 填充整行
        img_array[y, :] = color.astype(np.uint8)
    
    # 转换为PIL图片并保存
    enhanced_img = Image.fromarray(img_array)
    enhanced_img.save('d:/Power Test Integrate System/gradient_enhanced.png')
    print("✅ 增强版渐变图片已保存: gradient_enhanced.png")
    
    return enhanced_img

if __name__ == "__main__":
    try:
        # 生成基础渐变图片
        basic_img = create_gradient_image()
        
        # 生成增强版渐变图片
        enhanced_img = create_enhanced_gradient()
        
        print("\n🎉 图片生成完成！")
        print("📁 生成的文件:")
        print("   • gradient_background.png - 基础渐变背景")
        print("   • gradient_enhanced.png - 增强版渐变背景") 
        print("   • gradient_preview.png - 预览图片")
        
    except ImportError:
        print("❌ 需要安装PIL和numpy库")
        print("请运行: pip install Pillow numpy")
    except Exception as e:
        print(f"❌ 生成图片时出错: {e}")
        import traceback
        traceback.print_exc()
