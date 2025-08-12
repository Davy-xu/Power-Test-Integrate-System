@echo off
echo 🎨 启动Canvas渐变模式
echo.
echo 📁 当前目录: %CD%
echo.

REM 检查Python环境
python --version
if %ERRORLEVEL% NEQ 0 (
    echo ❌ Python未安装或不在PATH中
    pause
    exit /b 1
)

echo.
echo 🖼️ Canvas渐变模式 - 纯代码绘制背景
echo   • 不依赖图片文件
echo   • 实时动态绘制
echo   • 响应式窗口缩放
echo   • 三段式蓝色渐变

echo.
echo 🎯 启动主程序...
python app.py

echo.
echo 📝 程序已退出
pause
