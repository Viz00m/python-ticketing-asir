@echo off
TITLE Ticketing ASIR Suite - Backend Server
echo ====================================================
echo    Iniciando Servidor Ticketing ASIR Suite
echo ====================================================
echo.
echo Asegurate de haber ejecutado 'install_dependencies.bat' previamente.
echo.
echo El servidor estara disponible en: http://localhost:8000
echo La documentacion API esta en: http://localhost:8000/docs
echo.
echo [INFO] Presiona CTRL+C para detener el servidor.
echo.

python -m uvicorn backend.main:app --reload

if %errorlevel% neq 0 (
    echo.
    echo [ERROR] No se pudo iniciar el servidor.
    echo Verifica que Python este instalado y las dependencias cargadas.
    pause
)
