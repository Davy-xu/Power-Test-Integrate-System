#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
使用PIL生成高质量渐变背景图片
"""

def create_gradient_with_pil():
    """使用PIL创建高质量渐变背景"""
    try:
        from PIL import Image, ImageDraw
        print("🎨 使用PIL生成渐变背景...")
    except ImportError:
        print("❌ PIL库未安装，尝试安装...")
        import subprocess
        subprocess.check_call(["pip", "install", "Pillow"])
        from PIL import Image, ImageDraw
        print("✅ PIL库安装完成")
    
    # 创建标准尺寸背景
    width, height = 1200, 800
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)
    
    print(f"🖼️ 生成尺寸: {width}x{height}")
    
    for y in range(height):
        # 计算渐变比例
        ratio = y / height
        smooth_ratio = ratio ** 1.5  # 平滑过渡
        
        # 三段式渐变
        if ratio < 0.3:
            # 顶部：浅蓝
            local_ratio = ratio / 0.3
            start_r, start_g, start_b = 180, 230, 255
            end_r, end_g, end_b = 120, 190, 240
        elif ratio < 0.7:
            # 中部：中蓝
            local_ratio = (ratio - 0.3) / 0.4
            start_r, start_g, start_b = 120, 190, 240
            end_r, end_g, end_b = 80, 140, 220
        else:
            # 底部：深蓝
            local_ratio = (ratio - 0.7) / 0.3
            start_r, start_g, start_b = 80, 140, 220
            end_r, end_g, end_b = 40, 80, 120
        
        # 计算颜色
        r = int(start_r + (end_r - start_r) * local_ratio)
        g = int(start_g + (end_g - start_g) * local_ratio)
        b = int(start_b + (end_b - start_b) * local_ratio)
        
        # 绘制水平线
        color = (r, g, b)
        draw.line([(0, y), (width, y)], fill=color)
        
        if y % 100 == 0:
            print(f"   生成进度: {y}/{height} ({y/height*100:.1f}%)")
    
    # 保存PNG格式
    img.save("d:/Power Test Integrate System/gradient_background.png")
    print("✅ PNG渐变图片已保存: gradient_background.png")
    
    return True

def create_simple_gradient():
    """创建简化版渐变背景（使用tkinter，减少颜色数）"""
    import tkinter as tk
    
    print("🎨 生成简化渐变背景...")
    
    width = 800
    height = 600
    
    root = tk.Tk()
    root.withdraw()
    
    img = tk.PhotoImage(width=width, height=height)
    
    print(f"🖼️ 生成尺寸: {width}x{height}")
    
    # 使用较少的颜色级别
    color_steps = 64  # 减少颜色数量
    
    for y in range(height):
        # 计算颜色步级
        ratio = y / height
        step = int(ratio * (color_steps - 1))
        smooth_ratio = step / (color_steps - 1)
        
        # 颜色计算
        start_r, start_g, start_b = 150, 200, 255  # 浅蓝
        end_r, end_g, end_b = 30, 60, 120    # 深蓝
        
        r = int(start_r + (end_r - start_r) * smooth_ratio)
        g = int(start_g + (end_g - start_g) * smooth_ratio)
        b = int(start_b + (end_b - start_b) * smooth_ratio)
        
        color = f"#{r:02x}{g:02x}{b:02x}"
        
        # 绘制水平线
        img.put(color, (0, y, width, y+1))
        
        if y % 100 == 0:
            print(f"   生成进度: {y}/{height} ({y/height*100:.1f}%)")
    
    img.write("d:/Power Test Integrate System/gradient_simple.gif")
    print("✅ 简化渐变图片已保存: gradient_simple.gif")
    
    root.destroy()
    return True

if __name__ == "__main__":
    try:
        # 尝试使用PIL生成高质量PNG
        success = create_gradient_with_pil()
        
        if success:
            print("✅ PNG背景生成成功！")
        
        # 生成简化版GIF作为备用
        create_simple_gradient()
        
        print("\n🎉 渐变图片生成完成！")
        print("📁 生成的文件:")
        print("   • gradient_background.png - 高质量PNG背景")
        print("   • gradient_simple.gif - 简化版GIF背景")
        
    except Exception as e:
        print(f"❌ 生成图片时出错: {e}")
        import traceback
        traceback.print_exc()
