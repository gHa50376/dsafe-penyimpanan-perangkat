@echo off
setlocal
cd /d "%~dp0"

set "PYTHON_CMD="
py -3 -c "import streamlit, pptx, PIL, reportlab" >nul 2>&1
if not errorlevel 1 set "PYTHON_CMD=py -3"
if not defined PYTHON_CMD (
    python -c "import streamlit, pptx, PIL, reportlab" >nul 2>&1
    if not errorlevel 1 set "PYTHON_CMD=python"
)

if not defined PYTHON_CMD (
    echo Python atau paket aplikasi belum siap.
    echo Buka Command Prompt di folder ini, lalu jalankan:
    echo     python -m pip install -r requirements.txt
    echo Setelah selesai, jalankan berkas ini lagi.
    pause
    exit /b 1
)

echo D-Safe sedang dijalankan di port 8501.
echo Komputer: http://localhost:8501
echo HP: http://ALAMAT-IPv4-KOMPUTER:8501
echo.
echo Alamat IPv4 yang terdeteksi di komputer:
ipconfig | findstr /i "IPv4"
echo.
echo Gunakan IPv4 dari Wi-Fi yang sama dengan HP. Tutup jendela ini untuk menghentikan aplikasi.
echo.
%PYTHON_CMD% -m streamlit run app.py --server.address 0.0.0.0 --server.port 8501 --server.headless true
if errorlevel 1 pause
