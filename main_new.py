"""
电源测试设备集成控制系统 - 主程序入口
重构后的模块化版本
"""
import tkinter as tk
from tkinter import messagebox

# 版本信息配置 - 放在main_new.py中，作为系统入口文件的配置
VERSION = "V1.0"
BUILD_DATE = "20250805_112233"
VERSION_STRING = f"版本：{VERSION}({BUILD_DATE.replace('_', ' ')})"

def get_version_info():
    """获取版本信息"""
    return VERSION_STRING

def get_version():
    """获取版本号"""
    return VERSION

def get_build_date():
    """获取构建日期"""
    return BUILD_DATE

def main():
    """主程序入口"""
    # 在函数内部导入，避免循环导入
    from interface.main_interface import MainInterface
    from ConnectDatabase import ReadDataBase
    
    # 创建数据库连接对象
    db = ReadDataBase()
    
    # 查询系统启用状态
    enable_status = db.get_system_enable_status()
    
    if enable_status == '启用':
        # 系统已启用，打开界面
        print("系统已启用，正在启动界面...")
        root = tk.Tk()
        app = MainInterface(root)
        root.mainloop()
    else:
        # 系统未启用或查询失败，显示错误消息
        print(f"系统状态检查失败，状态: {enable_status}")
        
        # 创建临时窗口用于显示消息框
        temp_root = tk.Tk()
        temp_root.withdraw()  # 隐藏主窗口
        
        # 显示错误消息
        messagebox.showerror(
            "系统启动失败", 
            f"当前版本已禁用或者电脑未联网\n\n{VERSION_STRING}\n\n请联系系统管理员或检查网络连接。"
        )
        
        temp_root.destroy()
        print("程序已退出")


if __name__ == "__main__":
    main()
