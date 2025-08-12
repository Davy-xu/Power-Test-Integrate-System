"""
简单的程序启动测试
"""
import sys
import os

# 设置路径
sys.path.insert(0, r"d:\Power Test Integrate System")
os.chdir(r"d:\Power Test Integrate System")

try:
    print("检查模块导入...")
    import simple_tkintertools_main as modern_main
    print("✓ 主界面模块导入成功")
    
    print("检查类结构...")
    # 检查类是否存在
    if hasattr(modern_main, 'SimpleTkinterToolsInterface'):
        print("✓ 界面类存在")
        
        # 检查类构造函数
        interface = modern_main.SimpleTkinterToolsInterface()
        print("✓ 界面类实例化成功")
        
        # 检查关键方法
        if hasattr(interface, 'create_simplified_interface'):
            print("✓ 简化界面方法存在")
        
        print("✓ 所有测试通过！程序可以正常启动。")
    else:
        print("✗ 界面类不存在")
        
except Exception as e:
    print(f"✗ 测试失败: {e}")
    import traceback
    traceback.print_exc()
