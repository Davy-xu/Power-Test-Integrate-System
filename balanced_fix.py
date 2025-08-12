"""
修复布局平衡的脚本
"""
import os
import shutil

def fix_balance():
    """修复界面布局平衡"""
    main_file = r"d:\Power Test Integrate System\simple_tkintertools_main.py"
    backup_file = r"d:\Power Test Integrate System\simple_tkintertools_main_backup.py"
    
    # 备份原文件
    try:
        shutil.copy2(main_file, backup_file)
        print("✅ 已备份原文件")
    except Exception as e:
        print(f"备份失败: {e}")
        return
    
    # 读取原文件
    try:
        with open(main_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"读取文件失败: {e}")
        return
    
    # 定义新的平衡函数
    new_function = '''    def create_simple_content_area(self):
        """创建平衡的放大内容区域"""
        print("📐 创建平衡的放大内容区域...")
        
        # 获取窗口尺寸
        self.root.update_idletasks()
        window_width = self.bg_canvas.winfo_width() or 1200
        window_height = self.bg_canvas.winfo_height() or 800
        
        # 计算平衡的内容区域位置 - 考虑左侧按钮宽度
        content_x = 180   # 留出足够空间给左侧按钮
        content_y = 100   # 留出标题空间
        
        # 创建内容框架
        self.content_frame = tk.Frame(self.bg_canvas, bg='white', relief='raised', bd=1)
        
        # 计算合理的尺寸 - 根据窗口大小动态调整
        content_width = max(800, window_width - content_x - 40)   # 预留右边距
        content_height = max(500, window_height - content_y - 80) # 预留底部状态栏
        
        print(f"📐 平衡内容区域参数:")
        print(f"   窗口尺寸: {window_width} x {window_height}")
        print(f"   内容位置: ({content_x}, {content_y})")
        print(f"   内容尺寸: {content_width} x {content_height}")
        
        # 放置内容区域
        self.content_window = self.bg_canvas.create_window(
            content_x, content_y, window=self.content_frame, anchor='nw',
            width=content_width, height=content_height
        )
        
        # 添加默认内容
        self.show_simple_welcome_content()
        
        # 绑定窗口调整大小事件 - 平衡的响应式设计
        def resize_content(event=None):
            if event and event.widget == self.root:
                try:
                    win_w = self.bg_canvas.winfo_width()
                    win_h = self.bg_canvas.winfo_height()
                    # 平衡的内容区域调整
                    new_w = max(800, win_w - content_x - 40)
                    new_h = max(500, win_h - content_y - 80)
                    self.bg_canvas.itemconfig(self.content_window, width=new_w, height=new_h)
                    print(f"📐 平衡内容区域调整: {new_w}x{new_h}")
                except Exception as e:
                    print(f"调整内容区域时出错: {e}")
        
        self.root.bind('<Configure>', resize_content)
        
        print(f"✅ 平衡内容区域创建完成，ID: {self.content_window}")'''
    
    # 查找并替换函数
    import re
    
    # 使用正则表达式找到函数定义并替换
    pattern = r'(\s+def create_simple_content_area\(self\):.*?)(^\s+print\(f"✅ 超大内容区域创建完成，ID: \{self\.content_window\}"\))'
    
    def replacement(match):
        indent = match.group(1).split('def')[0]  # 获取缩进
        return new_function
    
    new_content = re.sub(pattern, replacement, content, flags=re.MULTILINE | re.DOTALL)
    
    # 如果正则替换没成功，尝试手动查找替换
    if new_content == content:
        start_marker = "def create_simple_content_area(self):"
        end_marker = '✅ 超大内容区域创建完成，ID: {self.content_window}")'
        
        start_pos = content.find(start_marker)
        if start_pos != -1:
            end_pos = content.find(end_marker, start_pos)
            if end_pos != -1:
                end_pos = content.find('\n', end_pos) + 1
                # 获取缩进
                line_start = content.rfind('\n', 0, start_pos) + 1
                indent = content[line_start:start_pos]
                
                new_content = (content[:line_start] + 
                             new_function + '\n' +
                             content[end_pos:])
                print("✅ 手动替换成功")
            else:
                print("❌ 找不到函数结束标记")
                return
        else:
            print("❌ 找不到函数开始标记")
            return
    else:
        print("✅ 正则替换成功")
    
    # 写入新内容
    try:
        with open(main_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("✅ 文件修复完成")
        print("📝 修改内容:")
        print("   - 内容区域位置: (180, 100)")
        print("   - 最小尺寸: 800x500")
        print("   - 边距: 左180 右40 顶100 底80")
        print("   - 实现了平衡的响应式布局")
    except Exception as e:
        print(f"❌ 写入文件失败: {e}")
        # 恢复备份
        shutil.copy2(backup_file, main_file)
        print("🔄 已恢复备份文件")

if __name__ == "__main__":
    fix_balance()
