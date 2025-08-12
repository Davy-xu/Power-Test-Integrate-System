"""
Power Test Integrate System - 主程序
优化版本，防止界面卡顿
"""
import tkinter as tk
from tkinter import ttk
import sys
import threading
import time
import os

# 使用tkintertools风格主界面
try:
    import simple_tkintertools_main as modern_main
    print("OK tkintertools风格主界面模块导入成功")  # 使用安全字符
except ImportError as e:
    print(f"ERROR 主界面模块导入失败: {e}")  # 使用安全字符
    sys.exit(1)

def main():
    """主函数 - 优化版本（防窗口状态变化卡顿）"""
    try:
        print("🚀 启动电源测试集成系统...")  # 保留这个，因为它在字符串内部
        
        # 创建超时机制
        def timeout_handler():
            """超时处理"""
            time.sleep(30)  # 30秒超时
            print("WARNING 程序启动超时，可能存在卡顿问题")  # 使用安全字符
        
        # 启动超时监控线程
        timeout_thread = threading.Thread(target=timeout_handler)
        timeout_thread.daemon = True
        timeout_thread.start()
          
        # 直接运行现代化主界面
        modern_main.main()
        
    except Exception as e:
        print(f"ERROR 程序启动失败: {e}")  # 使用安全字符
        import traceback
        traceback.print_exc()
        
        # 显示错误对话框
        try:
            root = tk.Tk()
            root.withdraw()
            from tkinter import messagebox
            messagebox.showerror("启动失败", f"程序启动失败：\n{str(e)}")
            root.destroy()
        except:
            pass

if __name__ == "__main__":
    main()
