"""
样式配置模块
负责设置界面的深色主题样式
"""
from tkinter import ttk


class StyleManager:
    """样式管理器"""
    
    def __init__(self):
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.setup_styles()
    
    def setup_styles(self):
        """设置深色主题样式"""
        # 配置主框架 - 调整为浅色主题以匹配浏览器标签样式
        self.style.configure('Dark.TFrame', background='#f5f5f5')
        
        # 配置选项卡容器样式 - 类似浏览器标签的现代样式
        self.style.configure('Sidebar.TNotebook', 
                           background='#f0f0f0',  # 浅灰色背景，类似截图
                           borderwidth=0,
                           tabposition='n')  # north，选项卡在顶部，类似浏览器
        
        # 配置选项卡标签样式 - 圆角浏览器标签效果
        self.style.configure('Sidebar.TNotebook.Tab',
                           background='#e8e8e8',    # 浅灰色背景
                           foreground='#333333',    # 深色文字
                           padding=[20, 8, 20, 8],  # 左、上、右、下内边距
                           borderwidth=1,
                           relief='raised',         # 凸起效果
                           font=('Microsoft YaHei', 11, 'normal'),
                           focuscolor='none')       # 去除焦点边框
        
        # 配置选项卡状态映射 - 模拟浏览器标签的交互效果
        self.style.map('Sidebar.TNotebook.Tab',
                     background=[('selected', '#ffffff'),    # 选中时白色底，突出显示
                                ('active', '#d0d0d0'),      # 悬停时更浅的灰色
                                ('!active', '#e8e8e8')],    # 未选中时默认浅灰色
                     foreground=[('selected', '#2c5aa0'),    # 选中时蓝色文字，类似截图
                                ('active', '#333333'),      # 悬停时深色文字
                                ('!active', '#666666')],    # 未选中时中灰色文字
                     relief=[('selected', 'flat'),          # 选中时平坦效果
                            ('active', 'raised'),          # 悬停时凸起效果
                            ('!active', 'flat')],          # 未选中时平坦效果
                     borderwidth=[('selected', 0),          # 选中时无边框
                                 ('active', 1),            # 悬停时显示边框
                                 ('!active', 1)])          # 未选中时显示边框
        
        # 配置标签样式 - 调整为浅色主题
        self.style.configure('Title.TLabel',
                           background='#f5f5f5',
                           foreground='#333333',
                           font=('Microsoft YaHei', 14, 'bold'))
        
        # 配置系统标题样式
        self.style.configure('System.Title.TLabel',
                           background='#f5f5f5',
                           foreground='#333333',
                           font=('Microsoft YaHei', 20, 'bold'),
                           anchor='center')
        
        self.style.configure('White.TLabel',
                           background='#2d2d2d',
                           foreground='white',
                           font=('Microsoft YaHei', 10))
        
        # 配置按钮样式
        self.style.configure('Dark.TButton',
                           background='#505050',
                           foreground='white',
                           font=('Microsoft YaHei', 10),
                           borderwidth=1,
                           relief='flat')
        
        self.style.map('Dark.TButton',
                     background=[('active', '#606060')])
        
        # 配置输入框样式
        self.style.configure('Dark.TEntry',
                           background='#404040',
                           foreground='white',
                           borderwidth=1,
                           relief='solid')
        
        # 配置橙色下拉框样式（用于仪器指令表格）
        self.style.configure('Orange.TCombobox',
                           background='#FF8C00',
                           foreground='black',
                           fieldbackground='#FFD700',
                           borderwidth=1,
                           relief='solid')
        
        self.style.map('Orange.TCombobox',
                     background=[('active', '#FFA500'),
                                ('readonly', '#FF8C00')])
        
        # 配置列表框样式
        self.style.configure('Dark.Treeview',
                           background='#404040',
                           foreground='white',
                           fieldbackground='#404040',
                           borderwidth=1,
                           relief='solid')
        
        self.style.configure('Dark.Treeview.Heading',
                           background='#505050',
                           foreground='white',
                           relief='flat')
        
        # 配置状态栏样式 - 调整为浅色主题
        self.style.configure('StatusBar.TFrame',
                           background='#e8e8e8',
                           relief='flat',
                           borderwidth=0)
        
        self.style.configure('StatusBar.TLabel',
                           background='#e8e8e8',
                           foreground='#333333',
                           font=('Microsoft YaHei', 11, 'normal'),
                           relief='flat')
