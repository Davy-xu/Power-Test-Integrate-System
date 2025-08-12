"""
自定义功能选项卡
"""
import tkinter as tk
from tkinter import ttk
import os
import sys

# 添加项目根目录到路径以便导入ConnectDatabase
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))
if project_root not in sys.path:
    sys.path.append(project_root)

from ConnectDatabase import ReadDataBase


class CustomFunctionTab:
    """自定义功能选项卡"""
    
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        self.create_content()
    
    def create_content(self):
        """创建自定义功能内容"""
        # 设置整个内容区域背景为白色
        self.parent_frame.configure(bg='#ffffff')
        
        # 创建新建测试项目按钮
        self.create_main_button()
        
    def create_main_button(self):
        """创建主要的新建测试子程序按钮和搜索下拉框"""
        # 创建整行容器，横跨整个宽度
        main_container = tk.Frame(self.parent_frame, bg='#ffffff')
        main_container.pack(fill=tk.X, padx=0, pady=10)
        
        # 创建搜索下拉框（放在最左边）
        self.create_search_combobox(main_container)
        
        # 创建新建测试子程序按钮（放在右边）
        new_program_button = tk.Button(
            main_container,
            text="新建测试子程序",
            bg="#FF9900",
            fg='white',
            font=('Microsoft YaHei', 12, 'bold'),
            relief='flat',
            borderwidth=0,
            cursor='hand2',
            width=20,
            height=1,
            command=self.show_input_dialog
        )
        new_program_button.pack(side=tk.RIGHT, padx=(0, 10))
        
        # 添加鼠标悬停效果
        def on_button_enter(event):
            new_program_button.config(bg="#E68900")
            
        def on_button_leave(event):
            new_program_button.config(bg="#FF9900")
            
        new_program_button.bind('<Enter>', on_button_enter)
        new_program_button.bind('<Leave>', on_button_leave)
    
    def create_search_combobox(self, parent):
        """创建带模糊搜索功能的下拉框"""
        # 创建下拉框容器（紧贴最左边）
        search_frame = tk.Frame(parent, bg='#ffffff')
        search_frame.pack(side=tk.LEFT, padx=(10, 0))
        
        # 添加标签和下拉框到同一行
        search_label = tk.Label(
            search_frame,
            text="选择测试项目:",
            font=('Microsoft YaHei', 10),
            bg='#ffffff',
            fg='#666666'
        )
        search_label.pack(side=tk.LEFT, padx=(0, 10))
        
        # 创建可编辑的下拉框
        self.search_var = tk.StringVar()
        self.search_combobox = ttk.Combobox(
            search_frame,
            textvariable=self.search_var,
            font=('Microsoft YaHei', 10),
            width=25,
            state='normal'  # 允许输入
        )
        self.search_combobox.pack(side=tk.LEFT)
        
        # 绑定事件
        self.search_combobox.bind('<KeyRelease>', self.on_search_key_release)
        self.search_combobox.bind('<<ComboboxSelected>>', self.on_combobox_selected)
        
        # 初始化下拉框数据
        self.refresh_combobox_data()
    
    def refresh_combobox_data(self):
        """刷新下拉框数据"""
        try:
            db = ReadDataBase()
            # 获取所有测试项目名称
            all_programs = db.get_all_test_programs()
            self.all_program_names = [program['name'] for program in all_programs]
            
            # 更新下拉框选项
            self.search_combobox['values'] = self.all_program_names
            print(f"已加载 {len(self.all_program_names)} 个测试项目")
            
        except Exception as e:
            print(f"刷新下拉框数据时发生错误: {e}")
            self.all_program_names = []
            self.search_combobox['values'] = []
    
    def on_search_key_release(self, event):
        """搜索框输入时的模糊搜索"""
        search_text = self.search_var.get().lower()
        
        if not search_text:
            # 如果搜索框为空，显示所有项目
            filtered_names = self.all_program_names
        else:
            # 模糊搜索：包含搜索文本的项目
            filtered_names = [name for name in self.all_program_names 
                            if search_text in name.lower()]
        
        # 更新下拉框选项
        self.search_combobox['values'] = filtered_names
        
        # 如果有匹配项，自动展开下拉框
        if filtered_names and len(search_text) > 0:
            self.search_combobox.event_generate('<Button-1>')
    
    def on_combobox_selected(self, event):
        """下拉框选择事件"""
        selected_program = self.search_var.get()
        if selected_program:
            print(f"选择的测试项目: {selected_program}")
            # 这里可以添加选择项目后的处理逻辑
    
    def show_input_dialog(self):
        """显示输入对话框"""
        from tkinter import messagebox
        
        # 创建自定义对话框窗口
        dialog = tk.Toplevel(self.parent_frame)
        dialog.title("新建测试子程序")
        dialog.geometry("400x300")  # 设置对话框大小
        dialog.resizable(False, False)
        dialog.configure(bg='#ffffff')
        
        # 计算屏幕中心位置
        dialog.update_idletasks()  # 确保窗口尺寸已更新
        width = 400
        height = 300
        screen_width = dialog.winfo_screenwidth()
        screen_height = dialog.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        dialog.geometry(f"{width}x{height}+{x}+{y}")
        
        # 使对话框居中显示
        dialog.transient(self.parent_frame)
        dialog.grab_set()
        
        # 创建标题
        title_label = tk.Label(
            dialog,
            text="新建测试子程序",
            font=('Microsoft YaHei', 16, 'bold'),
            bg='#ffffff',
            fg='#333333'
        )
        title_label.pack(pady=(30, 20))
        
        # 创建输入提示
        prompt_label = tk.Label(
            dialog,
            text="请输入测试子程序名称:",
            font=('Microsoft YaHei', 12),
            bg='#ffffff',
            fg='#666666'
        )
        prompt_label.pack(pady=(0, 15))
        
        # 创建输入框
        entry_var = tk.StringVar()
        entry = tk.Entry(
            dialog,
            textvariable=entry_var,
            font=('Microsoft YaHei', 12),
            width=30,
            relief='solid',
            borderwidth=1
        )
        entry.pack(pady=10)
        entry.focus_set()
        
        # 创建按钮框架
        button_frame = tk.Frame(dialog, bg='#ffffff')
        button_frame.pack(pady=30)
        
        # 确定按钮
        def on_ok():
            program_name = entry_var.get().strip()
            if program_name:
                # 检查数据库中是否已存在相同的测试项目名称
                if self.check_program_exists(program_name):
                    messagebox.showwarning(
                        "重复提醒", 
                        f"测试项目 '{program_name}' 已存在！\n请使用不同的名称。",
                        parent=dialog
                    )
                    return
                
                # 保存到数据库
                if self.save_to_database(program_name):
                    dialog.destroy()
                    # 刷新下拉框数据
                    self.refresh_combobox_data()
                    messagebox.showinfo(
                        "创建成功", 
                        f"测试子程序 '{program_name}' 创建成功！",
                        parent=self.parent_frame
                    )
                    print(f"创建测试子程序: {program_name}")
                else:
                    messagebox.showerror(
                        "保存失败", 
                        "保存到数据库时发生错误，请重试！",
                        parent=dialog
                    )
            else:
                messagebox.showwarning(
                    "输入错误", 
                    "测试子程序名称不能为空！",
                    parent=dialog
                )
        
        ok_button = tk.Button(
            button_frame,
            text="确定",
            bg="#FF9900",
            fg='white',
            font=('Microsoft YaHei', 12, 'bold'),
            relief='flat',
            borderwidth=0,
            cursor='hand2',
            width=10,
            height=1,
            command=on_ok
        )
        ok_button.pack(side=tk.LEFT, padx=(0, 20))
        
        # 取消按钮
        def on_cancel():
            dialog.destroy()
        
        cancel_button = tk.Button(
            button_frame,
            text="取消",
            bg="#CCCCCC",
            fg='#333333',
            font=('Microsoft YaHei', 12, 'bold'),
            relief='flat',
            borderwidth=0,
            cursor='hand2',
            width=10,
            height=1,
            command=on_cancel
        )
        cancel_button.pack(side=tk.LEFT)
        
        # 绑定回车键确定
        dialog.bind('<Return>', lambda event: on_ok())
        dialog.bind('<Escape>', lambda event: on_cancel())
    
    def check_program_exists(self, program_name):
        """检查测试项目名称是否已存在"""
        try:
            db = ReadDataBase()
            return db.check_test_program_exists(program_name)
        except Exception as e:
            print(f"检查数据库时发生错误: {e}")
            return False
    
    def save_to_database(self, program_name):
        """保存测试项目到数据库"""
        try:
            db = ReadDataBase()
            success = db.insert_test_program(program_name, 0)
            if success:
                print(f"成功保存测试项目到数据库: {program_name}")
            return success
        except Exception as e:
            print(f"保存到数据库时发生错误: {e}")
            return False

    


    


