"""
最简化的主界面 - 确保按钮可见
"""
import tkinter as tk
from interface.enhanced_parallelogram_button import EnhancedParallelogramButton

class SimpleMainInterface:
    """简化的主界面"""
    
    def __init__(self, root):
        self.root = root
        self.current_tab = 0
        self.create_interface()
    
    def create_interface(self):
        """创建界面"""
        # 标题栏
        title_frame = tk.Frame(self.root, bg='#f5f5f5', height=50)
        title_frame.pack(fill=tk.X)
        title_frame.pack_propagate(False)
        
        title_label = tk.Label(title_frame, text="电源测试设备集成控制系统",
                              font=('Microsoft YaHei', 16, 'bold'),
                              bg='#f5f5f5', fg='#333333')
        title_label.pack(pady=15)
        
        # 按钮区域
        button_frame = tk.Frame(self.root, bg='#f5f5f5', height=80)
        button_frame.pack(fill=tk.X, pady=10)
        button_frame.pack_propagate(False)
        
        # 按钮容器
        btn_container = tk.Frame(button_frame, bg='#f5f5f5')
        btn_container.pack(expand=True)
        
        # 创建标签按钮
        tab_names = ["测试主界面", "自定义功能", "仪器指令", "手动控制", "设备端口"]
        self.buttons = []
        
        for i, name in enumerate(tab_names):
            btn = EnhancedParallelogramButton(
                btn_container,
                text=name,
                width=120,
                height=45,
                bg_color='#4a90e2',
                fg_color='white',
                command=lambda idx=i: self.switch_tab(idx)
            )
            btn.pack(side=tk.LEFT, padx=5, pady=10)
            self.buttons.append(btn)
            print(f"✅ 创建按钮: {name}")
        
        # 内容区域
        self.content_frame = tk.Frame(self.root, bg='#ffffff', relief='solid', bd=1)
        self.content_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))
        
        # 默认内容
        self.show_content("测试主界面")
        
        # 设置第一个按钮为选中状态
        if self.buttons:
            self.buttons[0].set_active(True)
    
    def switch_tab(self, index):
        """切换标签"""
        print(f"切换到标签 {index}")
        
        # 重置所有按钮状态
        for btn in self.buttons:
            btn.set_active(False)
        
        # 设置当前按钮为选中
        self.buttons[index].set_active(True)
        
        # 显示对应内容
        tab_names = ["测试主界面", "自定义功能", "仪器指令", "手动控制", "设备端口"]
        self.show_content(tab_names[index])
    
    def show_content(self, tab_name):
        """显示内容"""
        # 清除之前的内容
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        # 显示新内容
        content_label = tk.Label(self.content_frame, 
                               text=f"当前标签: {tab_name}\n\n这是 {tab_name} 的内容区域",
                               font=('Microsoft YaHei', 14),
                               bg='#ffffff', fg='#333333')
        content_label.pack(expand=True)

def main():
    print("🚀 启动简化版主界面...")
    
    root = tk.Tk()
    root.title("电源测试设备集成控制系统")
    root.geometry("1000x700")
    root.configure(bg='#f5f5f5')
    
    app = SimpleMainInterface(root)
    
    print("✅ 简化版界面启动完成")
    print("🎯 按钮应该显示在窗口上方")
    
    root.mainloop()

if __name__ == "__main__":
    main()
