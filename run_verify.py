#!/usr/bin/env python3
"""
直接运行和验证白色界面放大效果
"""
import sys
import os

# 添加路径
sys.path.insert(0, "d:\\Power Test Integrate System")

def run_and_verify():
    """运行主程序并验证白色界面放大效果"""
    print("🔧 白色界面放大修复验证")
    print("=" * 60)
    print("修复内容:")
    print("✅ 统一了两个create_content_area函数的参数")
    print("✅ 左边距: 180 → 140 像素 (-40px)")
    print("✅ 上边距: 120 → 90 像素 (-30px)")
    print("✅ 最小宽度: 400 → 600 像素 (+200px)")
    print("✅ 最小高度: 300 → 400 像素 (+100px)")
    print("✅ 右边距: 180 → 160 像素 (-20px)")
    print("✅ 下边距: 150 → 120 像素 (-30px)")
    print("=" * 60)
    
    print("\n🧪 验证步骤:")
    print("1. 观察启动后的白色内容区域大小")
    print("2. 查看控制台输出是否显示'放大内容区域'")
    print("3. 拖拽窗口边缘测试响应性")
    print("4. 与之前的界面进行对比")
    print("5. 检查左侧按钮是否更紧凑")
    
    print("\n📊 预期效果:")
    print("• 白色内容区域应该明显占用更多屏幕空间")
    print("• 左侧按钮区域应该更紧凑")
    print("• 整体空间利用率应该提高约20-25%")
    
    print("\n🚀 启动程序进行验证...")
    print("=" * 60)
    
    try:
        # 导入并运行主程序
        import simple_tkintertools_main as main_module
        
        print("✅ 修复版主模块导入成功")
        print("🎯 正在启动修复版界面...\n")
        
        # 运行主程序
        main_module.main()
        
    except Exception as e:
        print(f"❌ 验证失败: {e}")
        import traceback
        traceback.print_exc()
        
        print("\n📝 故障排除建议:")
        print("1. 检查simple_tkintertools_main.py是否保存了最新修改")
        print("2. 确认Python能正确导入模块")
        print("3. 查看是否有语法错误")

if __name__ == "__main__":
    run_and_verify()
