"""
增强版按钮测试
使用明显的颜色和边框
"""
import tkinter as tk
from interface.enhanced_parallelogram_button import EnhancedParallelogramButton

def enhanced_test():
    root = tk.Tk()
    root.title("增强版按钮测试")
    root.geometry("500x400")
    root.configure(bg='#f0f0f0')
    
    # 标题
    title = tk.Label(root, text="🔍 增强版圆角平行四边形按钮测试", 
                    font=('Microsoft YaHei', 16, 'bold'),
                    bg='#f0f0f0', fg='#333333')
    title.pack(pady=20)
    
    # 说明
    info = tk.Label(root, text="这些按钮有明显的边框和颜色，应该很容易看到", 
                   font=('Microsoft YaHei', 10),
                   bg='#f0f0f0', fg='#666666')
    info.pack(pady=10)
    
    # 按钮容器
    button_frame = tk.Frame(root, bg='#f0f0f0')
    button_frame.pack(pady=30)
    
    # 创建多个明显的按钮
    buttons_info = [
        ("主页", "#4a90e2", "white"),
        ("监控", "#5cb85c", "white"), 
        ("告警", "#f0ad4e", "white"),
        ("设置", "#d9534f", "white"),
        ("帮助", "#5bc0de", "white")
    ]
    
    for i, (text, bg_color, fg_color) in enumerate(buttons_info):
        container = tk.Frame(button_frame, bg='#f0f0f0')
        container.pack(side=tk.LEFT, padx=8)
        
        button = EnhancedParallelogramButton(
            container,
            text=text,
            width=100,
            height=45,
            bg_color=bg_color,
            fg_color=fg_color,
            command=lambda idx=i, t=text: print(f"点击了 {t} 按钮 (索引: {idx})")
        )
        button.pack()
    
    # 状态信息
    status = tk.Label(root, text="如果您看到了5个彩色按钮，说明组件工作正常！", 
                     font=('Microsoft YaHei', 12, 'bold'),
                     bg='#f0f0f0', fg='#007700')
    status.pack(pady=30)
    
    print("🚀 增强版按钮测试启动")
    print("📋 应该看到5个不同颜色的平行四边形按钮")
    print("🎯 每个按钮都有明显的边框和颜色")
    
    root.mainloop()

if __name__ == "__main__":
    enhanced_test()
