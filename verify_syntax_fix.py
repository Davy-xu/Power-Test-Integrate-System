"""
验证语法修复并测试程序
"""
import subprocess
import sys
import os

def verify_syntax_fix():
    """验证语法修复"""
    print("🔍 验证语法修复...")
    
    # 1. 检查语法
    try:
        result = subprocess.run([
            sys.executable, "-m", "py_compile", 
            r"d:\Power Test Integrate System\simple_tkintertools_main.py"
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ 语法检查通过")
        else:
            print(f"❌ 语法错误: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ 语法检查失败: {e}")
        return False
    
    # 2. 检查关键代码行
    try:
        with open(r"d:\Power Test Integrate System\simple_tkintertools_main.py", 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # 查找修复的行
        for i, line in enumerate(lines):
            if "self.current_tab = 0" in line and "def create_simple_content_area" in line:
                print(f"❌ 第{i+1}行仍有合并错误: {line.strip()}")
                return False
        
        print("✅ 代码结构检查通过")
    except Exception as e:
        print(f"❌ 代码检查失败: {e}")
        return False
    
    # 3. 尝试导入模块
    try:
        sys.path.insert(0, r"d:\Power Test Integrate System")
        import simple_tkintertools_main
        print("✅ 模块导入成功")
        return True
    except Exception as e:
        print(f"❌ 模块导入失败: {e}")
        return False

def test_program():
    """测试程序启动"""
    print("\n🚀 测试程序启动...")
    
    try:
        # 设置工作目录
        os.chdir(r"d:\Power Test Integrate System")
        
        # 启动程序
        print("启动主程序...")
        result = subprocess.run([sys.executable, "app.py"], 
                              timeout=10, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ 程序启动成功")
        else:
            print(f"⚠️ 程序退出: {result.stderr}")
            
    except subprocess.TimeoutExpired:
        print("✅ 程序正在运行中（10秒后超时终止测试）")
    except Exception as e:
        print(f"❌ 程序测试失败: {e}")

if __name__ == "__main__":
    print("=" * 50)
    print("🔧 语法修复验证工具")
    print("=" * 50)
    
    if verify_syntax_fix():
        print("\n🎉 语法修复成功！")
        test_program()
    else:
        print("\n❌ 语法修复失败，需要进一步处理")
