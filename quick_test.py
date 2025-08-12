#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
快速验证界面的脚本
"""

import sys
import traceback

try:
    print("� 导入模块...")
    import tkinter as tk
    from simple_tkintertools_main import SimpleTkinterToolsInterface
    print("✅ 模块导入成功")
    
    print("🏗️ 创建界面...")
    root = tk.Tk()
    app = SimpleTkinterToolsInterface(root)
    print("✅ 界面创建成功")
    
    # 检查按钮
    if hasattr(app, 'tab_buttons'):
        print(f"📊 发现 {len(app.tab_buttons)} 个按钮")
        for i, btn in enumerate(app.tab_buttons):
            print(f"  - 按钮 {i+1}: '{btn.cget('text')}'")
    else:
        print("❌ 未找到tab_buttons属性")
    
    print("🎉 测试完成，显示窗口...")
    root.mainloop()

except Exception as e:
    print(f"❌ 错误: {e}")
    traceback.print_exc()
