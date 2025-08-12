"""
圆角矩形按钮组件
现代化的圆角矩形按钮设计
"""
import tkinter as tk
import math

class RoundedRectangleButton:
    """圆角矩形按钮"""
    
    def __init__(self, parent, text="", width=120, height=45, 
                 corner_radius=12, 
                 bg_color='#4a90e2', fg_color='white',
                 hover_bg='#357abd', hover_fg='white',
                 active_bg='#ffffff', active_fg='#4a90e2',
                 font=('Microsoft YaHei', 11, 'bold'),
                 command=None):
        
        self.parent = parent
        self.text = text
        self.width = width
        self.height = height
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
        self.is_active = False
        
        self.create_button()
        self.bind_events()
    
    def create_button(self):
        """创建按钮"""
        # 获取父组件背景色
        try:
            parent_bg = self.parent.cget('bg')
        except:
            parent_bg = '#f5f5f5'
            
        # 创建Canvas，留出一些边距
        canvas_width = self.width + 10
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
        """绘制圆角矩形按钮"""
        # 清除之前的绘制
        self.canvas.delete("all")
        
        # 根据状态选择颜色
        if self.is_active:
            fill_color = self.active_bg
            text_color = self.active_fg
            outline_color = '#4a90e2'
            outline_width = 2
        elif self.state == 'hover':
            fill_color = self.hover_bg
            text_color = self.hover_fg
            outline_color = '#333333'
            outline_width = 1
        else:
            fill_color = self.bg_color
            text_color = self.fg_color
            outline_color = '#333333'
            outline_width = 1
        
        # 计算圆角矩形位置（居中）
        offset_x = 5
        offset_y = 5
        x1 = offset_x
        y1 = offset_y
        x2 = offset_x + self.width
        y2 = offset_y + self.height
        
        # 绘制圆角矩形
        self.draw_rounded_rectangle(x1, y1, x2, y2, self.corner_radius, 
                                   fill_color, outline_color, outline_width)
        
        # 绘制文本
        text_x = offset_x + self.width // 2
        text_y = offset_y + self.height // 2
        
        self.text_id = self.canvas.create_text(
            text_x, text_y,
            text=self.text,
            font=self.font,
            fill=text_color,
            anchor='center'
        )
    
    def draw_rounded_rectangle(self, x1, y1, x2, y2, radius, fill_color, outline_color, outline_width):
        """绘制圆角矩形"""
        # 确保半径不超过矩形的一半
        max_radius = min((x2 - x1) // 2, (y2 - y1) // 2)
        radius = min(radius, max_radius)
        
        # 创建圆角矩形的路径
        points = []
        
        # 右上角圆弧
        for i in range(0, 91, 5):  # 90度圆弧，每5度一个点
            angle = math.radians(i)
            x = x2 - radius + radius * math.cos(angle)
            y = y1 + radius - radius * math.sin(angle)
            points.extend([x, y])
        
        # 右下角圆弧
        for i in range(0, 91, 5):
            angle = math.radians(i)
            x = x2 - radius + radius * math.sin(angle)
            y = y2 - radius + radius * math.cos(angle)
            points.extend([x, y])
        
        # 左下角圆弧
        for i in range(0, 91, 5):
            angle = math.radians(i)
            x = x1 + radius - radius * math.cos(angle)
            y = y2 - radius + radius * math.sin(angle)
            points.extend([x, y])
        
        # 左上角圆弧
        for i in range(0, 91, 5):
            angle = math.radians(i)
            x = x1 + radius - radius * math.sin(angle)
            y = y1 + radius - radius * math.cos(angle)
            points.extend([x, y])
        
        # 绘制填充的多边形
        self.shape_id = self.canvas.create_polygon(
            points,
            fill=fill_color,
            outline=outline_color,
            width=outline_width,
            smooth=True
        )
    
    def bind_events(self):
        """绑定事件"""
        self.canvas.bind("<Button-1>", self.on_click)
        self.canvas.bind("<Enter>", self.on_enter)
        self.canvas.bind("<Leave>", self.on_leave)
        
        # 为了让鼠标悬停效果更好，也绑定所有子元素
        self.canvas.tag_bind(self.shape_id, "<Button-1>", self.on_click)
        self.canvas.tag_bind(self.shape_id, "<Enter>", self.on_enter)
        self.canvas.tag_bind(self.shape_id, "<Leave>", self.on_leave)
    
    def on_click(self, event=None):
        """点击事件"""
        if self.command:
            self.command()
    
    def on_enter(self, event=None):
        """鼠标进入"""
        if not self.is_active:
            self.state = 'hover'
            self.draw_button()
            self.canvas.configure(cursor='hand2')
    
    def on_leave(self, event=None):
        """鼠标离开"""
        if not self.is_active:
            self.state = 'normal'
            self.draw_button()
            self.canvas.configure(cursor='')
    
    def set_active(self, active):
        """设置激活状态"""
        self.is_active = active
        self.state = 'active' if active else 'normal'
        self.draw_button()
    
    def pack(self, **kwargs):
        """包装pack方法"""
        self.canvas.pack(**kwargs)
    
    def grid(self, **kwargs):
        """包装grid方法"""
        self.canvas.grid(**kwargs)
    
    def place(self, **kwargs):
        """包装place方法"""
        self.canvas.place(**kwargs)
    
    def configure(self, **kwargs):
        """配置按钮属性"""
        if 'text' in kwargs:
            self.text = kwargs['text']
        if 'bg_color' in kwargs:
            self.bg_color = kwargs['bg_color']
        if 'fg_color' in kwargs:
            self.fg_color = kwargs['fg_color']
        if 'command' in kwargs:
            self.command = kwargs['command']
        
        # 重新绘制按钮
        self.draw_button()
    
    def destroy(self):
        """销毁按钮"""
        if self.canvas:
            self.canvas.destroy()
