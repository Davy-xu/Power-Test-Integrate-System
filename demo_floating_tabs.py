"""
悬空标签演示
展示类似现代网站导航栏的悬空标签效果
"""
import tkinter as tk
import sys
import os

# 添加项目路径
sys.path.append('.')

from interface.floating_tabs import FloatingTabFrame

def demo_floating_tabs():
    """演示悬空标签效果"""
    root = tk.Tk()
    root.title("悬空标签演示 - 类似现代网站导航")
    root.geometry("1000x700")
    root.configure(bg='#f5f5f5')
    
    # 添加说明标签
    info_frame = tk.Frame(root, bg='#f5f5f5', height=50)
    info_frame.pack(fill=tk.X, pady=(10, 0))
    info_frame.pack_propagate(False)
    
    info_label = tk.Label(info_frame, 
                         text="✨ 悬空标签效果演示 - 具有阴影、悬停动画和现代化外观",
                         font=('Microsoft YaHei', 12, 'bold'),
                         bg='#f5f5f5',
                         fg='#2c5aa0')
    info_label.pack(expand=True)
    
    # 创建悬空标签框架
    floating_frame = FloatingTabFrame(root)
    
    # 创建演示内容页面
    for i, (tab_name, content_text) in enumerate([
        ("首页", "欢迎使用悬空标签界面！\n\n这个标签具有现代化的悬空效果，包括：\n• 阴影效果\n• 悬停动画\n• 平滑过渡\n• 现代化配色"),
        ("监控", "监控页面内容\n\n实时监控系统状态和设备运行情况"),
        ("告警", "告警页面内容\n\n系统告警信息和通知管理"),
        ("查询", "查询页面内容\n\n数据查询和报表生成功能"),
        ("我的", "个人中心页面\n\n用户设置和个人信息管理")
    ]):
        # 创建内容框架
        content_frame = tk.Frame(floating_frame.content_area, bg='#ffffff')
        
        # 添加内容
        title_label = tk.Label(content_frame, 
                              text=f"{tab_name}页面", 
                              font=('Microsoft YaHei', 18, 'bold'),
                              bg='#ffffff',
                              fg='#333333')
        title_label.pack(pady=30)
        
        content_label = tk.Label(content_frame, 
                                text=content_text, 
                                font=('Microsoft YaHei', 12),
                                bg='#ffffff',
                                fg='#666666',
                                justify=tk.LEFT)
        content_label.pack(pady=20)
        
        # 添加装饰性边框
        border_frame = tk.Frame(content_frame, bg='#e0e0e0', height=2)
        border_frame.pack(fill=tk.X, padx=50, pady=20)
        
        # 添加到悬空标签
        floating_frame.add_tab(tab_name, content_frame)
    
    # 添加底部说明
    bottom_info = tk.Label(root, 
                          text="💡 提示：点击标签切换页面，悬停查看动画效果",
                          font=('Microsoft YaHei', 10),
                          bg='#f5f5f5',
                          fg='#888888')
    bottom_info.pack(side=tk.BOTTOM, pady=10)
    
    print("🚀 悬空标签特性:")
    print("  ✓ 3D阴影效果")
    print("  ✓ 悬停上升动画")
    print("  ✓ 选中状态突出显示")
    print("  ✓ 现代化圆角设计")
    print("  ✓ 流畅的交互反馈")
    print("  ✓ 类似现代网站导航栏")
    
    root.mainloop()

if __name__ == "__main__":
    demo_floating_tabs()
