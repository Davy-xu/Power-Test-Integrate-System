@echo off
echo 🚀 启动电源测试设备集成控制系统（PNG背景版）
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
echo 🖼️ 检查背景图片...
if exist "gradient_background.png" (
    echo ✅ 找到PNG背景图片
) else if exist "gradient_simple.gif" (
    echo ✅ 找到GIF背景图片
) else (
    echo ⚠️ 未找到背景图片，将使用Canvas渐变
)

echo.
echo 🎯 启动主程序...
python final_png_version.py

echo.
echo 📝 程序已退出
pause
