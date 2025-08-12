#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
验证自定义功能控件是否正确显示
"""

import tkinter as tk
import sys
import os

def verify_custom_function_display():
    """验证自定义功能控件显示"""
    print("🔍 验证自定义功能控件显示...")
    
    # 导入并创建简单测试
    try:
        from simple_tkintertools_main import SimpleTkinterToolsInterface
        
        # 创建测试窗口
        root = tk.Tk()
        root.geometry("900x600")
        root.title("自定义功能控件验证")
        
        # 创建背景画布
        bg_canvas = tk.Canvas(root, bg="#e3f2fd", highlightthickness=0)
        bg_canvas.pack(fill='both', expand=True)
        
        # 创建主界面实例
        interface = SimpleTkinterToolsInterface()
        interface.root = root
        interface.bg_canvas = bg_canvas
        
        # 创建内容框架模拟主程序环境
        interface.content_frame = tk.Frame(bg_canvas, bg='#F8FBFF')
        interface.content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        print("✅ 测试环境创建成功")
        
        # 直接调用自定义功能内容创建方法
        print("🎨 正在创建自定义功能内容...")
        interface.create_custom_function_content()
        
        print("✅ 自定义功能内容创建完成")
        print("📋 现在应该能看到以下控件:")
        print("   - 测试项目区域（带输入框和按钮）")
        print("   - 子程序区域（带输入框和按钮）")
        print("   - 自定义功能列表")
        print("   - 各种操作按钮")
        
        # 检查内容框架中的widget数量
        widgets = interface.content_frame.winfo_children()
        print(f"📊 检测到 {len(widgets)} 个子控件")
        
        for i, widget in enumerate(widgets):
            widget_type = type(widget).__name__
            try:
                widget_text = widget.cget('text') if hasattr(widget, 'cget') else "无文本"
            except:
                widget_text = "无法获取文本"
            print(f"   控件 {i+1}: {widget_type} - {widget_text}")
        
        # 显示窗口
        root.mainloop()
        
    except Exception as e:
        print(f"❌ 验证失败: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    verify_custom_function_display()
