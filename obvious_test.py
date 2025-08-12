"""
明显的按钮测试 - 使用亮色
"""
import tkinter as tk
from interface.rounded_parallelogram_button import RoundedParallelogramButton

def obvious_test():
    root = tk.Tk()
    root.title("明显的按钮测试")
    root.geometry("400x300")
    root.configure(bg='white')
    
    # 标题
    title = tk.Label(root, text="圆角平行四边形按钮测试", 
                    font=('Arial', 16, 'bold'),
                    bg='white', fg='black')
    title.pack(pady=20)
    
    # 创建一个非常明显的红色按钮
    button = RoundedParallelogramButton(
        root,
        text="红色测试按钮",
        width=150,
        height=50,
        bg_color='red',
        fg_color='white',
        hover_bg='darkred',
        hover_fg='yellow',
        command=lambda: print("红色按钮被点击了！")
    )
    button.pack(pady=20)
    
    # 创建一个蓝色按钮
    button2 = RoundedParallelogramButton(
        root,
        text="蓝色测试按钮", 
        width=150,
        height=50,
        bg_color='blue',
        fg_color='white',
        hover_bg='darkblue',
        hover_fg='yellow',
        command=lambda: print("蓝色按钮被点击了！")
    )
    button2.pack(pady=10)
    
    print("明显按钮测试启动 - 应该看到红色和蓝色按钮")
    root.mainloop()

if __name__ == "__main__":
    obvious_test()
