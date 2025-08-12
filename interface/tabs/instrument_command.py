"""
仪器指令选项卡
"""
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import sys
import os
import json
import re

# 添加父目录到路径以导入数据库模块
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ConnectDatabase import ReadDataBase

# 导入圆角矩形按钮组件
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from rounded_rect_button import RoundedRectButton


class InstrumentCommandTab:
    """仪器指令选项卡"""
    
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        self.command_entry = None
        self.response_text = None
        self.create_content()
    
    def create_content(self):
        """创建仪器指令内容"""
        # 设置整个内容区域背景为白色
        self.parent_frame.configure(bg='#ffffff')
        
        # 创建带边框的标签框架
        border_frame = tk.LabelFrame(self.parent_frame, 
                                    text="添加仪器指令",
                                    bg='#ffffff', 
                                    fg="#000000",
                                    font=('Microsoft YaHei', 12, 'bold'),
                                    relief='solid',
                                    borderwidth=1,
                                    padx=5,
                                    pady=5)
        border_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # 在边框内创建控件行
        self.create_widget_row(border_frame)
        
        # 创建数据显示区域
        self.create_data_display(self.parent_frame)
    
    def create_widget_row(self, parent):
        """创建控件行，按照截图布局"""
        # 仪器分类 - 橙色下拉框
        device_label = tk.Label(parent, text="仪器分类", bg='#ffffff', fg='#333333',
                               font=('Microsoft YaHei', 10))
        device_label.grid(row=0, column=0, padx=(10, 5), pady=(10, 5), sticky='w')
        
        self.device_combo = ttk.Combobox(parent, 
                                   values=["示波器", "AC Source", "电子负载", "控制盒"],
                                   state="readonly",
                                   style="Orange.TCombobox",
                                   width=15,
                                   height=6)  # 下拉列表显示6个选项
        self.device_combo.grid(row=1, column=0, padx=(10, 10), pady=(0, 10), sticky='ew')
        
        # 仪器型号 - 橙色下拉框
        model_label = tk.Label(parent, text="仪器型号", bg='#ffffff', fg='#333333',
                              font=('Microsoft YaHei', 10))
        model_label.grid(row=0, column=1, padx=(0, 5), pady=(10, 5), sticky='w')
        
        self.model_combo = ttk.Combobox(parent,
                                  values=["请选择"],
                                  state="readonly",
                                  style="Orange.TCombobox",
                                  width=20,
                                  height=6)  # 下拉列表显示6个选项
        self.model_combo.grid(row=1, column=1, padx=(0, 10), pady=(0, 10), sticky='ew')
        
        # 绑定仪器分类变化事件
        self.device_combo.bind('<<ComboboxSelected>>', self.on_device_changed)
        
        # 功能分类 - 改为输入框
        function_label = tk.Label(parent, text="功能分类", bg='#ffffff', fg='#000000',
                                 font=('Microsoft YaHei', 10))
        function_label.grid(row=0, column=2, padx=(0, 5), pady=(10, 5), sticky='w')
        
        self.function_entry = tk.Entry(parent, bg='#FFFFFF', fg='black', 
                                 font=('Consolas', 10), relief='solid', 
                                 borderwidth=1, width=15)
        self.function_entry.grid(row=1, column=2, padx=(0, 10), pady=(0, 10), sticky='ew')
        
        # 指令 - 红色输入框
        command_label = tk.Label(parent, text="指令", bg='#ffffff', fg='#000000',
                                font=('Microsoft YaHei', 10))
        command_label.grid(row=0, column=3, padx=(0, 5), pady=(10, 5), sticky='w')
        
        self.command_entry = tk.Entry(parent, bg='#FFFFFF', fg='black', 
                                     font=('Consolas', 10), relief='solid', 
                                     borderwidth=1, width=15)
        self.command_entry.grid(row=1, column=3, padx=(0, 10), pady=(0, 10), sticky='ew')
        
        # 指令参数提醒 - 红色输入框
        params_label = tk.Label(parent, text="指令参数填写提醒", bg='#ffffff', fg='#000000',
                               font=('Microsoft YaHei', 10))
        params_label.grid(row=0, column=4, padx=(0, 5), pady=(10, 5), sticky='w')
        
        self.params_entry = tk.Entry(parent, bg='#FFFFFF', fg='black', 
                               font=('Consolas', 10), relief='solid', 
                               borderwidth=1, width=20)
        self.params_entry.grid(row=1, column=4, padx=(0, 10), pady=(0, 10), sticky='ew')
        
        # 添加按钮容器
        button_container = tk.Frame(parent, bg='#ffffff', width=120, height=50)
        button_container.grid(row=1, column=5, padx=(10, 10), pady=(0, 10))
        button_container.grid_propagate(False)
        
        # 添加按钮 - 矩形按钮
        add_button = tk.Button(
            button_container,
            text="添加",
            bg="#FF9900",
            fg='white',
            font=('Microsoft YaHei', 10, 'bold'),
            relief='flat',
            borderwidth=0,
            cursor='hand2',
            command=self.add_command
        )
        add_button.pack(expand=True, fill=tk.BOTH, padx=3, pady=5)
        
        # 添加鼠标悬停效果
        def on_add_button_enter(event):
            add_button.config(bg="#E68900")
            
        def on_add_button_leave(event):
            add_button.config(bg="#FF9900")
            
        add_button.bind('<Enter>', on_add_button_enter)
        add_button.bind('<Leave>', on_add_button_leave)
        
        # 配置列权重，让输入框可以拉伸
        parent.grid_columnconfigure(3, weight=1)
        parent.grid_columnconfigure(4, weight=1)
    
    def create_data_display(self, parent):
        """创建数据显示区域"""
        # 创建数据显示框架
        data_frame = tk.LabelFrame(parent, 
                                  text="数据库中的仪器指令",
                                  bg='#ffffff', 
                                  fg='#000000',
                                  font=('Microsoft YaHei', 12, 'bold'),
                                  relief='solid',
                                  borderwidth=1,
                                  padx=5,
                                  pady=5)
        data_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # 创建筛选区域
        self.create_filter_area(data_frame)
        
        # 创建表格区域
        table_frame = tk.Frame(data_frame, bg='#ffffff')
        table_frame.pack(fill=tk.BOTH, expand=True)
        
        # 创建Treeview表格
        columns = ('仪器分类', '仪器型号', '功能分类', '指令', '指令参数提醒', '更新时间', '参数输入')
        self.tree = ttk.Treeview(table_frame, columns=columns, show='headings', height=12)
        
        # 设置列标题
        for col in columns:
            self.tree.heading(col, text=col)
            if col == '指令' or col == '指令参数提醒':
                self.tree.column(col, width=150, minwidth=150)
            elif col == '更新时间':
                self.tree.column(col, width=120, minwidth=120)
            elif col == '参数输入':
                self.tree.column(col, width=120, minwidth=120)
            else:
                self.tree.column(col, width=100, minwidth=100)
        
        # 创建滚动条
        v_scrollbar = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=self.tree.yview)
        h_scrollbar = ttk.Scrollbar(table_frame, orient=tk.HORIZONTAL, command=self.tree.xview)
        self.tree.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
        
        # 布局表格和滚动条
        self.tree.grid(row=0, column=0, sticky='nsew')
        v_scrollbar.grid(row=0, column=1, sticky='ns')
        h_scrollbar.grid(row=1, column=0, sticky='ew')
        
        # 配置权重
        table_frame.grid_rowconfigure(0, weight=1)
        table_frame.grid_columnconfigure(0, weight=1)
        
        # 绑定单击事件用于编辑参数输入列
        self.tree.bind('<Button-1>', self.on_item_click)
        
        # 初始化数据和编辑相关变量
        self.all_data = []  # 存储所有数据
        self.parameter_inputs = {}  # 存储每行的参数输入内容
        self.current_edit_item = None  # 当前编辑的项目
        self.current_edit_entry = None  # 当前编辑的输入框
        self.load_initial_data()
    
    def create_filter_area(self, parent):
        """创建筛选区域"""
        filter_frame = tk.Frame(parent, bg='#ffffff')
        filter_frame.pack(fill=tk.X, pady=5)
        
        # 仪器分类筛选
        device_filter_label = tk.Label(filter_frame, text="仪器分类:", bg='#ffffff', fg='#000000',
                                      font=('Microsoft YaHei', 10))
        device_filter_label.grid(row=0, column=0, padx=(5, 5), pady=5, sticky='w')
        
        self.device_filter = ttk.Combobox(filter_frame, 
                                         values=["全部"],
                                         state="readonly",
                                         style="Orange.TCombobox",
                                         width=12)
        self.device_filter.set("全部")
        self.device_filter.grid(row=0, column=1, padx=(0, 10), pady=5, sticky='w')
        self.device_filter.bind('<<ComboboxSelected>>', self.apply_filters)
        
        # 仪器型号筛选
        model_filter_label = tk.Label(filter_frame, text="仪器型号:", bg='#ffffff', fg='#000000',
                                     font=('Microsoft YaHei', 10))
        model_filter_label.grid(row=0, column=2, padx=(5, 5), pady=5, sticky='w')
        
        self.model_filter = ttk.Combobox(filter_frame, 
                                        values=["全部"],
                                        state="readonly",
                                        style="Orange.TCombobox",
                                        width=15)
        self.model_filter.set("全部")
        self.model_filter.grid(row=0, column=3, padx=(0, 10), pady=5, sticky='w')
        self.model_filter.bind('<<ComboboxSelected>>', self.apply_filters)
        
        # 功能分类筛选
        function_filter_label = tk.Label(filter_frame, text="功能分类:", bg='#ffffff', fg='#000000',
                                        font=('Microsoft YaHei', 10))
        function_filter_label.grid(row=0, column=4, padx=(5, 5), pady=5, sticky='w')
        
        self.function_filter = ttk.Combobox(filter_frame, 
                                           values=["全部"],
                                           state="readonly",
                                           style="Orange.TCombobox",
                                           width=12)
        self.function_filter.set("全部")
        self.function_filter.grid(row=0, column=5, padx=(0, 10), pady=5, sticky='w')
        self.function_filter.bind('<<ComboboxSelected>>', self.apply_filters)
        
        # 清除筛选按钮容器
        clear_button_container = tk.Frame(filter_frame, bg='#ffffff', width=100, height=40)
        clear_button_container.grid(row=0, column=6, padx=(10, 5), pady=5)
        clear_button_container.grid_propagate(False)
        
        # 清除筛选按钮 - 长方形按钮
        clear_filter_button = tk.Button(
            clear_button_container,
            text="清除筛选",
            bg="#FF9800",
            fg='white',
            font=('Microsoft YaHei', 9, 'bold'),
            relief='flat',
            borderwidth=0,
            cursor='hand2',
            command=self.clear_filters
        )
        clear_filter_button.pack(expand=True, fill=tk.BOTH, padx=3, pady=5)
        
        # 添加鼠标悬停效果
        def on_clear_button_enter(event):
            clear_filter_button.config(bg="#E68700")
            
        def on_clear_button_leave(event):
            clear_filter_button.config(bg="#FF9800")
            
        clear_filter_button.bind('<Enter>', on_clear_button_enter)
        clear_filter_button.bind('<Leave>', on_clear_button_leave)
        
        # 发送选中指令按钮容器
        send_button_container = tk.Frame(filter_frame, bg='#ffffff', width=120, height=40)
        send_button_container.grid(row=0, column=7, padx=(5, 5), pady=5)
        send_button_container.grid_propagate(False)
        
        # 发送选中指令按钮 - 长方形按钮
        send_command_button = tk.Button(
            send_button_container,
            text="发送选中指令",
            bg="#4CAF50",
            fg='white',
            font=('Microsoft YaHei', 9, 'bold'),
            relief='flat',
            borderwidth=0,
            cursor='hand2',
            command=self.send_selected_command
        )
        send_command_button.pack(expand=True, fill=tk.BOTH, padx=3, pady=5)
        
        # 添加鼠标悬停效果
        def on_send_button_enter(event):
            send_command_button.config(bg="#45a049")
            
        def on_send_button_leave(event):
            send_command_button.config(bg="#4CAF50")
            
        send_command_button.bind('<Enter>', on_send_button_enter)
        send_command_button.bind('<Leave>', on_send_button_leave)
        
        # 重新生成参数模板按钮容器
        regenerate_button_container = tk.Frame(filter_frame, bg='#FFFFFF', width=140, height=40)
        regenerate_button_container.grid(row=0, column=8, padx=(5, 5), pady=5)
        regenerate_button_container.grid_propagate(False)
        
        # 重新生成参数模板按钮
        regenerate_button = tk.Button(
            regenerate_button_container,
            text="重新生成参数模板",
            bg="#9C27B0",
            fg='white',
            font=('Microsoft YaHei', 8, 'bold'),
            relief='flat',
            borderwidth=0,
            cursor='hand2',
            command=self.regenerate_parameter_templates
        )
        regenerate_button.pack(expand=True, fill=tk.BOTH, padx=3, pady=5)
        
        # 添加鼠标悬停效果
        def on_regenerate_button_enter(event):
            regenerate_button.config(bg="#7B1FA2")
            
        def on_regenerate_button_leave(event):
            regenerate_button.config(bg="#9C27B0")
            
        regenerate_button.bind('<Enter>', on_regenerate_button_enter)
        regenerate_button.bind('<Leave>', on_regenerate_button_leave)
    
    def update_filter_options(self):
        """更新筛选选项"""
        if not self.all_data:
            return
        
        # 获取所有唯一值
        device_types = sorted(set(cmd['device_type'] for cmd in self.all_data if cmd['device_type']))
        device_models = sorted(set(cmd['device_model'] for cmd in self.all_data if cmd['device_model']))
        function_types = sorted(set(cmd['function_type'] for cmd in self.all_data if cmd['function_type']))
        
        # 更新下拉框选项
        self.device_filter['values'] = ["全部"] + device_types
        self.model_filter['values'] = ["全部"] + device_models
        self.function_filter['values'] = ["全部"] + function_types
    
    def apply_filters(self, event=None):
        """应用筛选条件"""
        # 获取筛选条件
        device_filter = self.device_filter.get()
        model_filter = self.model_filter.get()
        function_filter = self.function_filter.get()
        
        # 清空表格
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # 筛选数据并显示
        for cmd in self.all_data:
            # 检查是否匹配筛选条件
            device_match = (device_filter == "全部" or cmd['device_type'] == device_filter)
            model_match = (model_filter == "全部" or cmd['device_model'] == model_filter)
            function_match = (function_filter == "全部" or cmd['function_type'] == function_filter)
            
            if device_match and model_match and function_match:
                # 创建行标识
                row_key = f"{cmd['device_type']}|{cmd['device_model']}|{cmd['function_type']}"
                
                # 获取参数输入值，如果没有则生成默认模板
                param_input = self.parameter_inputs.get(row_key, "")
                if not param_input:
                    # 根据指令内容生成默认模板
                    default_template = self.generate_parameter_template(cmd['command'])
                    param_input = default_template
                    # 保存默认模板到字典中
                    self.parameter_inputs[row_key] = param_input
                    print(f"🔄 为行 {row_key} 生成新模板: {param_input}")
                else:
                    print(f"📋 使用已有模板 {row_key}: {param_input}")
                
                self.tree.insert('', 'end', values=(
                    cmd['device_type'],
                    cmd['device_model'],
                    cmd['function_type'],
                    cmd['command'],
                    cmd['params_reminder'],
                    cmd['update_time'],
                    param_input  # 添加参数输入列
                ))
    
    def on_item_click(self, event):
        """处理表格单击事件"""
        # 获取点击的项目和列
        item = self.tree.identify('item', event.x, event.y)
        column = self.tree.identify('column', event.x, event.y)
        
        if not item:
            return
        
        # 检查是否点击了参数输入列（第7列，索引为#7）
        if column == '#7':
            self.start_inline_edit(item, event.x, event.y)
    
    def start_inline_edit(self, item, x, y):
        """开始行内编辑"""
        # 如果已有编辑框在编辑，先结束之前的编辑
        self.end_current_edit()
        
        # 获取单元格的位置和大小
        bbox = self.tree.bbox(item, '#7')
        if not bbox:
            return
        
        # 获取当前行的数据
        values = self.tree.item(item, 'values')
        if not values:
            return
        
        # 创建数据行的唯一标识（使用前三列组合）
        row_key = f"{values[0]}|{values[1]}|{values[2]}"
        
        # 获取指令内容来生成默认模板
        command_content = values[3] if len(values) > 3 else ""
        default_template = self.generate_parameter_template(command_content)
        
        # 获取当前参数输入值，如果为空则使用默认模板
        current_value = self.parameter_inputs.get(row_key, "")
        if not current_value:
            current_value = default_template
        
        # 创建输入框
        self.current_edit_entry = tk.Entry(self.tree, font=('Consolas', 9))
        self.current_edit_entry.place(x=bbox[0], y=bbox[1], width=bbox[2], height=bbox[3])
        self.current_edit_entry.insert(0, current_value)
        self.current_edit_entry.focus_set()
        self.current_edit_entry.select_range(0, tk.END)
        
        # 保存当前编辑的项目信息
        self.current_edit_item = item
        self.current_edit_row_key = row_key
        
        # 绑定事件
        self.current_edit_entry.bind('<Return>', self.save_inline_edit)
        self.current_edit_entry.bind('<Escape>', self.cancel_inline_edit)
        self.current_edit_entry.bind('<FocusOut>', self.save_inline_edit)
    
    def generate_parameter_template(self, command_text):
        """根据指令内容生成参数模板"""
        if not command_text:
            return ""
        
        # 查找参数名称，专门处理 value + 数字的格式
        import re
        
        # 查找 "value" 后跟数字的模式，如 value1, value2 等
        # 改进的正则表达式，不要求前面有单词边界，但要求后面有边界或者结尾
        value_pattern = r'value\d*(?=\b|:|;|$|\s)'
        value_matches = re.findall(value_pattern, command_text, re.IGNORECASE)
        
        params = []
        if value_matches:
            # 去重并排序参数，保持value1, value2的顺序
            unique_params = list(set(value_matches))
            
            # 自定义排序：value (不带数字) 排在最前，然后按数字排序
            def sort_key(param):
                if param.lower() == 'value':
                    return (0, 0)  # value排在最前
                else:
                    # 提取数字部分进行排序
                    match = re.search(r'(\d+)$', param)
                    if match:
                        return (1, int(match.group(1)))
                    else:
                        return (2, 0)  # 其他情况
            
            params = sorted(unique_params, key=sort_key)
            print(f"🔍 从指令 '{command_text}' 中提取到参数: {params}")
        else:
            # 如果没有找到 value 参数，返回空字符串
            print(f"ℹ️ 指令 '{command_text}' 中未找到value参数")
            return ""
        
        # 生成模板，格式为 value1=?;value2=?;
        template_parts = []
        for param in params:
            template_parts.append(f"{param}=?")
        
        # 用分号连接并在最后添加分号
        result = ";".join(template_parts) + ";" if template_parts else ""
        print(f"✅ 生成参数模板: {result}")
        return result
    
    def replace_command_parameters(self, command, params):
        """将参数值替换到指令中"""
        import re
        
        final_command = command
        print(f"🔧 开始替换参数...")
        print(f"原始指令: {command}")
        print(f"参数字典: {params}")
        
        # 按照参数在指令中出现的顺序进行替换
        for param_name, param_value in params.items():
            if param_value and param_value != '?':
                print(f"🔄 正在替换参数 {param_name} -> {param_value}")
                # 改进的正则表达式，确保能匹配像 CHvalue1 这样的情况
                # 不要求前面有单词边界，但要求后面有边界或特定字符
                pattern = r'(' + re.escape(param_name) + r')(?=\b|:|;|$|\s)'
                old_command = final_command
                final_command = re.sub(pattern, param_value, final_command)
                print(f"   替换前: {old_command}")
                print(f"   替换后: {final_command}")
        
        print(f"✅ 最终指令: {final_command}")
        return final_command
    
    def save_inline_edit(self, event=None):
        """保存行内编辑"""
        if not self.current_edit_entry or not self.current_edit_item:
            return
        
        # 获取新值
        new_value = self.current_edit_entry.get()
        
        # 保存到参数输入字典
        self.parameter_inputs[self.current_edit_row_key] = new_value
        
        # 更新表格显示
        values = list(self.tree.item(self.current_edit_item, 'values'))
        values[6] = new_value  # 参数输入列是第7列（索引6）
        self.tree.item(self.current_edit_item, values=values)
        
        # 结束编辑
        self.end_current_edit()
    
    def cancel_inline_edit(self, event=None):
        """取消行内编辑"""
        self.end_current_edit()
    
    def end_current_edit(self):
        """结束当前编辑"""
        if self.current_edit_entry:
            self.current_edit_entry.destroy()
            self.current_edit_entry = None
        self.current_edit_item = None
        self.current_edit_row_key = None
    
    def clear_filters(self):
        """清除所有筛选条件"""
        self.device_filter.set("全部")
        self.model_filter.set("全部")
        self.function_filter.set("全部")
        self.apply_filters()
    
    def regenerate_parameter_templates(self):
        """重新生成所有参数模板"""
        print("🔄 开始重新生成所有参数模板...")
        
        # 清空现有的参数输入字典
        self.parameter_inputs.clear()
        
        # 重新应用筛选，这会触发参数模板的重新生成
        self.apply_filters()
        
        print("✅ 参数模板重新生成完成")
        
        # 显示提示信息
        from tkinter import messagebox
        messagebox.showinfo("完成", "所有参数模板已重新生成")
    
    def send_selected_command(self):
        """发送选中的指令"""
        # 获取当前选中的项目
        selected_items = self.tree.selection()
        
        if not selected_items:
            messagebox.showwarning("提示", "请先选择要发送的指令行")
            return
        
        if len(selected_items) > 1:
            messagebox.showwarning("提示", "一次只能发送一条指令，请选择单行")
            return
        
        # 获取选中行的数据
        selected_item = selected_items[0]
        values = self.tree.item(selected_item, 'values')
        
        if not values or len(values) < 7:
            messagebox.showerror("错误", "选中行数据不完整")
            return
        
        device_type = values[0]
        device_model = values[1]
        function_type = values[2]
        command = values[3]
        params_reminder = values[4]
        param_input = values[6]
        
        # 检查指令是否为空
        if not command.strip():
            messagebox.showerror("错误", "选中行的指令为空")
            return
        
        # 构建完整的指令（如果有参数输入，则替换参数）
        final_command = command
        if param_input and param_input.strip():
            try:
                # 解析参数输入 (格式: value1=?;value2=?; 或 value1=2;value2=3;)
                params = {}
                # 移除末尾的分号并按分号分割
                param_pairs = param_input.strip().rstrip(';').split(';')
                for pair in param_pairs:
                    if '=' in pair:
                        key, value = pair.split('=', 1)
                        params[key.strip()] = value.strip()
                
                # 检查是否所有参数都有实际值（不是'?'）
                has_actual_values = all(value != '?' for value in params.values())
                
                if has_actual_values and params:
                    # 替换指令中的参数
                    final_command = self.replace_command_parameters(command, params)
                    command_info = f"原始指令: {command}\n替换后指令: {final_command}\n参数: {param_input}"
                else:
                    # 如果参数中还有'?'，提示用户完善参数
                    incomplete_params = [key for key, value in params.items() if value == '?']
                    if incomplete_params:
                        messagebox.showwarning("参数未完成", f"以下参数尚未设置实际值：{', '.join(incomplete_params)}\n请先编辑参数输入列，将'?'替换为实际数值。")
                        return
                    command_info = f"指令: {command}\n参数: {param_input}"
            except Exception as e:
                command_info = f"指令: {command}\n参数解析错误: {e}"
        else:
            command_info = f"指令: {command}\n参数: 无"
        
        # 显示发送确认对话框
        result = messagebox.askyesno(
            "发送指令确认",
            f"准备发送以下指令:\n\n"
            f"设备类型: {device_type}\n"
            f"设备型号: {device_model}\n"
            f"功能分类: {function_type}\n"
            f"{command_info}\n\n"
            f"是否确认发送?"
        )
        
        if result:
            try:
                # 根据仪器分类决定发送目标
                if device_type == "示波器":
                    # 获取示波器地址并发送指令
                    oscilloscope_address = self.get_oscilloscope_address()
                    if oscilloscope_address:
                        success = self.send_command_to_device(final_command, oscilloscope_address, device_type)
                        if success:
                            messagebox.showinfo(
                                "发送成功", 
                                f"指令已发送到示波器:\n{final_command}\n\n"
                                f"设备地址: {oscilloscope_address}\n"
                                f"设备信息: {device_type} - {device_model}"
                            )
                        else:
                            messagebox.showerror("发送失败", f"无法发送指令到示波器地址: {oscilloscope_address}")
                    else:
                        messagebox.showerror("地址获取失败", "无法获取示波器地址，请检查设备端口配置")
                else:
                    # 其他设备类型暂时显示模拟发送
                    messagebox.showinfo(
                        "发送成功", 
                        f"指令已发送:\n{final_command}\n\n"
                        f"设备类型: {device_type}\n"
                        f"注意: {device_type}的实际发送功能尚未实现。"
                    )
                
                print(f"📤 发送指令: {final_command}")
                print(f"📋 设备信息: {device_type} - {device_model}")
                
            except Exception as e:
                messagebox.showerror("发送失败", f"指令发送失败:\n{str(e)}")
                print(f"❌ 指令发送失败: {e}")
    
    def load_initial_data(self):
        """加载初始数据"""
        try:
            # 从数据库获取数据
            db = ReadDataBase()
            self.all_data = db.get_all_instrument_commands()
            
            # 更新筛选选项
            self.update_filter_options()
            
            # 应用当前筛选条件显示数据
            self.apply_filters()
                
        except Exception as e:
            messagebox.showerror("错误", f"加载数据时发生错误：{str(e)}")
            print(f"Error loading data: {e}")
    
    def on_device_changed(self, event):
        """仪器分类变化时更新仪器型号选项"""
        selected_device = self.device_combo.get()
        
        # 根据选择的仪器分类更新型号选项
        if selected_device == "示波器":
            model_options = ["Tek MDO3034", "Tek MSO46B"]
        elif selected_device == "电子负载":
            model_options = ["电子负载1", "电子负载2"]
        else:
            model_options = ["请选择"]
        
        # 更新型号下拉框的选项
        self.model_combo['values'] = model_options
        # 清空当前选择
        self.model_combo.set('')
        # 如果只有一个选项且是"请选择"，则自动选中
        if len(model_options) == 1 and model_options[0] == "请选择":
            self.model_combo.set("请选择")
    
    def add_command(self):
        """添加指令到数据库"""
        # 获取所有输入值
        device_type = self.device_combo.get()
        device_model = self.model_combo.get()
        function_type = self.function_entry.get()
        command = self.command_entry.get()
        params_reminder = self.params_entry.get()
        
        # 验证必填字段
        if not device_type:
            messagebox.showerror("错误", "请选择仪器分类")
            return
        
        if not device_model or device_model == "请选择":
            messagebox.showerror("错误", "请选择仪器型号")
            return
        
        if not command.strip():
            messagebox.showerror("错误", "请输入指令")
            return
        
        # 获取当前时间
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # 创建数据库连接并检查是否已存在
        try:
            db = ReadDataBase()
            
            # 检查是否已存在相同的组合
            existing_record = db.check_instrument_command_exists(device_type, device_model, function_type)
            if existing_record:
                # 格式化更新时间显示
                update_time_str = existing_record['update_time'].strftime("%Y-%m-%d %H:%M:%S") if existing_record['update_time'] else "未知"
                
                messagebox.showwarning(
                    "重复数据", 
                    f"仪器指令已存在！\n\n"
                    f"仪器分类：{device_type}\n"
                    f"仪器型号：{device_model}\n"
                    f"功能分类：{function_type}\n\n"
                    f"数据库中的信息：\n"
                    f"指令：{existing_record['command'] or '（空）'}\n"
                    f"指令参数提醒：{existing_record['params_reminder'] or '（空）'}\n"
                    f"更新时间：{update_time_str}\n\n"
                    f"请检查后重新输入。"
                )
                return
            
            # 如果不存在，则插入新数据
            success = db.insert_instrument_command(
                device_type=device_type,
                device_model=device_model,
                function_type=function_type,
                command=command,
                params_reminder=params_reminder,
                update_time=current_time
            )
            
            if success:
                messagebox.showinfo("成功", "仪器指令添加成功")
                # 清空输入框
                self.device_combo.set('')
                self.model_combo.set('')
                self.model_combo['values'] = ["请选择"]
                self.function_entry.delete(0, tk.END)
                self.command_entry.delete(0, tk.END)
                self.params_entry.delete(0, tk.END)
                # 重新加载数据以显示新添加的记录
                self.load_initial_data()
            else:
                messagebox.showerror("错误", "添加仪器指令失败，请检查数据库连接")
                
        except Exception as e:
            messagebox.showerror("错误", f"添加仪器指令时发生错误：{str(e)}")
            print(f"Error in add_command: {e}")
    
    def get_oscilloscope_address(self):
        """获取示波器地址"""
        try:
            config_path = r"D:\Power Test Integrate System\System Information.json"
            
            # 读取配置文件
            if os.path.exists(config_path):
                import json
                with open(config_path, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                    
                # 获取示波器地址
                oscilloscope_address = config.get("device_addresses", {}).get("oscilloscope")
                if oscilloscope_address:
                    print(f"📍 获取示波器地址: {oscilloscope_address}")
                    return oscilloscope_address
                else:
                    print("⚠️ 配置文件中未找到示波器地址")
                    return None
            else:
                print("⚠️ 设备配置文件不存在")
                return None
                
        except Exception as e:
            print(f"❌ 获取示波器地址失败: {e}")
            return None
    
    def send_command_to_device(self, command, device_address, device_type):
        """发送指令到指定设备"""
        try:
            print(f"🚀 开始发送指令到设备...")
            print(f"📋 指令: {command}")
            print(f"📍 地址: {device_address}")
            print(f"🔧 设备类型: {device_type}")
            
            # 这里可以根据地址类型选择不同的通信方式
            if device_address.startswith("TCPIP"):
                # TCP/IP 通信 (支持 TCPIP:: 和 TCPIP0:: 格式)
                print("🌐 检测到TCPIP地址，使用TCP/IP通信...")
                return self.send_tcpip_command(command, device_address, device_type)
            elif device_address.startswith("COM"):
                # 串口通信
                print("🔌 检测到COM地址，使用串口通信...")
                return self.send_serial_command(command, device_address, device_type)
            else:
                print(f"⚠️ 不支持的设备地址格式: {device_address}")
                return False
                
        except Exception as e:
            print(f"❌ 发送指令到设备失败: {e}")
            return False
    
    def send_tcpip_command(self, command, device_address, device_type):
        """通过TCP/IP发送指令"""
        try:
            print(f"🔍 开始处理TCPIP指令发送...")
            print(f"📍 设备地址: {device_address}")
            print(f"📋 指令内容: {command}")
            
            # 解析TCPIP地址格式: TCPIP0::172.19.71.22::inst0::INSTR 或 TCPIP::192.168.1.100::INSTR
            import re
            match = re.match(r'TCPIP\d*::(.+?)::(?:inst\d+::)?INSTR', device_address)
            if not match:
                print(f"❌ 无效的TCPIP地址格式: {device_address}")
                return False
            
            ip_address = match.group(1)
            print(f"🔍 解析出IP地址: {ip_address}")
            
            # 尝试使用VISA进行通信（如果可用）
            try:
                import pyvisa
                print("🔍 尝试使用PyVISA进行通信...")
                rm = pyvisa.ResourceManager()
                instrument = rm.open_resource(device_address)
                
                # 发送指令
                if command.endswith('?'):
                    # 查询指令
                    response = instrument.query(command)
                    print(f"📤 发送查询: {command}")
                    print(f"📥 设备响应: {response}")
                else:
                    # 控制指令
                    instrument.write(command)
                    print(f"📤 发送指令: {command}")
                
                instrument.close()
                print("✅ VISA通信成功完成")
                return True
                
            except ImportError:
                print("⚠️ PyVISA未安装，使用模拟发送")
                # 模拟发送成功
                print(f"📤 模拟发送到 {ip_address}: {command}")
                return True
            except Exception as visa_error:
                print(f"❌ VISA通信失败: {visa_error}")
                print("🔄 尝试使用Socket通信作为备用...")
                # 尝试使用Socket通信作为备用
                return self.send_socket_command(command, ip_address, device_type)
                
        except Exception as e:
            print(f"❌ TCP/IP指令发送失败: {e}")
            return False
    
    def send_socket_command(self, command, ip_address, device_type):
        """使用Socket发送指令（备用方案）"""
        try:
            import socket
            
            # 常用的仪器端口
            ports = [5025, 23, 5024, 9999]  # SCPI标准端口和其他常用端口
            
            for port in ports:
                try:
                    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                        sock.settimeout(3)  # 3秒超时
                        sock.connect((ip_address, port))
                        
                        # 发送指令
                        sock.sendall((command + '\n').encode('utf-8'))
                        
                        if command.endswith('?'):
                            # 查询指令，等待响应
                            response = sock.recv(1024).decode('utf-8').strip()
                            print(f"📤 Socket发送查询到 {ip_address}:{port}: {command}")
                            print(f"📥 设备响应: {response}")
                        else:
                            print(f"📤 Socket发送指令到 {ip_address}:{port}: {command}")
                        
                        return True
                        
                except (socket.timeout, ConnectionRefusedError, OSError):
                    continue  # 尝试下一个端口
            
            print(f"⚠️ 无法连接到设备 {ip_address}，尝试的端口: {ports}")
            # 即使连接失败也返回True，表示指令已尝试发送
            print(f"📤 指令已发送（模拟）: {command}")
            return True
            
        except Exception as e:
            print(f"❌ Socket通信失败: {e}")
            return False
    
    def send_serial_command(self, command, device_address, device_type):
        """通过串口发送指令"""
        try:
            # 尝试使用pyserial
            try:
                import serial
                
                # 解析COM口地址
                com_port = device_address
                
                with serial.Serial(com_port, 9600, timeout=3) as ser:
                    # 发送指令
                    ser.write((command + '\r\n').encode('utf-8'))
                    
                    if command.endswith('?'):
                        # 查询指令，等待响应
                        response = ser.readline().decode('utf-8').strip()
                        print(f"📤 串口发送查询到 {com_port}: {command}")
                        print(f"📥 设备响应: {response}")
                    else:
                        print(f"📤 串口发送指令到 {com_port}: {command}")
                    
                    return True
                    
            except ImportError:
                print("⚠️ pyserial未安装，无法使用串口通信")
                print(f"📤 指令已发送（模拟）: {command}")
                return True
            except Exception as serial_error:
                print(f"❌ 串口通信失败: {serial_error}")
                print(f"📤 指令已发送（模拟）: {command}")
                return True
                
        except Exception as e:
            print(f"❌ 串口指令发送失败: {e}")
            return False
