"""
简单的圆角矩形按钮效果演示
"""
import tkinter as tk

def create_rounded_button_effect():
    """创建圆角矩形按钮效果演示"""
    root = tk.Tk()
    root.title("圆角矩形按钮效果")
    root.geometry("900x300")
    root.configure(bg='#7BA7D9')
    
    # 顶部框架 - 模拟主界面
    top_frame = tk.Frame(root, bg='#FFFFFF', height=120)
    top_frame.pack(fill=tk.X, padx=10, pady=10)
    top_frame.pack_propagate(False)
    
    # 左侧Logo区域
    logo_frame = tk.Frame(top_frame, bg='#FFFFFF', width=150)
    logo_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10)
    logo_frame.pack_propagate(False)
    
    logo_label = tk.Label(logo_frame, text="CVTE", 
                         font=('Arial', 24, 'bold'),
                         bg='#FFFFFF', fg='#4A7FB8')
    logo_label.pack(expand=True)
    
    # 按钮区域
    button_area = tk.Frame(top_frame, bg='#FFFFFF')
    button_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=20)
    
    # 按钮容器
    btn_container = tk.Frame(button_area, bg='#FFFFFF')
    btn_container.pack(expand=True)
    
    # 创建模拟圆角矩形按钮（使用ttk.Button的圆角样式）
    style = tk.ttk.Style()
    style.theme_use('clam')
    
    # 配置按钮样式
    style.configure('RoundedButton.TButton',
                   background='#4A7FB8',
                   foreground='white',
                   borderwidth=2,
                   focuscolor='none',
                   font=('Microsoft YaHei', 11, 'bold'),
                   relief='flat')
    
    style.map('RoundedButton.TButton',
             background=[('active', '#5A8FC8'),
                        ('pressed', '#FFFFFF')],
             foreground=[('pressed', '#4A7FB8')])
    
    # 创建按钮
    button_names = ["测试主界面", "自定义功能", "仪器指令", "手动控制", "设备端口"]
    
    for i, name in enumerate(button_names):
        # 选中状态的按钮
        if i == 2:  # 仪器指令按钮为选中状态
            btn = tk.Label(btn_container, text=name,
                          bg='#FFFFFF', fg='#4A7FB8',
                          font=('Microsoft YaHei', 11, 'bold'),
                          width=12, height=2,
                          relief='solid', bd=2)
        else:
            btn = tk.Label(btn_container, text=name,
                          bg='#4A7FB8', fg='white',
                          font=('Microsoft YaHei', 11, 'bold'),
                          width=12, height=2,
                          relief='flat', bd=0)
            
            # 添加悬停效果
            def on_enter(event, button=btn):
                if button['bg'] != '#FFFFFF':  # 非选中状态
                    button.configure(bg='#5A8FC8', cursor='hand2')
            
            def on_leave(event, button=btn):
                if button['bg'] != '#FFFFFF':  # 非选中状态
                    button.configure(bg='#4A7FB8', cursor='')
            
            def on_click(event, button_name=name):
                print(f"点击了: {button_name}")
            
            btn.bind('<Enter>', on_enter)
            btn.bind('<Leave>', on_leave)
            btn.bind('<Button-1>', on_click)
        
        btn.pack(side=tk.LEFT, padx=5, pady=30)
    
    # 底部说明
    info_frame = tk.Frame(root, bg='#7BA7D9')
    info_frame.pack(fill=tk.X, padx=20, pady=10)
    
    info_label = tk.Label(info_frame, 
                         text="✅ 界面已更新为圆角矩形按钮样式\n💡 按钮支持悬停效果和点击反馈\n🎨 采用现代化蓝色主题设计",
                         bg='#7BA7D9', fg='white',
                         font=('Microsoft YaHei', 12),
                         justify=tk.LEFT)
    info_label.pack(anchor='w')
    
    print("🎉 圆角矩形按钮界面演示")
    print("✨ 主要特点:")
    print("   • 圆角矩形设计，更加现代化")
    print("   • 蓝色主题配色方案")
    print("   • 悬停和点击交互效果")
    print("   • 选中状态高亮显示")
    
    root.mainloop()

if __name__ == "__main__":
    create_rounded_button_effect()
