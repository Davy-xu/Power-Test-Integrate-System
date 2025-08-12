"""
圆角矩形按钮
现代化设计的圆角矩形按钮组件
"""
import tkinter as tk
import math

class RoundedRectButton:
    """圆角矩形按钮"""
    
    def __init__(self, parent, text="", width=120, height=45, 
                 corner_radius=12,
                 bg_color='#4a90e2', fg_color='white',
                 hover_bg='#357abd', hover_fg='white',
                 active_bg='#ffffff', active_fg='#4a90e2',
                 font=('Microsoft YaHei', 11, 'bold'),
                 border_color='#333333', border_width=2,
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
        self.border_color = border_color
        self.border_width = border_width
        self.command = command
        
        self.state = 'normal'
        self.canvas = None
        self.shape_id = None
        self.text_id = None
        
        self.create_button()
        self.bind_events()
    
    def create_button(self):
        """创建按钮"""
        # 获取父组件背景色
        try:
            parent_bg = self.parent.cget('bg')
        except:
            parent_bg = '#f5f5f5'
            
        # 创建Canvas，添加少量边距
        canvas_width = self.width + 6
        canvas_height = self.height + 6
        
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
        if self.state == 'active':
            fill_color = self.active_bg
            text_color = self.active_fg
        elif self.state == 'hover':
            fill_color = self.hover_bg
            text_color = self.hover_fg
        else:
            fill_color = self.bg_color
            text_color = self.fg_color
        
        # 计算位置（居中）
        offset_x = 3
        offset_y = 3
        
        # 绘制圆角矩形
        self.draw_rounded_rectangle(
            offset_x, offset_y,
            offset_x + self.width, offset_y + self.height,
            self.corner_radius,
            fill_color
        )
        
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
        
        # 重新绑定事件
        self.bind_shape_events()
    
    def draw_rounded_rectangle(self, x1, y1, x2, y2, radius, fill_color):
        """绘制圆角矩形"""
        # 确保半径不超过矩形的一半
        radius = min(radius, abs(x2-x1)//2, abs(y2-y1)//2)
        
        points = []
        
        # 右上角
        for i in range(0, 90, 5):
            angle = math.radians(i)
            x = x2 - radius + radius * math.cos(angle)
            y = y1 + radius - radius * math.sin(angle)
            points.extend([x, y])
        
        # 右下角
        for i in range(90, 180, 5):
            angle = math.radians(i)
            x = x2 - radius + radius * math.cos(angle)
            y = y2 - radius - radius * math.sin(angle)
            points.extend([x, y])
        
        # 左下角
        for i in range(180, 270, 5):
            angle = math.radians(i)
            x = x1 + radius + radius * math.cos(angle)
            y = y2 - radius - radius * math.sin(angle)
            points.extend([x, y])
        
        # 左上角
        for i in range(270, 360, 5):
            angle = math.radians(i)
            x = x1 + radius + radius * math.cos(angle)
            y = y1 + radius - radius * math.sin(angle)
            points.extend([x, y])
        
        # 创建圆角矩形
        self.shape_id = self.canvas.create_polygon(
            points,
            fill=fill_color,
            outline=self.border_color,
            width=self.border_width,
            smooth=True
        )
    
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

    def destroy(self):
        """销毁按钮"""
        if self.canvas:
            self.canvas.destroy()

# 为了兼容性，保持相同的接口
def create_button(parent, text="", width=120, height=45, 
                 bg_color='#4a90e2', fg_color='white',
                 hover_bg='#357abd', hover_fg='white',
                 command=None, **kwargs):
    """创建圆角矩形按钮的便捷函数"""
    return RoundedRectButton(
        parent=parent,
        text=text,
        width=width,
        height=height,
        bg_color=bg_color,
        fg_color=fg_color,
        hover_bg=hover_bg,
        hover_fg=hover_fg,
        command=command,
        **kwargs
    )
