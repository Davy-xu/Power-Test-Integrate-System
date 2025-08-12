#!/usr/bin/env python3
"""
快速图标测试
"""
import sys
import os
import tkinter as tk

# 添加项目路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from simple_tkintertools_main import SimpleTkinterToolsInterface
    
    print("🧪 图标系统测试开始...")
    
    # 创建接口对象
    interface = SimpleTkinterToolsInterface()
    
    # 测试图标开启状态
    print(f"✅ 图标开启: {interface.use_icons}")
    
    # 获取带图标的标签名称
    tab_names_with_icons = interface.get_tab_names()
    print("📋 带图标标签:")
    for i, name in enumerate(tab_names_with_icons):
        print(f"  {i+1}. {name}")
    
    # 切换到无图标模式测试
    interface.use_icons = False
    tab_names_without_icons = interface.get_tab_names()
    print("\n📋 无图标标签:")
    for i, name in enumerate(tab_names_without_icons):
        print(f"  {i+1}. {name}")
    
    print("\n✅ 图标系统测试完成！")
    print("💡 如果上面显示的图标正常，那么主界面中的图标也应该正常显示")
    
except Exception as e:
    print(f"❌ 测试失败: {e}")
    import traceback
    traceback.print_exc()
