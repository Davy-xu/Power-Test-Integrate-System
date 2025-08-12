#!/usr/bin/env python3
"""
最简启动测试
"""
print("🚀 开始启动测试...")

try:
    print("1. 导入模块...")
    import simple_tkintertools_main
    
    print("2. 调用main函数...")
    simple_tkintertools_main.main()
    
except Exception as e:
    print(f"❌ 启动失败: {e}")
    import traceback
    traceback.print_exc()
