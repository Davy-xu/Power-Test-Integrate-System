"""
完整的主程序演示
展示所有圆角平行四边形标签按钮
"""
import tkinter as tk
from interface.main_interface import MainInterface

def main():
    """主函数"""
    print("🚀 启动 Power Test Integrate System 完整演示...")
    print("📋 功能特性:")
    print("  • 现代化圆角平行四边形标签")
    print("  • 悬空按钮效果")  
    print("  • 3D阴影设计")
    print("  • 完整的界面集成")
    
    # 创建主窗口
    root = tk.Tk()
    root.title("Power Test Integrate System - 圆角平行四边形标签演示")
    root.geometry("1200x800")
    root.configure(bg='#f5f5f5')
    
    # 创建主界面
    app = MainInterface(root)
    
    print("✅ 界面初始化完成")
    print("🎨 圆角平行四边形标签按钮已激活")
    print("💡 现在应该能看到顶部的标签按钮了！")
    
    # 启动主循环
    root.mainloop()

if __name__ == "__main__":
    main()
