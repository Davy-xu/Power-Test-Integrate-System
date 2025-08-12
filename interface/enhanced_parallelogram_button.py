"""
增强版圆角平行四边形按钮
解决显示问题，使用更明显的样式
"""
import tkinter as tk
import math

class EnhancedParallelogramButton:
    """增强版圆角平行四边形按钮"""
    
    def __init__(self, parent, text="", width=120, height=45, 
                 skew=15, corner_radius=8, 
                 bg_color='#4a90e2', fg_color='white',
                 hover_bg='#357abd', hover_fg='white',
                 active_bg='#ffffff', active_fg='#4a90e2',
                 font=('Microsoft YaHei', 11, 'bold'),
                 command=None):
        
        self.parent = parent
        self.text = text
        self.width = width
        self.height = height
        self.skew = skew
        self.corner_radius = corner_radius
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.hover_bg = hover_bg
        self.hover_fg = hover_fg
        self.active_bg = active_bg
        self.active_fg = active_fg
        self.font = font
        self.command = command
        
        self.state = 'normal'
        self.canvas = None
        self.shape_id = None
        self.text_id = None
        self.border_id = None
        
        self.create_button()
        self.bind_events()
    
    def create_button(self):
        """创建按钮"""
        # 获取父组件背景色
        try:
            parent_bg = self.parent.cget('bg')
        except:
            parent_bg = '#f5f5f5'
            
        # 创建Canvas，尺寸稍大以容纳倾斜效果
        canvas_width = self.width + abs(self.skew) + 10
        canvas_height = self.height + 10
        
        self.canvas = tk.Canvas(
            self.parent,
            width=canvas_width,
            height=canvas_height,
            highlightthickness=0,
            bd=0,
            relief='flat',
            bg=parent_bg
        )
        
        self.draw_button()
    
    def draw_button(self):
        """绘制按钮"""
        # 清除之前的绘制
        self.canvas.delete("all")
        
        # 根据状态选择颜色
        if self.state == 'active':
            fill_color = self.active_bg
            text_color = self.active_fg
        elif self.state == 'hover':
            fill_color = self.hover_bg
            text_color = self.hover_fg
        else:
            fill_color = self.bg_color
            text_color = self.fg_color
        
        # 计算平行四边形顶点（偏移以居中）
        offset_x = 5
        offset_y = 5
        
        # 平行四边形的四个顶点
        x1 = offset_x + self.skew
        y1 = offset_y
        x2 = offset_x + self.width + self.skew
        y2 = offset_y
        x3 = offset_x + self.width
        y3 = offset_y + self.height
        x4 = offset_x
        y4 = offset_y + self.height
        
        points = [x1, y1, x2, y2, x3, y3, x4, y4]
        
        # 绘制主形状
        self.shape_id = self.canvas.create_polygon(
            points,
            fill=fill_color,
            outline='#333333',
            width=2,
            smooth=True
        )
        
        # 绘制文本
        text_x = offset_x + (self.width + self.skew) // 2
        text_y = offset_y + self.height // 2
        
        self.text_id = self.canvas.create_text(
            text_x, text_y,
            text=self.text,
            font=self.font,
            fill=text_color,
            anchor='center'
        )
        
        # 重新绑定事件
        self.bind_shape_events()
    
    def bind_events(self):
        """绑定基础事件"""
        self.canvas.bind('<Button-1>', self.on_click)
        self.canvas.bind('<Enter>', self.on_enter)
        self.canvas.bind('<Leave>', self.on_leave)
    
    def bind_shape_events(self):
        """绑定形状事件"""
        if self.shape_id:
            self.canvas.tag_bind(self.shape_id, '<Button-1>', self.on_click)
        if self.text_id:
            self.canvas.tag_bind(self.text_id, '<Button-1>', self.on_click)
    
    def on_click(self, event):
        """点击事件"""
        if self.command:
            self.command()
    
    def on_enter(self, event):
        """鼠标进入"""
        if self.state != 'active':
            self.state = 'hover'
            self.draw_button()
            self.canvas.configure(cursor='hand2')
    
    def on_leave(self, event):
        """鼠标离开"""
        if self.state != 'active':
            self.state = 'normal'
            self.draw_button()
            self.canvas.configure(cursor='')
    
    def set_active(self, active=True):
        """设置激活状态"""
        self.state = 'active' if active else 'normal'
        self.draw_button()
    
    def pack(self, **kwargs):
        """布局方法"""
        self.canvas.pack(**kwargs)
    
    def place(self, **kwargs):
        """位置布局方法"""
        self.canvas.place(**kwargs)
    
    def grid(self, **kwargs):
        """网格布局方法"""
        self.canvas.grid(**kwargs)
