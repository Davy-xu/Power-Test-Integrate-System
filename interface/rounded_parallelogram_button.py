"""
圆角平行四边形按钮组件
用于实现现代化的标签按钮效果
"""
import tkinter as tk
import math


class RoundedParallelogramButton:
    """圆角平行四边形按钮"""
    
    def __init__(self, parent, text="", width=120, height=45, 
                 skew=15, corner_radius=8, 
                 bg_color='#e8e8e8', fg_color='#666666',
                 hover_bg='#f0f0f0', hover_fg='#333333',
                 active_bg='#ffffff', active_fg='#2c5aa0',
                 font=('Microsoft YaHei', 11, 'normal'),
                 command=None):
        
        self.parent = parent
        self.text = text
        self.width = width
        self.height = height
        self.skew = skew  # 平行四边形倾斜度
        self.corner_radius = corner_radius
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.hover_bg = hover_bg
        self.hover_fg = hover_fg
        self.active_bg = active_bg
        self.active_fg = active_fg
        self.font = font
        self.command = command
        
        self.state = 'normal'  # normal, hover, active
        self.canvas = None
        self.text_id = None
        self.shape_id = None
        
        self.create_button()
        self.bind_events()
    
    def create_button(self):
        """创建画布按钮"""
        # 获取父组件背景色
        try:
            parent_bg = self.parent.cget('bg')
        except:
            parent_bg = '#f5f5f5'
            
        self.canvas = tk.Canvas(
            self.parent, 
            width=self.width + self.skew, 
            height=self.height,
            highlightthickness=0,
            bd=0,
            relief='flat',
            bg=parent_bg
        )
        
        self.draw_shape()
        self.draw_text()
    
    def draw_shape(self):
        """绘制圆角平行四边形"""
        if self.shape_id:
            self.canvas.delete(self.shape_id)
        
        # 根据状态选择颜色
        if self.state == 'active':
            fill_color = self.active_bg
        elif self.state == 'hover':
            fill_color = self.hover_bg
        else:
            fill_color = self.bg_color
        
        # 计算平行四边形的顶点
        points = self.calculate_parallelogram_points()
        
        # 绘制平行四边形（先绘制基本形状）
        self.shape_id = self.canvas.create_polygon(
            points,
            fill=fill_color,
            outline=fill_color,
            width=0,
            smooth=True
        )
        
        # 绘制圆角效果（在四个角添加圆角）
        self.add_rounded_corners(fill_color)
        
        # 重新绑定事件
        if self.shape_id:
            self.canvas.tag_bind(self.shape_id, '<Button-1>', self.on_click)
    
    def calculate_parallelogram_points(self):
        """计算平行四边形顶点"""
        # 平行四边形的四个顶点
        # 左上角向右倾斜
        x1, y1 = self.skew, 0
        x2, y2 = self.width + self.skew, 0
        x3, y3 = self.width, self.height
        x4, y4 = 0, self.height
        
        return [x1, y1, x2, y2, x3, y3, x4, y4]
    
    def add_rounded_corners(self, fill_color):
        """添加圆角效果"""
        radius = self.corner_radius
        
        # 获取平行四边形的四个角的位置
        corners = [
            (self.skew, 0),  # 左上
            (self.width + self.skew, 0),  # 右上
            (self.width, self.height),  # 右下
            (0, self.height)  # 左下
        ]
        
        # 在每个角添加小的圆形来模拟圆角
        for i, (x, y) in enumerate(corners):
            if i == 0:  # 左上角
                self.canvas.create_oval(
                    x - radius//2, y - radius//2, 
                    x + radius//2, y + radius//2,
                    fill=fill_color, outline=fill_color
                )
            elif i == 1:  # 右上角
                self.canvas.create_oval(
                    x - radius//2, y - radius//2, 
                    x + radius//2, y + radius//2,
                    fill=fill_color, outline=fill_color
                )
            elif i == 2:  # 右下角
                self.canvas.create_oval(
                    x - radius//2, y - radius//2, 
                    x + radius//2, y + radius//2,
                    fill=fill_color, outline=fill_color
                )
            else:  # 左下角
                self.canvas.create_oval(
                    x - radius//2, y - radius//2, 
                    x + radius//2, y + radius//2,
                    fill=fill_color, outline=fill_color
                )
    
    def draw_text(self):
        """绘制文字"""
        if self.text_id:
            self.canvas.delete(self.text_id)
        
        # 根据状态选择文字颜色
        if self.state == 'active':
            text_color = self.active_fg
        elif self.state == 'hover':
            text_color = self.hover_fg
        else:
            text_color = self.fg_color
        
        # 文字位置（平行四边形的中心）
        text_x = (self.width + self.skew) // 2
        text_y = self.height // 2
        
        self.text_id = self.canvas.create_text(
            text_x, text_y,
            text=self.text,
            font=self.font,
            fill=text_color,
            anchor='center'
        )
        
        # 重新绑定事件
        if self.text_id:
            self.canvas.tag_bind(self.text_id, '<Button-1>', self.on_click)
    
    def bind_events(self):
        """绑定事件"""
        self.canvas.bind('<Button-1>', self.on_click)
        self.canvas.bind('<Enter>', self.on_enter)
        self.canvas.bind('<Leave>', self.on_leave)
        self.canvas.bind('<Motion>', self.on_motion)
        
        # 确保所有图形元素都绑定了事件
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
            self.draw_shape()
            self.draw_text()
            self.canvas.configure(cursor='hand2')
    
    def on_leave(self, event):
        """鼠标离开"""
        if self.state != 'active':
            self.state = 'normal'
            self.draw_shape()
            self.draw_text()
            self.canvas.configure(cursor='')
    
    def on_motion(self, event):
        """鼠标移动"""
        # 检查鼠标是否在按钮区域内
        x, y = event.x, event.y
        if self.is_point_in_parallelogram(x, y):
            if self.state == 'normal':
                self.on_enter(event)
        else:
            if self.state == 'hover':
                self.on_leave(event)
    
    def is_point_in_parallelogram(self, x, y):
        """检查点是否在平行四边形内"""
        points = self.calculate_parallelogram_points()
        
        # 简化的点在多边形内检测
        # 使用边界框检测
        min_x = min(points[::2])
        max_x = max(points[::2])
        min_y = min(points[1::2])
        max_y = max(points[1::2])
        
        return min_x <= x <= max_x and min_y <= y <= max_y
    
    def set_active(self, active=True):
        """设置激活状态"""
        self.state = 'active' if active else 'normal'
        self.draw_shape()
        self.draw_text()
    
    def pack(self, **kwargs):
        """布局方法"""
        self.canvas.pack(**kwargs)
    
    def place(self, **kwargs):
        """位置布局方法"""
        self.canvas.place(**kwargs)
    
    def grid(self, **kwargs):
        """网格布局方法"""
        self.canvas.grid(**kwargs)
