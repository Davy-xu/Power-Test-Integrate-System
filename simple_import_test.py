#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""简单测试主界面能否加载设备端口"""

import os
import sys

print("🔍 检查文件结构...")

# 检查关键文件是否存在
files_to_check = [
    "simple_tkintertools_main.py",
    "interface/tabs/device_port.py", 
    "interface/rounded_rect_button.py"
]

for file_path in files_to_check:
    if os.path.exists(file_path):
        print(f"✅ {file_path} 存在")
    else:
        print(f"❌ {file_path} 不存在")

print("\n🧪 尝试导入测试...")

try:
    # 添加路径
    sys.path.insert(0, os.path.join(os.getcwd(), 'interface', 'tabs'))
    sys.path.insert(0, os.path.join(os.getcwd(), 'interface'))
    
    # 测试导入
    import device_port
    print("✅ device_port 模块导入成功")
    
    from device_port import DevicePortTab
    print("✅ DevicePortTab 类导入成功")
    
    print("\n🎉 所有导入测试通过！设备端口集成应该可以正常工作。")
    
except Exception as e:
    print(f"❌ 导入测试失败: {e}")
    import traceback
    traceback.print_exc()

print("\n📌 现在可以运行主程序测试设备端口功能了：")
print("   python app.py")
print("   然后点击左侧的'设备端口'按钮")
