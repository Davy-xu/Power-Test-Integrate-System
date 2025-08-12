"""
启动平衡版本的界面
"""

import subprocess
import sys
import os

def start_balanced_ui():
    """启动平衡版本的用户界面"""
    try:
        print("🚀 启动平衡布局界面...")
        print("📐 布局特性:")
        print("   ✓ 白色内容区域已放大")
        print("   ✓ 保持左侧按钮完整显示")
        print("   ✓ 响应式窗口调整")
        print("   ✓ 协调的整体布局")
        print()
        
        # 启动主程序
        result = subprocess.run([sys.executable, "main.py"], 
                              cwd=r"d:\Power Test Integrate System",
                              capture_output=False)
        
        if result.returncode == 0:
            print("✅ 程序正常退出")
        else:
            print(f"⚠️ 程序退出码: {result.returncode}")
            
    except Exception as e:
        print(f"❌ 启动失败: {e}")

if __name__ == "__main__":
    start_balanced_ui()
