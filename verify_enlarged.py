#!/usr/bin/env python3
"""
验证白色界面放大效果
"""
import sys
import os
import tkinter as tk
from datetime import datetime

# 添加路径
sys.path.insert(0, "d:\\Power Test Integrate System")

def verify_enlarged_interface():
    """验证白色界面放大效果"""
    print("🔍 验证白色界面放大效果...")
    print("=" * 50)
    print("预期改进:")
    print("✅ 白色内容区域应该明显更大")
    print("✅ 左边距从180减少到140像素")
    print("✅ 上边距从120减少到90像素") 
    print("✅ 内容区域最小宽度从400增加到600像素")
    print("✅ 内容区域最小高度从300增加到400像素")
    print("✅ 窗口调整大小时内容区域应该更积极地扩展")
    print("=" * 50)
    
    try:
        # 导入主模块
        import simple_tkintertools_main as main_module
        
        print("✅ 主模块导入成功")
        print("🚀 启动验证程序...\n")
        
        # 创建验证窗口
        verification_root = tk.Tk()
        verification_root.title("验证结果监控")
        verification_root.geometry("400x300")
        verification_root.attributes('-topmost', True)  # 置顶
        
        # 验证信息显示
        info_frame = tk.Frame(verification_root, bg='lightblue', padx=10, pady=10)
        info_frame.pack(fill='both', expand=True)
        
        title_label = tk.Label(info_frame, text="白色界面放大验证", 
                              font=('Microsoft YaHei UI', 14, 'bold'),
                              bg='lightblue')
        title_label.pack(pady=10)
        
        status_label = tk.Label(info_frame, text="正在检测界面参数...", 
                               font=('Microsoft YaHei UI', 11),
                               bg='lightblue', justify='left')
        status_label.pack(pady=5)
        
        results_text = tk.Text(info_frame, height=8, width=45, font=('Consolas', 9))
        results_text.pack(pady=10)
        
        def start_main_interface():
            """启动主界面"""
            print("启动主界面进行验证...")
            verification_root.after(2000, lambda: verification_root.destroy())
            main_module.main()
        
        def update_verification():
            """更新验证信息"""
            current_time = datetime.now().strftime("%H:%M:%S")
            status_label.config(text=f"验证时间: {current_time}")
            
            verification_text = f"""验证项目:
            
□ 检查白色内容区域是否比之前更大
□ 检查左侧按钮是否更紧凑
□ 拖拽窗口边缘查看内容区域响应
□ 比较调整前后的空间利用率
□ 观察控制台输出的尺寸信息

预期看到:
• 内容区域位置: (140, 90) 而非 (180, 120)
• 最小尺寸: 600x400 而非 400x300
• 控制台输出包含"放大内容区域"字样

测试方法:
1. 观察白色区域相对大小
2. 调整窗口大小查看响应
3. 检查控制台输出信息
"""
            results_text.delete(1.0, tk.END)
            results_text.insert(1.0, verification_text)
            
            verification_root.after(1000, update_verification)
        
        # 开始更新
        update_verification()
        
        # 2秒后启动主界面
        verification_root.after(2000, start_main_interface)
        
        print("✅ 验证程序已启动")
        print("📋 验证清单:")
        print("   1. 白色内容区域是否比之前明显更大")
        print("   2. 左侧按钮区域是否更紧凑")
        print("   3. 调整窗口大小时内容区域是否正确响应")
        print("   4. 控制台是否输出'放大内容区域'相关信息\n")
        
        # 运行验证窗口
        verification_root.mainloop()
        
    except Exception as e:
        print(f"❌ 验证失败: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    verify_enlarged_interface()
