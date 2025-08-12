"""
最简单的按钮测试
只测试单个按钮是否能显示
"""
import tkinter as tk
from interface.rounded_parallelogram_button import RoundedParallelogramButton

def simple_test():
    root = tk.Tk()
    root.title("单个按钮测试")
    root.geometry("300x200")
    root.configure(bg='#f5f5f5')
    
    # 直接创建一个按钮
    button = RoundedParallelogramButton(
        root,
        text="测试按钮",
        width=120,
        height=45,
        command=lambda: print("按钮被点击了！")
    )
    button.pack(pady=50)
    
    print("单个按钮测试启动...")
    root.mainloop()

if __name__ == "__main__":
    simple_test()
