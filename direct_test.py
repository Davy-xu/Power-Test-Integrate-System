"""
直接标签按钮测试
不使用复杂的悬空标签系统，直接在主窗口显示按钮
"""
import tkinter as tk
from interface.enhanced_parallelogram_button import EnhancedParallelogramButton

def direct_button_test():
    root = tk.Tk()
    root.title("直接按钮测试")
    root.geometry("800x600")
    root.configure(bg='#f5f5f5')
    
    # 顶部信息
    info_frame = tk.Frame(root, bg='#f5f5f5', height=80)
    info_frame.pack(fill=tk.X, pady=10)
    info_frame.pack_propagate(False)
    
    title = tk.Label(info_frame, text="🔍 直接按钮测试", 
                    font=('Microsoft YaHei', 16, 'bold'),
                    bg='#f5f5f5', fg='#333333')
    title.pack(pady=10)
    
    # 按钮容器 - 固定高度确保按钮可见
    button_container = tk.Frame(root, bg='#f5f5f5', height=100)
    button_container.pack(fill=tk.X, pady=20)
    button_container.pack_propagate(False)  # 重要：固定容器高度
    
    # 按钮框架
    button_frame = tk.Frame(button_container, bg='#f5f5f5')
    button_frame.pack(expand=True)
    
    # 创建标签按钮
    tab_texts = ["测试主界面", "自定义功能", "仪器指令", "手动控制", "设备端口"]
    
    for i, text in enumerate(tab_texts):
        print(f"创建按钮: {text}")
        
        # 按钮容器
        btn_container = tk.Frame(button_frame, bg='#f5f5f5', width=140, height=60)
        btn_container.pack(side=tk.LEFT, padx=8)
        btn_container.pack_propagate(False)  # 固定大小
        
        # 创建按钮
        button = EnhancedParallelogramButton(
            btn_container,
            text=text,
            width=120,
            height=45,
            bg_color='#4a90e2',
            fg_color='white',
            command=lambda idx=i, t=text: print(f"点击了标签: {t}")
        )
        button.pack(pady=5)  # 使用pack而不是place
    
    # 内容区域
    content_area = tk.Frame(root, bg='#ffffff', relief='solid', bd=1)
    content_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))
    
    content_label = tk.Label(content_area, text="这里是内容区域\n标签按钮应该显示在上方",
                           font=('Microsoft YaHei', 14),
                           bg='#ffffff', fg='#666666')
    content_label.pack(expand=True)
    
    print("🚀 直接按钮测试启动")
    print("📋 按钮应该显示在窗口顶部")
    
    root.mainloop()

if __name__ == "__main__":
    direct_button_test()
