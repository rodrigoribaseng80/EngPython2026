@echo off
title Calculadora de Superno - Guia de Engenharia
cls

:: Navega ate a pasta do projeto
cd /d "C:\PythonCodes\Codes 2026"

:: Verifica se o servidor Streamlit ja esta ativo na porta 8501
netstat -ano | findstr :8501 >nul
if %errorlevel% == 0 (
    echo Servidor ja esta rodando. Abrindo o navegador...
    start http://localhost:8501
) else (
    echo Iniciando o servidor Streamlit e a Calculadora...
    :: O comando abaixo inicia o streamlit sem bloquear o terminal
    start /b streamlit run "C:\PythonCodes\Codes 2026\seu_script.py" --server.port 8501 --server.headless true
    
    :: Aguarda 3 segundos para o servidor subir e abre o navegador
    timeout /t 3 /nobreak >nul
    start http://localhost:8501
)

exit