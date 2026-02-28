@echo off
chcp 65001 >nul
title Auto Chrome Script GUI
color 0A
mode con: cols=80 lines=25

echo.
echo   █████╗ ██╗   ██╗████████╗ ██████╗      ██████╗██╗  ██╗██████╗  ██████╗ ███╗   ███╗███████╗
echo  ██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗    ██╔════╝██║  ██║██╔══██╗██╔═══██╗████╗ ████║██╔════╝
echo  ███████║██║   ██║   ██║   ██║   ██║    ██║     ███████║██████╔╝██║   ██║██╔████╔██║█████╗  
echo  ██╔══██║██║   ██║   ██║   ██║   ██║    ██║     ██╔══██║██╔══██╗██║   ██║██║╚██╔╝██║██╔══╝  
echo  ██║  ██║╚██████╔╝   ██║   ╚██████╔╝    ╚██████╗██║  ██║██║  ██║╚██████╔╝██║ ╚═╝ ██║███████╗
echo  ╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝      ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝
echo.
echo  ================================
echo        AUTO CHROME TIẾNG VIỆT
echo  ================================
echo.

rem Lấy thư mục hiện tại
set "CURRENT_DIR=%~dp0"
cd /d "%CURRENT_DIR%"

rem Tìm Python - ưu tiên Anaconda nếu có
echo [INFO] Đang tìm Python...
set "PYTHON_PATH="

rem Tìm trong PATH thông thường
where python >nul 2>nul
if %ERRORLEVEL% equ 0 (
    echo [INFO] Tìm thấy Python trong PATH
    rem Lấy đường dẫn chính xác của python
    for /f "delims=" %%i in ('where python') do (
        set "PYTHON_FULL_PATH=%%i"
        echo [INFO] Đường dẫn Python: %%i
        goto :run_script
    )
)

rem Tìm Anaconda3 trong thư mục user
if exist "C:\Users\%USERNAME%\anaconda3\python.exe" (
    set "PYTHON_PATH=C:\Users\%USERNAME%\anaconda3"
    echo [INFO] Tìm thấy Anaconda Python tại: %PYTHON_PATH%
    set "PATH=%PYTHON_PATH%;%PYTHON_PATH%\Scripts;%PATH%"
    goto :run_script
)

rem Tìm Anaconda3 ở các vị trí khác
if exist "C:\ProgramData\anaconda3\python.exe" (
    set "PYTHON_PATH=C:\ProgramData\anaconda3"
    echo [INFO] Tìm thấy Anaconda Python tại: %PYTHON_PATH%
    set "PATH=%PYTHON_PATH%;%PYTHON_PATH%\Scripts;%PATH%"
    goto :run_script
)

if exist "C:\Anaconda3\python.exe" (
    set "PYTHON_PATH=C:\Anaconda3"
    echo [INFO] Tìm thấy Anaconda Python tại: %PYTHON_PATH%
    set "PATH=%PYTHON_PATH%;%PYTHON_PATH%\Scripts;%PATH%"
    goto :run_script
)

echo [LOI] KHÔNG tìm thấy Python!
echo.
echo Có thể cài đặt Python theo các cách sau:
echo 1. Python.org: https://www.python.org/downloads/
echo 2. Anaconda: https://www.anaconda.com/products/distribution
echo.
echo Sau khi cài đặt, vui lòng khởi động lại máy tính hoặc thêm Python vào PATH.
pause
exit /b 1

:run_script
echo.
echo [INFO] Python thông tin:
python --version
echo.

rem Hiển thị phiên bản và đường dẫn chi tiết hơn
python -c "import sys; print(f'Phiên bản: {sys.version}'); print(f'Đường dẫn: {sys.executable}')"
echo.

echo [INFO] Thư mục làm việc: %CURRENT_DIR%
echo.

echo [INFO] Đang khởi động Auto Chrome Script GUI...
timeout /t 1 /nobreak >nul

rem Kiểm tra file tool.py
if not exist "tool.py" (
    echo [LOI] Không tìm thấy file tool.py!
    echo Cần đặt file này cùng thư mục với start.bat
    pause
    exit /b 1
)

rem Chạy script
python tool.py

echo.
if %ERRORLEVEL% equ 0 (
    echo [INFO] Chương trình đã kết thúc thành công!
) else (
    echo [LOI] Chương trình kết thúc với lỗi: %ERRORLEVEL%
)
echo.
pause