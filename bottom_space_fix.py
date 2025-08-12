#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
底部空间一致性修复补丁
解决点击按钮后底部空间高度变化的问题
"""
import tkinter as tk
from datetime import datetime
import threading
import time

class BottomSpaceConsistencyPatch:
    """底部空间一致性修复补丁"""
    
    @staticmethod
    def apply_to_interface(interface_obj):
        """将修复补丁应用到界面对象"""
        print("🔧 应用底部空间一致性修复补丁...")
        
        # 备份原始方法
        original_switch_tab = interface_obj.switch_tab
        original_load_tab_content = interface_obj.load_tab_content
        original_on_window_resize = interface_obj.on_window_resize
        
        def fixed_switch_tab(tab_index):
            """修复版的标签切换，确保底部空间一致"""
            print(f"🔄 [修复版] 切换到标签 {tab_index}")
            
            # 调用原始切换逻辑
            original_switch_tab(tab_index)
            
            # 强制保持底部空间一致
            BottomSpaceConsistencyPatch.force_consistent_layout(interface_obj)
            
        def fixed_load_tab_content(tab_index):
            """修复版的内容加载，确保底部空间一致"""
            print(f"📄 [修复版] 加载标签内容 {tab_index}")
            
            # 调用原始加载逻辑
            original_load_tab_content(tab_index)
            
            # 延迟确保布局一致性
            interface_obj.root.after(100, lambda: BottomSpaceConsistencyPatch.force_consistent_layout(interface_obj))
            
        def fixed_on_window_resize(event=None):
            """修复版的窗口大小改变处理"""
            print("🖼️ [修复版] 窗口大小改变")
            
            # 调用原始处理逻辑
            original_on_window_resize(event)
            
            # 强制保持底部空间一致
            BottomSpaceConsistencyPatch.force_consistent_layout(interface_obj)
        
        # 替换方法
        interface_obj.switch_tab = fixed_switch_tab
        interface_obj.load_tab_content = fixed_load_tab_content  
        interface_obj.on_window_resize = fixed_on_window_resize
        
        print("✅ 底部空间一致性修复补丁应用完成")
        
    @staticmethod
    def force_consistent_layout(interface_obj):
        """强制保持布局一致性"""
        try:
            # 确保内容区域尺寸一致
            if hasattr(interface_obj, 'content_window') and interface_obj.content_window:
                interface_obj.root.update_idletasks()
                
                # 获取当前窗口尺寸
                win_w = interface_obj.bg_canvas.winfo_width() if interface_obj.bg_canvas else 1200
                win_h = interface_obj.bg_canvas.winfo_height() if interface_obj.bg_canvas else 800
                
                # 固定的布局参数
                SIDEBAR_WIDTH = 220
                PADDING = 20
                BOTTOM_SPACE = 180  # 固定底部空间
                
                # 计算内容区域尺寸
                content_width = max(200, win_w - SIDEBAR_WIDTH - PADDING)
                content_height = max(100, win_h - BOTTOM_SPACE - PADDING)
                
                # 应用尺寸
                interface_obj.bg_canvas.itemconfig(
                    interface_obj.content_window,
                    width=content_width,
                    height=content_height
                )
                
                print(f"🔧 强制布局一致: {content_width}x{content_height}, 底部间距: {BOTTOM_SPACE}px")
                
            # 确保状态栏位置正确
            if hasattr(interface_obj, 'create_status_bar'):
                interface_obj.create_status_bar()
                
        except Exception as e:
            print(f"❌ 强制布局一致性失败: {e}")

def apply_bottom_space_fix():
    """应用底部空间修复的主函数"""
    print("🚀 启动底部空间一致性修复...")
    
    # 导入主界面
    try:
        import simple_tkintertools_main as main_module
        
        # 修改主界面的main函数
        original_main = main_module.main
        
        def patched_main():
            """修复版的主函数"""
            print("🔧 启动修复版主界面...")
            
            # 调用原始主函数逻辑
            root = tk.Tk()
            root.title("简化的tkintertools风格主界面")
            root.geometry("1200x800")
            
            # 创建背景画布
            bg_canvas = tk.Canvas(root, bg="#CCCCCC", highlightthickness=0)
            bg_canvas.pack(fill='both', expand=True)
            
            # 创建主界面对象
            interface = main_module.SimpleTkinterToolsInterface()
            interface.root = root
            interface.bg_canvas = bg_canvas
            
            # 应用修复补丁
            BottomSpaceConsistencyPatch.apply_to_interface(interface)
            
            # 初始化界面
            interface.draw_background()
            interface.create_interface()
            
            # 强制初始布局一致性
            interface.root.after(500, lambda: BottomSpaceConsistencyPatch.force_consistent_layout(interface))
            
            # 启动主循环
            root.mainloop()
            
        # 替换主函数
        main_module.main = patched_main
        
        # 运行修复版主界面
        main_module.main()
        
    except Exception as e:
        print(f"❌ 修复版启动失败: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    apply_bottom_space_fix()
