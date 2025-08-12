"""
优化后的启动脚本 - 防止界面卡顿
"""
import tkinter as tk
import sys
import os
import threading
import time

# 添加当前目录到Python路径
sys.path.insert(0, os.path.dirname(__file__))

def create_optimized_ui():
    """创建优化的界面，防止卡顿"""
    try:
        print("🚀 启动优化版界面...")
        
        # 创建主窗口
        root = tk.Tk()
        root.title("电源测试集成系统 v2.0 - 优化版")
        root.geometry("1400x900")
        root.configure(bg='#6699CC')
        
        # 先显示简单的启动画面
        startup_label = tk.Label(root, 
                                text="电源测试集成系统\n正在初始化...", 
                                font=('Microsoft YaHei', 20, 'bold'),
                                bg='#6699CC', fg='white')
        startup_label.pack(expand=True)
        
        # 更新界面
        root.update()
        
        def load_main_interface():
            """在后台加载主界面"""
            try:
                # 移除启动画面
                startup_label.destroy()
                
                from simple_tkintertools_main import SimpleTkinterToolsInterface
                
                # 创建界面
                interface = SimpleTkinterToolsInterface()
                interface.root = root
                
                # 创建主画布（延迟创建）
                interface.bg_canvas = tk.Canvas(root, bg='#6699CC', highlightthickness=0)
                interface.bg_canvas.pack(fill=tk.BOTH, expand=True)
                
                # 绑定窗口大小变化事件（优化版）
                def on_window_resize(event):
                    if event.widget == root:
                        # 延迟执行背景绘制，避免频繁重绘
                        root.after_idle(interface.draw_background)
                        
                root.bind('<Configure>', on_window_resize)
                
                # 分步创建界面
                interface.create_interface()
                
                print("✅ 优化版界面启动成功！")
                print("🎯 优化特性：")
                print("   - 分步骤加载界面组件")
                print("   - 减少渐变绘制复杂度")
                print("   - 异步设备检测")
                print("   - 防卡顿机制")
                
            except Exception as e:
                print(f"❌ 主界面加载失败: {e}")
                import traceback
                traceback.print_exc()
                
                # 显示错误信息
                error_label = tk.Label(root, 
                                      text=f"界面加载失败\n{str(e)}", 
                                      font=('Microsoft YaHei', 12),
                                      bg='#6699CC', fg='#ff6b6b')
                error_label.pack(expand=True)
        
        # 延迟1秒后开始加载主界面
        root.after(1000, load_main_interface)
        
        # 启动主循环
        root.mainloop()
        
    except Exception as e:
        print(f"❌ 界面启动失败: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    create_optimized_ui()
