@echo off
chcp 65001 >nul
title Auto Chrome Script GUI + Smart Python Installer
color 0A
mode con: cols=100 lines=30

echo.
echo   █████╗ ██╗   ██╗████████╗ ██████╗      ██████╗██╗  ██╗██████╗  ██████╗ ███╗   ███╗███████╗
echo  ██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗    ██╔════╝██║  ██║██╔══██╗██╔═══██╗████╗ ████║██╔════╝
echo  ███████║██║   ██║   ██║   ██║   ██║    ██║     ███████║██████╔╝██║   ██║██╔████╔██║█████╗  
echo  ██╔══██║██║   ██║   ██║   ██║   ██║    ██║     ██╔══██║██╔══██╗██║   ██║██║╚██╔╝██║██╔══╝  
echo  ██║  ██║╚██████╔╝   ██║   ╚██████╔╝    ╚██████╗██║  ██║██║  ██║╚██████╔╝██║ ╚═╝ ██║███████╗
echo  ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚═════╝      ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝
echo.
echo  ==========================================================
echo            AUTO CHROME - TỰ ĐỘNG THIẾT LẬP PYTHON
echo  ==========================================================
echo.

rem Lấy thư mục hiện tại
set "CURRENT_DIR=%~dp0"
cd /d "%CURRENT_DIR%"

:check_python
echo [INFO] Đang kiểm tra Python trên hệ thống...

:: 1. Kiểm tra Python trong PATH
where python >nul 2>nul
if %ERRORLEVEL% equ 0 (
    echo [INFO] Tìm thấy Python trong PATH.
    goto :run_script
)

:: 2. Kiểm tra các đường dẫn phổ biến (Anaconda, v.v.)
set "PYTHON_FOUND=0"
for %%p in ("C:\Users\%USERNAME%\anaconda3\python.exe" "C:\ProgramData\anaconda3\python.exe" "C:\Anaconda3\python.exe") do (
    if exist %%p (
        echo [INFO] Tìm thấy Anaconda Python tại: %%~dpp
        set "PATH=%%~dpp;%%~dppScripts;%PATH%"
        set "PYTHON_FOUND=1"
        goto :run_script
    )
)

:: 3. Nếu chưa có, tiến hành cài đặt tự động
echo [WARNING] KHÔNG tìm thấy Python! Đang chuẩn bị cài đặt bản mới nhất...

:: Kiểm tra quyền Admin
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo [LOI] Cần quyền Administrator để cài đặt Python.
    echo [!] Vui lòng chuột phải vào file này và chọn "Run as Administrator".
    pause
    exit /b 1
)

echo [INFO] Đang dùng Winget để tải và cài đặt Python 3 (Silent Mode)...
winget install -e --id Python.Python.3 --source winget --override "/quiet PrependPath=1 Include_pip=1"

if %errorLevel% equ 0 (
    echo [OK] Cài đặt thành công. Đang làm mới biến môi trường...
    
    :: Logic thông minh: Tự động lấy PATH mới nhất từ Registry mà không cần khởi động lại máy
    for /f "tokens=*" %%i in ('powershell -command "[System.Environment]::GetEnvironmentVariable('PATH','Machine') + ';' + [System.Environment]::GetEnvironmentVariable('PATH','User')"') do set "PATH=%%i"
    
    :: Kiểm tra lại một lần nữa
    where python >nul 2>nul
    if %ERRORLEVEL% neq 0 (
        echo [!] Cảnh báo: Vui lòng tắt và mở lại file .bat này để hoàn tất cập nhật.
        pause
        exit /b 0
    )
    goto :run_script
) else (
    echo [LOI] Không thể tự động cài đặt. Vui lòng cài thủ công tại python.org
    pause
    exit /b 1
)

:run_script
echo.
echo [INFO] Trạng thái: Sẵn sàng.
python --version
echo.

:: Kiểm tra file tool.py
if not exist "tool.py" (
    echo [LOI] Không tìm thấy file tool.py!
    echo [!] Đảm bảo tool.py nằm cùng thư mục: %CURRENT_DIR%
    pause
    exit /b 1
)

echo [INFO] Đang khởi động Auto Chrome Script GUI...
timeout /t 2 /nobreak >nul

:: Chạy script Python
python tool.py

echo.
if %ERRORLEVEL% equ 0 (
    echo [INFO] Chương trình đã kết thúc thành công!
) else (
    echo [LOI] Chương trình lỗi (Mã: %ERRORLEVEL%)
)
echo.
pause