#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
快速验证自定义功能界面集成
"""

import tkinter as tk
import sys
import os

def quick_test():
    """快速测试自定义功能界面在主程序中的集成"""
    print("🔍 开始验证自定义功能界面集成...")
    
    # 导入主程序类
    try:
        from simple_tkintertools_main import SimpleTkinterToolsInterface
        print("✅ 主程序模块导入成功")
    except Exception as e:
        print(f"❌ 主程序模块导入失败: {e}")
        return
    
    # 创建应用实例（模拟主程序初始化）
    try:
        root = tk.Tk()
        root.geometry("800x600")
        
        # 创建背景画布
        bg_canvas = tk.Canvas(root, bg="#e3f2fd", highlightthickness=0)
        bg_canvas.pack(fill='both', expand=True)
        
        # 创建主界面实例
        interface = SimpleTkinterToolsInterface()
        interface.root = root
        interface.bg_canvas = bg_canvas
        
        # 创建内容框架来模拟主界面结构
        interface.content_frame = tk.Frame(bg_canvas, bg='#F8FBFF')
        interface.content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        print("✅ 应用实例创建成功")
    except Exception as e:
        print(f"❌ 应用实例创建失败: {e}")
        return
    
    # 测试自定义功能内容创建
    try:
        interface.create_custom_function_content()
        print("✅ 自定义功能内容创建成功")
        print("🎉 验证完成！自定义功能界面已成功集成到主程序中。")
        print("💡 请在主程序界面中点击'🎨自定义功能'标签页查看控件。")
        
        # 显示窗口进行验证
        print("📋 正在显示测试窗口，您应该能看到自定义功能的控件...")
        root.title("自定义功能界面集成验证")
        root.mainloop()
        
    except Exception as e:
        print(f"❌ 自定义功能内容创建失败: {e}")
        import traceback
        traceback.print_exc()
    finally:
        if 'root' in locals():
            try:
                root.destroy()
            except:
                pass

if __name__ == "__main__":
    quick_test()
