@echo off
echo ========================================
echo  Gerador de Executavel - Exportador ConsultaSQL
echo ========================================
echo.

echo [1/3] Instalando PyInstaller...
pip install pyinstaller

echo.
echo [2/3] Gerando executavel...
pyinstaller --onefile --windowed --name "ExportadorConsultaSQL" sql_export.py

echo.
echo [3/3] Limpando arquivos temporarios...
rmdir /s /q build
del /q ExportadorConsultaSQL.spec

echo.
echo ========================================
echo  Concluido!
echo ========================================
echo.
echo O executavel esta em: dist\ExportadorConsultaSQL.exe
echo.
pause
