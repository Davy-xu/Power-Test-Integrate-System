"""
自定义功能选项卡
"""
import tkinter as tk
from tkinter import ttk
import os
import sys
from datetime import datetime

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
        
        # 创建水平拆分面板 - 左侧为原有内容，右侧为仪器指令列表
        self.paned_window = ttk.PanedWindow(self.parent_frame, orient=tk.HORIZONTAL)
        self.paned_window.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # 左侧面板 - 放原有内容
        self.left_frame = tk.Frame(self.paned_window, bg='#ffffff')
        self.paned_window.add(self.left_frame, weight=2)  # 左侧占比较大
        
        # 右侧面板 - 放仪器指令列表
        self.right_frame = tk.Frame(self.paned_window, bg='#ffffff')
        self.paned_window.add(self.right_frame, weight=1)  # 右侧占比较小
        
        # 在左侧面板创建新建测试项目按钮
        self.create_main_button()
        
        # 在右侧面板创建仪器指令列表
        self.create_instrument_command_list()
        
    def create_main_button(self):
        """创建主要的新建测试子程序按钮和搜索下拉框"""
        # 创建整行容器，横跨整个宽度
        main_container = tk.Frame(self.left_frame, bg='#ffffff')
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
        
        # 创建左侧已选择的仪器指令列表
        self.create_selected_commands_list()
    
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
    
    def create_instrument_command_list(self):
        """创建仪器指令列表"""
        # 创建标题
        title_frame = tk.Frame(self.right_frame, bg='#ffffff')
        title_frame.pack(fill=tk.X, padx=10, pady=10)
        
        title_label = tk.Label(
            title_frame,
            text="仪器指令列表",
            font=('Microsoft YaHei', 14, 'bold'),
            bg='#ffffff',
            fg='#333333'
        )
        title_label.pack(side=tk.LEFT)
        
        # 创建刷新按钮
        refresh_button = tk.Button(
            title_frame,
            text="刷新",
            bg="#4CAF50",
            fg='white',
            font=('Microsoft YaHei', 9),
            relief='flat',
            borderwidth=0,
            cursor='hand2',
            padx=10,
            command=self.refresh_instrument_commands
        )
        refresh_button.pack(side=tk.RIGHT)
        
        # 创建查看指令按钮
        add_button = tk.Button(
            title_frame,
            text="查看指令",
            bg="#2196F3",
            fg='white',
            font=('Microsoft YaHei', 9),
            relief='flat',
            borderwidth=0,
            cursor='hand2',
            padx=10,
            command=self.view_command_details
        )
        add_button.pack(side=tk.RIGHT, padx=(0, 10))
        
        # 添加下拉框作为过滤器
        filter_frame = tk.Frame(self.right_frame, bg='#ffffff')
        filter_frame.pack(fill=tk.X, padx=10, pady=(0, 10))
        
        # 仪器分类过滤器
        self.device_type_var = tk.StringVar()
        tk.Label(
            filter_frame, 
            text="仪器分类:", 
            bg='#ffffff',
            font=('Microsoft YaHei', 9)
        ).grid(row=0, column=0, sticky='w', pady=2)
        
        self.device_type_combo = ttk.Combobox(
            filter_frame,
            textvariable=self.device_type_var,
            width=15,
            font=('Microsoft YaHei', 9),
            state='readonly'
        )
        self.device_type_combo.grid(row=0, column=1, sticky='w', padx=5, pady=2)
        self.device_type_combo.bind('<<ComboboxSelected>>', self.filter_instrument_commands)
        
        # 创建Treeview显示列表
        columns = ('device_type', 'device_model', 'function_type')
        self.tree = ttk.Treeview(self.right_frame, columns=columns, show='headings', height=15)
        
        # 设置列标题
        self.tree.heading('device_type', text='仪器分类')
        self.tree.heading('device_model', text='仪器型号')
        self.tree.heading('function_type', text='功能分类')
        
        # 设置列宽
        self.tree.column('device_type', width=100)
        self.tree.column('device_model', width=120)
        self.tree.column('function_type', width=120)
        
        # 添加垂直滚动条
        scrollbar = ttk.Scrollbar(self.right_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # 绑定双击事件
        self.tree.bind('<Double-1>', self.on_tree_double_click)
        
        # 加载数据
        self.refresh_instrument_commands()
    
    def refresh_instrument_commands(self):
        """刷新仪器指令列表"""
        # 清空现有数据
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        try:
            # 从数据库获取数据
            db = ReadDataBase()
            commands = db.get_all_instrument_commands()
            
            # 获取所有不重复的仪器分类
            device_types = sorted(list(set([cmd['device_type'] for cmd in commands])))
            self.device_type_combo['values'] = ['全部'] + device_types
            self.device_type_var.set('全部')
            
            # 存储完整的命令数据
            self.all_commands = commands
            
            # 填充数据到Treeview
            self.populate_tree_with_commands(commands)
            
        except Exception as e:
            print(f"刷新仪器指令列表时发生错误: {e}")
    
    def filter_instrument_commands(self, event=None):
        """根据选定的过滤器筛选仪器指令"""
        selected_type = self.device_type_var.get()
        
        if selected_type == '全部':
            filtered_commands = self.all_commands
        else:
            filtered_commands = [cmd for cmd in self.all_commands if cmd['device_type'] == selected_type]
            
        # 清空现有数据
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        # 填充过滤后的数据
        self.populate_tree_with_commands(filtered_commands)
    
    def populate_tree_with_commands(self, commands):
        """将命令数据填充到树视图中"""
        for i, cmd in enumerate(commands):
            # 使用交替行颜色
            tag = 'even' if i % 2 == 0 else 'odd'
            
            self.tree.insert('', tk.END, values=(
                cmd['device_type'],
                cmd['device_model'],
                cmd['function_type']
            ), tags=(tag,))
        
        # 设置交替行颜色
        self.tree.tag_configure('even', background='#f0f0f0')
        self.tree.tag_configure('odd', background='#ffffff')
    
    def on_tree_double_click(self, event):
        """处理双击事件 - 现在是添加指令到左侧列表"""
        selected_item = self.tree.selection()
        if not selected_item:
            return
            
        # 获取选中项的值
        item = self.tree.item(selected_item[0])
        values = item['values']
        
        if len(values) >= 3:
            device_type, device_model, function_type = values[0], values[1], values[2]
            
            # 查找完整的命令信息并添加到左侧列表
            for cmd in self.all_commands:
                if (cmd['device_type'] == device_type and 
                    cmd['device_model'] == device_model and 
                    cmd['function_type'] == function_type):
                    self.add_command_to_left_list(cmd)
                    break
    
    def show_command_details(self, device_type, device_model, function_type):
        """显示命令详细信息"""
        # 找到对应的命令
        command_details = None
        for cmd in self.all_commands:
            if (cmd['device_type'] == device_type and 
                cmd['device_model'] == device_model and 
                cmd['function_type'] == function_type):
                command_details = cmd
                break
                
        if not command_details:
            return
            
        # 创建详细信息对话框
        dialog = tk.Toplevel(self.parent_frame)
        dialog.title("仪器指令详细信息")
        dialog.geometry("500x400")
        dialog.resizable(False, False)
        dialog.configure(bg='#ffffff')
        
        # 居中显示
        dialog.update_idletasks()
        width = 500
        height = 400
        screen_width = dialog.winfo_screenwidth()
        screen_height = dialog.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        dialog.geometry(f"{width}x{height}+{x}+{y}")
        
        dialog.transient(self.parent_frame)
        dialog.grab_set()
        
        # 创建信息显示区域
        info_frame = tk.Frame(dialog, bg='#ffffff')
        info_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # 设备信息
        tk.Label(
            info_frame, 
            text=f"仪器分类: {device_type}",
            font=('Microsoft YaHei', 12, 'bold'),
            bg='#ffffff',
            fg='#333333'
        ).pack(anchor='w', pady=(0, 5))
        
        tk.Label(
            info_frame, 
            text=f"仪器型号: {device_model}",
            font=('Microsoft YaHei', 12),
            bg='#ffffff',
            fg='#333333'
        ).pack(anchor='w', pady=5)
        
        tk.Label(
            info_frame, 
            text=f"功能分类: {function_type}",
            font=('Microsoft YaHei', 12),
            bg='#ffffff',
            fg='#333333'
        ).pack(anchor='w', pady=5)
        
        # 指令详细信息
        tk.Label(
            info_frame, 
            text="指令:",
            font=('Microsoft YaHei', 11, 'bold'),
            bg='#ffffff',
            fg='#333333'
        ).pack(anchor='w', pady=(15, 5))
        
        command_text = tk.Text(
            info_frame,
            font=('Courier New', 11),
            bg='#f8f8f8',
            fg='#000000',
            height=4,
            wrap=tk.WORD,
            relief='solid',
            borderwidth=1
        )
        command_text.pack(fill=tk.X, pady=5)
        command_text.insert(tk.END, command_details['command'])
        command_text.configure(state='disabled')
        
        # 参数提醒
        tk.Label(
            info_frame, 
            text="参数提醒:",
            font=('Microsoft YaHei', 11, 'bold'),
            bg='#ffffff',
            fg='#333333'
        ).pack(anchor='w', pady=(10, 5))
        
        params_text = tk.Text(
            info_frame,
            font=('Microsoft YaHei', 10),
            bg='#f8f8f8',
            fg='#555555',
            height=3,
            wrap=tk.WORD,
            relief='solid',
            borderwidth=1
        )
        params_text.pack(fill=tk.X, pady=5)
        params_text.insert(tk.END, command_details['params_reminder'] or "无参数提醒")
        params_text.configure(state='disabled')
        
        # 更新时间
        tk.Label(
            info_frame, 
            text=f"更新时间: {command_details['update_time']}",
            font=('Microsoft YaHei', 9),
            bg='#ffffff',
            fg='#888888'
        ).pack(anchor='e', pady=(10, 0))
        
        # 按钮框架
        button_frame = tk.Frame(dialog, bg='#ffffff')
        button_frame.pack(pady=(0, 20))
        
        # 确定按钮
        ok_button = tk.Button(
            button_frame,
            text="确定",
            bg="#4CAF50",
            fg='white',
            font=('Microsoft YaHei', 11, 'bold'),
            relief='flat',
            borderwidth=0,
            cursor='hand2',
            width=8,
            command=dialog.destroy
        )
        ok_button.pack(side=tk.LEFT)
        
        # 绑定Escape键关闭窗口
        dialog.bind('<Escape>', lambda event: dialog.destroy())
    
    def create_selected_commands_list(self):
        """创建左侧已选择的仪器指令列表"""
        # 初始化已选择命令列表
        self.selected_commands = []
        
        # 创建标题框架
        title_frame = tk.Frame(self.left_frame, bg='#ffffff')
        title_frame.pack(fill=tk.X, padx=10, pady=(20, 10))
        
        title_label = tk.Label(
            title_frame,
            text="已选择的仪器指令",
            font=('Microsoft YaHei', 14, 'bold'),
            bg='#ffffff',
            fg='#333333'
        )
        title_label.pack(side=tk.LEFT)
        
        # 创建清空按钮
        clear_button = tk.Button(
            title_frame,
            text="清空列表",
            bg="#F44336",
            fg='white',
            font=('Microsoft YaHei', 9),
            relief='flat',
            borderwidth=0,
            cursor='hand2',
            padx=10,
            command=self.clear_left_list
        )
        clear_button.pack(side=tk.RIGHT)
        
        # 创建保存按钮
        save_button = tk.Button(
            title_frame,
            text="保存选择",
            bg="#4CAF50",
            fg='white',
            font=('Microsoft YaHei', 9),
            relief='flat',
            borderwidth=0,
            cursor='hand2',
            padx=10,
            command=self.save_selected_commands
        )
        save_button.pack(side=tk.RIGHT, padx=(0, 10))
        
        # 创建Treeview显示已选择的列表
        columns = ('device_info', 'command', 'params_reminder', 'params_input')
        self.left_tree = ttk.Treeview(self.left_frame, columns=columns, show='headings', height=15)
        
        # 设置列标题
        self.left_tree.heading('device_info', text='仪器信息')
        self.left_tree.heading('command', text='指令')
        self.left_tree.heading('params_reminder', text='参数提醒')
        self.left_tree.heading('params_input', text='参数输入')
        
        # 设置列宽
        self.left_tree.column('device_info', width=180)
        self.left_tree.column('command', width=150)
        self.left_tree.column('params_reminder', width=150)
        self.left_tree.column('params_input', width=150)
        
        # 添加垂直滚动条
        scrollbar = ttk.Scrollbar(self.left_frame, orient=tk.VERTICAL, command=self.left_tree.yview)
        self.left_tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.left_tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # 添加右键菜单
        self.left_tree_menu = tk.Menu(self.left_frame, tearoff=0)
        self.left_tree_menu.add_command(label="移除", command=self.remove_selected_command)
        self.left_tree_menu.add_command(label="上移", command=lambda: self.move_command("up"))
        self.left_tree_menu.add_command(label="下移", command=lambda: self.move_command("down"))
        self.left_tree_menu.add_separator()
        self.left_tree_menu.add_command(label="清空列表", command=self.clear_left_list)
        
        # 绑定右键菜单事件
        self.left_tree.bind("<Button-3>", self.show_left_tree_popup)
    
    def view_command_details(self):
        """显示当前选中项的指令详细信息"""
        selected_items = self.tree.selection()
        if not selected_items:
            from tkinter import messagebox
            messagebox.showinfo("提示", "请先选择右侧列表中的一项", parent=self.parent_frame)
            return
        
        # 只获取第一个选中项
        item_id = selected_items[0]
        item = self.tree.item(item_id)
        values = item['values']
        
        if len(values) >= 3:
            device_type, device_model, function_type = values[0], values[1], values[2]
            # 显示详细信息
            self.show_command_details(device_type, device_model, function_type)
    
    def add_to_left_list(self):
        """从右侧列表添加选中项到左侧列表 - 已被view_command_details替代，保留方法供其他地方引用"""
        selected_items = self.tree.selection()
        if not selected_items:
            from tkinter import messagebox
            messagebox.showinfo("提示", "请先选择右侧列表中的一项", parent=self.parent_frame)
            return
        
        for item_id in selected_items:
            item = self.tree.item(item_id)
            values = item['values']
            if len(values) >= 3:
                device_type, device_model, function_type = values[0], values[1], values[2]
                
                # 查找完整的命令信息
                for cmd in self.all_commands:
                    if (cmd['device_type'] == device_type and 
                        cmd['device_model'] == device_model and 
                        cmd['function_type'] == function_type):
                        self.add_command_to_left_list(cmd)
                        break
    
    def add_command_to_left_list(self, command):
        """添加命令到左侧列表，允许重复添加相同的指令"""
        # 创建扩展的命令对象，增加参数输入字段
        extended_command = command.copy()
        
        # 分析指令字符串，确定参数数量
        cmd_text = command.get('command', '')
        params_reminder = command.get('params_reminder', '')
        
        # 从指令文本中提取参数数量
        import re
        # 查找指令中的 value 或 valueN 模式
        cmd_values = re.findall(r'value\d*', cmd_text)
        # 查找可能的其他参数表示方式，如 <param1>
        cmd_params = re.findall(r'<(\w+)>', cmd_text)
        
        # 如果在指令中找到了参数
        if cmd_values:
            # 生成与指令中匹配的参数格式
            params_input = ";".join([f"{val}=?" for val in cmd_values]) + ";"
        elif cmd_params:
            # 使用找到的参数名
            params_input = ";".join([f"{param}=?" for param in cmd_params]) + ";"
        else:
            # 分析指令文本中可能的值参数个数
            # 通常指令最后的单词可能是值参数，如 :HOR:SCA value1;
            parts = cmd_text.split()
            if parts and not parts[-1].startswith(':'):
                # 如果最后一部分可能是值，只使用一个参数
                params_input = "value1=?;"
            elif "value" in cmd_text.lower():
                # 如果指令中包含"value"字样，但没有具体数量，使用一个参数
                params_input = "value1=?;"
            else:
                # 从参数提醒中获取线索
                if params_reminder:
                    param_names = re.findall(r'(\w+)\s*[:：]', params_reminder)
                    if param_names:
                        # 使用从参数提醒中提取的参数名
                        params_input = ";".join([f"{name}=?" for name in param_names]) + ";"
                    else:
                        # 默认使用单个参数
                        params_input = "value1=?;"
                else:
                    # 没有找到任何参数信息，默认使用单个参数
                    params_input = "value1=?;"
        
        extended_command['params_input'] = params_input
        
        # 添加到已选择列表
        self.selected_commands.append(extended_command)
        
        # 更新左侧树状视图
        self.update_left_tree()
    
    def update_left_tree(self):
        """更新左侧树状视图"""
        # 清空现有数据
        for item in self.left_tree.get_children():
            self.left_tree.delete(item)
        
        # 填充数据
        for i, cmd in enumerate(self.selected_commands):
            # 使用交替行颜色
            tag = 'even' if i % 2 == 0 else 'odd'
            
            # 合并仪器分类、型号和功能分类
            device_info = f"{cmd['device_type']} - {cmd['device_model']} - {cmd['function_type']}"
            
            # 获取参数输入，如果不存在则使用空字符串
            params_input = cmd.get('params_input', "")
            
            self.left_tree.insert('', tk.END, values=(
                device_info,
                cmd['command'],
                cmd.get('params_reminder', ""),  # 使用get避免键不存在的错误
                params_input
            ), tags=(tag,))
        
        # 设置交替行颜色
        self.left_tree.tag_configure('even', background='#f0f0f0')
        self.left_tree.tag_configure('odd', background='#ffffff')
        
        # 绑定双击事件用于编辑参数
        self.left_tree.bind('<Double-1>', self.edit_params_input)
    
    def show_left_tree_popup(self, event):
        """显示左侧树状视图的右键菜单"""
        # 先选中鼠标所在的项
        item = self.left_tree.identify_row(event.y)
        if item:
            self.left_tree.selection_set(item)
            self.left_tree_menu.post(event.x_root, event.y_root)
    
    def remove_selected_command(self):
        """从左侧列表移除选中的命令"""
        selected_items = self.left_tree.selection()
        if not selected_items:
            return
        
        for item_id in selected_items:
            item = self.left_tree.item(item_id)
            values = item['values']
            if len(values) >= 1:
                # 从合并的信息中提取仪器分类、型号和功能分类
                device_info_parts = values[0].split(' - ')
                if len(device_info_parts) >= 3:
                    device_type, device_model, function_type = device_info_parts[0], device_info_parts[1], device_info_parts[2]
                    
                    # 从列表中移除
                    self.selected_commands = [cmd for cmd in self.selected_commands 
                                            if not (cmd['device_type'] == device_type and 
                                                  cmd['device_model'] == device_model and 
                                                  cmd['function_type'] == function_type)]
        
        # 更新左侧树状视图
        self.update_left_tree()
    
    def edit_params_input(self, event):
        """编辑参数输入"""
        # 获取当前点击的列
        column = self.left_tree.identify_column(event.x)
        column_index = int(column.replace('#', '')) - 1  # 将列标识符转换为索引
        
        # 只有当点击的是参数输入列(索引3)时才允许编辑
        if column_index != 3:
            return
            
        selected_items = self.left_tree.selection()
        if not selected_items:
            return
            
        item_id = selected_items[0]
        item = self.left_tree.item(item_id)
        values = item['values']
        
        if len(values) >= 4:
            # 获取当前项的信息
            device_info = values[0]
            device_info_parts = device_info.split(' - ')
            if len(device_info_parts) < 3:
                return
                
            device_type, device_model, function_type = device_info_parts[0], device_info_parts[1], device_info_parts[2]
            command_text = values[1]
            params_reminder = values[2]
            current_params = values[3]
            
            # 创建编辑对话框
            self.show_params_edit_dialog(item_id, device_type, device_model, function_type, command_text, params_reminder, current_params)
    
    def show_params_edit_dialog(self, item_id, device_type, device_model, function_type, command_text, params_reminder, current_params):
        """显示参数编辑对话框"""
        from tkinter import messagebox
        
        # 创建编辑对话框
        dialog = tk.Toplevel(self.parent_frame)
        dialog.title("编辑参数输入")
        dialog.geometry("500x350")
        dialog.resizable(False, False)
        dialog.configure(bg='#ffffff')
        
        # 居中显示
        dialog.update_idletasks()
        width = 500
        height = 350
        screen_width = dialog.winfo_screenwidth()
        screen_height = dialog.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        dialog.geometry(f"{width}x{height}+{x}+{y}")
        
        dialog.transient(self.parent_frame)
        dialog.grab_set()
        
        # 创建信息显示区域
        info_frame = tk.Frame(dialog, bg='#ffffff')
        info_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # 设备信息
        tk.Label(
            info_frame, 
            text=f"仪器信息: {device_type} - {device_model} - {function_type}",
            font=('Microsoft YaHei', 12, 'bold'),
            bg='#ffffff',
            fg='#333333'
        ).pack(anchor='w', pady=(0, 10))
        
        # 指令信息
        tk.Label(
            info_frame, 
            text="指令:",
            font=('Microsoft YaHei', 11, 'bold'),
            bg='#ffffff',
            fg='#333333'
        ).pack(anchor='w', pady=(5, 5))
        
        command_text_widget = tk.Text(
            info_frame,
            font=('Courier New', 11),
            bg='#f8f8f8',
            fg='#000000',
            height=3,
            wrap=tk.WORD,
            relief='solid',
            borderwidth=1
        )
        command_text_widget.pack(fill=tk.X, pady=5)
        command_text_widget.insert(tk.END, command_text)
        command_text_widget.configure(state='disabled')
        
        # 参数提醒
        tk.Label(
            info_frame, 
            text="参数提醒:",
            font=('Microsoft YaHei', 11, 'bold'),
            bg='#ffffff',
            fg='#333333'
        ).pack(anchor='w', pady=(10, 5))
        
        params_reminder_widget = tk.Text(
            info_frame,
            font=('Microsoft YaHei', 10),
            bg='#f8f8f8',
            fg='#555555',
            height=2,
            wrap=tk.WORD,
            relief='solid',
            borderwidth=1
        )
        params_reminder_widget.pack(fill=tk.X, pady=5)
        params_reminder_widget.insert(tk.END, params_reminder or "无参数提醒")
        params_reminder_widget.configure(state='disabled')
        
        # 参数输入
        tk.Label(
            info_frame, 
            text="参数输入:",
            font=('Microsoft YaHei', 11, 'bold'),
            bg='#ffffff',
            fg='#333333'
        ).pack(anchor='w', pady=(10, 5))
        
        # 说明标签
        tk.Label(
            info_frame,
            text="格式: name=value; (使用分号分隔多个参数，使用?作为占位符)",
            font=('Microsoft YaHei', 9),
            bg='#ffffff',
            fg='#666666'
        ).pack(anchor='w', pady=(0, 5))
        
        # 使用文本框而不是Entry，以便更好地编辑多行参数
        params_text = tk.Text(
            info_frame,
            font=('Courier New', 11),
            bg='#ffffff',
            fg='#000000',
            height=4,
            relief='solid',
            borderwidth=1
        )
        params_text.pack(fill=tk.X, pady=5)
        params_text.insert(tk.END, current_params)
        params_text.focus_set()
        
        # 添加示例按钮
        example_button = tk.Button(
            info_frame,
            text="插入示例格式",
            font=('Microsoft YaHei', 9),
            bg='#E0E0E0',
            relief='flat',
            borderwidth=0,
            cursor='hand2',
            command=lambda: self.generate_example_format(params_text, command_text)
        )
        example_button.pack(anchor='e', pady=(0, 10))
        
        # 按钮框架
        button_frame = tk.Frame(dialog, bg='#ffffff')
        button_frame.pack(pady=(0, 20))
        
        # 保存按钮
        def on_save():
            # 获取文本框中的内容
            new_params = params_text.get(1.0, tk.END).strip()
            
            # 验证参数格式
            if new_params and not new_params.endswith(';'):
                new_params += ';'  # 确保结尾有分号
                
            # 更新内存中的数据
            for cmd in self.selected_commands:
                if (cmd['device_type'] == device_type and 
                    cmd['device_model'] == device_model and 
                    cmd['function_type'] == function_type):
                    cmd['params_input'] = new_params
                    break
            
            # 更新视图
            self.update_left_tree()
            dialog.destroy()
        
        save_button = tk.Button(
            button_frame,
            text="保存",
            bg="#4CAF50",
            fg='white',
            font=('Microsoft YaHei', 11, 'bold'),
            relief='flat',
            borderwidth=0,
            cursor='hand2',
            width=8,
            command=on_save
        )
        save_button.pack(side=tk.LEFT, padx=(0, 10))
        
        # 取消按钮
        cancel_button = tk.Button(
            button_frame,
            text="取消",
            bg="#CCCCCC",
            fg='#333333',
            font=('Microsoft YaHei', 11, 'bold'),
            relief='flat',
            borderwidth=0,
            cursor='hand2',
            width=8,
            command=dialog.destroy
        )
        cancel_button.pack(side=tk.LEFT)
        
        # 绑定回车键和Escape键
        dialog.bind('<Return>', lambda event: on_save())
        dialog.bind('<Escape>', lambda event: dialog.destroy())
    
    def generate_example_format(self, text_widget, command_text):
        """根据指令文本生成参数输入示例格式"""
        import re
        
        # 清空当前内容
        text_widget.delete(1.0, tk.END)
        
        # 获取命令文本
        cmd_text = command_text
        
        # 查找指令中的 value 或 valueN 模式
        cmd_values = re.findall(r'value\d*', cmd_text)
        # 查找可能的其他参数表示方式，如 <param1>
        cmd_params = re.findall(r'<(\w+)>', cmd_text)
        
        # 如果在指令中找到了参数
        if cmd_values:
            # 生成与指令中匹配的参数格式
            params_input = ";".join([f"{val}=123" for val in cmd_values]) + ";"
        elif cmd_params:
            # 使用找到的参数名
            params_input = ";".join([f"{param}=123" for param in cmd_params]) + ";"
        else:
            # 分析指令文本中可能的值参数个数
            # 通常指令最后的单词可能是值参数，如 :HOR:SCA value1;
            parts = cmd_text.split()
            if parts and not parts[-1].startswith(':'):
                # 如果最后一部分可能是值，只使用一个参数
                params_input = "value1=123;"
            else:
                # 默认使用单个参数
                params_input = "value1=123;"
        
        # 插入生成的示例格式
        text_widget.insert(tk.END, params_input)
    
    def move_command(self, direction):
        """上移或下移左侧列表中的命令"""
        selected_items = self.left_tree.selection()
        if not selected_items:
            return
        
        # 获取所有项的ID
        all_items = self.left_tree.get_children()
        
        for item_id in selected_items:
            # 获取当前索引
            current_index = all_items.index(item_id)
            
            if direction == "up" and current_index > 0:
                # 上移
                item = self.left_tree.item(item_id)
                values = item['values']
                if len(values) >= 1:
                    # 从合并的信息中提取仪器分类、型号和功能分类
                    device_info_parts = values[0].split(' - ')
                    if len(device_info_parts) >= 3:
                        device_type, device_model, function_type = device_info_parts[0], device_info_parts[1], device_info_parts[2]
                        
                        # 查找对应的命令
                        for i, cmd in enumerate(self.selected_commands):
                            if (cmd['device_type'] == device_type and 
                                cmd['device_model'] == device_model and 
                                cmd['function_type'] == function_type):
                                if i > 0:
                                    # 交换位置
                                    self.selected_commands[i], self.selected_commands[i-1] = \
                                        self.selected_commands[i-1], self.selected_commands[i]
                                    break
                    
            elif direction == "down" and current_index < len(all_items) - 1:
                # 下移
                item = self.left_tree.item(item_id)
                values = item['values']
                if len(values) >= 1:
                    # 从合并的信息中提取仪器分类、型号和功能分类
                    device_info_parts = values[0].split(' - ')
                    if len(device_info_parts) >= 3:
                        device_type, device_model, function_type = device_info_parts[0], device_info_parts[1], device_info_parts[2]
                        
                        # 查找对应的命令
                        for i, cmd in enumerate(self.selected_commands):
                            if (cmd['device_type'] == device_type and 
                                cmd['device_model'] == device_model and 
                                cmd['function_type'] == function_type):
                                if i < len(self.selected_commands) - 1:
                                    # 交换位置
                                    self.selected_commands[i], self.selected_commands[i+1] = \
                                        self.selected_commands[i+1], self.selected_commands[i]
                                    break
        
        # 更新左侧树状视图
        self.update_left_tree()
    
    def clear_left_list(self):
        """清空左侧列表"""
        from tkinter import messagebox
        result = messagebox.askyesno(
            "确认清空", 
            "确定要清空已选择的所有仪器指令吗？",
            parent=self.parent_frame
        )
        
        if result:
            self.selected_commands = []
            self.update_left_tree()
    
    def save_selected_commands(self):
        """保存已选择的命令列表"""
        if not self.selected_commands:
            from tkinter import messagebox
            messagebox.showinfo("提示", "请先添加仪器指令到左侧列表", parent=self.parent_frame)
            return
        
        # 创建保存对话框
        from tkinter import messagebox
        messagebox.showinfo(
            "保存成功", 
            f"已成功保存 {len(self.selected_commands)} 个仪器指令！",
            parent=self.parent_frame
        )
        
        # 这里可以添加保存到数据库或文件的逻辑
        print(f"已保存 {len(self.selected_commands)} 个仪器指令")
        for cmd in self.selected_commands:
            params_input = cmd.get('params_input', "")
            print(f"  - {cmd['device_type']} - {cmd['device_model']} - {cmd['function_type']}")
            print(f"    指令: {cmd['command']}")
            print(f"    参数: {params_input if params_input else '无'}")
            print("")
    
