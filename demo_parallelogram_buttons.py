"""
圆角平行四边形按钮演示
展示新的标签按钮样式
"""
import tkinter as tk
import sys
import os

# 添加项目路径
sys.path.append('.')

from interface.rounded_parallelogram_button import RoundedParallelogramButton

def demo_parallelogram_buttons():
    """演示圆角平行四边形按钮"""
    root = tk.Tk()
    root.title("圆角平行四边形按钮演示")
    root.geometry("800x600")
    root.configure(bg='#f5f5f5')
    
    # 标题
    title_label = tk.Label(root, 
                          text="🔷 圆角平行四边形按钮演示",
                          font=('Microsoft YaHei', 16, 'bold'),
                          bg='#f5f5f5',
                          fg='#2c5aa0')
    title_label.pack(pady=20)
    
    # 说明文字
    info_label = tk.Label(root, 
                         text="现代化的标签按钮样式 - 具有倾斜效果和圆角设计",
                         font=('Microsoft YaHei', 12),
                         bg='#f5f5f5',
                         fg='#666666')
    info_label.pack(pady=10)
    
    # 按钮容器
    button_frame = tk.Frame(root, bg='#f5f5f5')
    button_frame.pack(pady=30)
    
    # 创建多个演示按钮
    button_texts = ["首页", "监控", "告警", "查询", "我的"]
    buttons = []
    
    for i, text in enumerate(button_texts):
        # 按钮容器（用于阴影效果）
        container = tk.Frame(button_frame, bg='#f5f5f5')
        container.pack(side=tk.LEFT, padx=10)
        
        # 阴影按钮
        shadow = RoundedParallelogramButton(
            container,
            text="",
            width=100,
            height=40,
            skew=12,
            corner_radius=6,
            bg_color='#d0d0d0',
            fg_color='#d0d0d0'
        )
        shadow.place(x=3, y=3)
        
        # 主按钮
        button = RoundedParallelogramButton(
            container,
            text=text,
            width=100,
            height=40,
            skew=12,
            corner_radius=6,
            bg_color='#e8e8e8',
            fg_color='#666666',
            hover_bg='#f0f0f0',
            hover_fg='#333333',
            active_bg='#ffffff',
            active_fg='#2c5aa0',
            command=lambda idx=i: switch_demo_tab(idx)
        )
        button.place(x=0, y=0)
        buttons.append(button)
    
    # 状态显示
    status_label = tk.Label(root, 
                           text="悬停或点击按钮查看效果",
                           font=('Microsoft YaHei', 11),
                           bg='#f5f5f5',
                           fg='#888888')
    status_label.pack(pady=(50, 20))
    
    # 当前选中的按钮
    current_button = [0]
    
    def switch_demo_tab(index):
        """切换演示标签"""
        # 重置所有按钮
        for btn in buttons:
            btn.set_active(False)
        
        # 设置选中按钮
        buttons[index].set_active(True)
        current_button[0] = index
        
        status_label.config(text=f"当前选中: {button_texts[index]}")
    
    # 默认选中第一个
    switch_demo_tab(0)
    
    # 特性说明
    features_frame = tk.Frame(root, bg='#f5f5f5')
    features_frame.pack(pady=20)
    
    features_text = """✨ 按钮特性:
• 圆角平行四边形设计
• 3D阴影效果
• 悬停状态变化
• 选中状态突出显示
• 现代化视觉风格"""
    
    features_label = tk.Label(features_frame, 
                             text=features_text,
                             font=('Microsoft YaHei', 10),
                             bg='#f5f5f5',
                             fg='#555555',
                             justify=tk.LEFT)
    features_label.pack()
    
    print("🎨 圆角平行四边形按钮特性:")
    print("  ✓ 倾斜的平行四边形形状")
    print("  ✓ 圆角边缘处理") 
    print("  ✓ 3D阴影效果")
    print("  ✓ 悬停动画反馈")
    print("  ✓ 选中状态突出")
    print("  ✓ 现代化配色方案")
    
    root.mainloop()

if __name__ == "__main__":
    demo_parallelogram_buttons()
