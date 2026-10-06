@echo off
title AI Vernacular Pedagogy - SMT CO2
echo ========================================================
echo   AI-Powered Vernacular Pedagogy and Translation Tool
echo   Starting Backend & Frontend Server...
echo ========================================================
cd /d "%~dp0backend"

echo Checking requirements...
python -m pip install -r requirements.txt --quiet

echo Opening browser at http://127.0.0.1:8000 ...
start "" http://127.0.0.1:8000

echo Starting FastAPI server with Uvicorn...
python -m uvicorn app:app --reload --host 127.0.0.1 --port 8000

pause
