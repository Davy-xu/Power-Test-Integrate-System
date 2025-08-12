#!/usr/bin/env python3
"""
强制测试白色界面放大效果
"""
import sys
import os

# 添加路径
sys.path.insert(0, "d:\\Power Test Integrate System")

def force_test_enlarged():
    """强制测试白色界面放大效果"""
    print("🔧 强制白色界面放大测试")
    print("=" * 60)
    print("修改说明:")
    print("✅ 主函数现在强制调用 create_simplified_interface()")
    print("✅ 绕过了旧的分步骤创建流程")
    print("✅ 直接使用放大版本的内容区域")
    print("✅ 内容区域初始尺寸: 1000x600 (之前 800x500)")
    print("✅ 位置优化: (140,90) 而非 (180,120)")
    print("=" * 60)
    
    print("\n🎯 验证要点:")
    print("1. 启动时观察白色内容区域大小")
    print("2. 检查控制台输出信息")
    print("3. 左侧按钮区域应该更紧凑")
    print("4. 拖拽窗口边缘测试响应")
    
    print("\n🚀 启动强制修改版本...")
    print("- 如果还是不变大，可能是缓存或其他问题")
    print("- 请注意观察控制台输出的具体信息")
    print("=" * 60)
    
    try:
        # 导入并运行强制修改版本
        import simple_tkintertools_main as main_module
        
        print("✅ 强制修改版本导入成功")
        print("🎯 正在启动强制放大版界面...\n")
        
        # 直接运行
        main_module.main()
        
    except Exception as e:
        print(f"❌ 强制测试失败: {e}")
        import traceback
        traceback.print_exc()
        
        print("\n🔍 问题分析:")
        print("如果仍然不能放大，可能的原因:")
        print("1. 代码修改没有保存")
        print("2. Python模块缓存问题")
        print("3. 存在其他版本的函数被调用")
        print("4. tkinter版本或系统限制")

if __name__ == "__main__":
    force_test_enlarged()
