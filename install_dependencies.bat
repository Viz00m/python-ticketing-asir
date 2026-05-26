@echo off
TITLE Ticketing ASIR Suite - Instalador
echo ====================================================
echo    Instalando Dependencias
echo ====================================================
echo.
echo Verificando instalacion de Python...
python --version
if %errorlevel% neq 0 (
    echo [ERROR] Python no encontrado. Por favor instalalo y agregalo al PATH.
    pause
    exit /b
)

echo.
echo Instalando librerias desde requirements.txt...
python -m pip install -r requirements.txt

echo.
echo ====================================================
echo    Instalacion Completada
echo ====================================================
echo Puedes cerrar esta ventana y ejecutar 'run_server.bat'.
pause
