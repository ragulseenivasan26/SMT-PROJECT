@echo off
chcp 65001 >nul
title Vernacular AI - Push to GitHub
echo ======================================================================
echo           VERNACULAR AI - 1-CLICK GITHUB PUSH WIZARD
echo ======================================================================
echo.

cd /d "%~dp0"

echo [*] Checking Git installation...
where git >nul 2>nul
if %errorlevel% neq 0 (
    echo [!] Git is not installed or not found in PATH.
    echo Please install Git from https://git-scm.com/ and try again.
    pause
    exit /b 1
)

echo [*] Staging all project files...
git add .

echo [*] Creating commit...
git commit -m "feat(v2.0): Vernacular AI with Engineering NEC Symbols Studio, Study Themes, Live Circuit Simulators & Cinema Dubbing"

echo.
echo [*] Checking remote origin...
git remote get-url origin >nul 2>nul
if %errorlevel% neq 0 (
    echo [*] Setting remote origin to https://github.com/ragulseenivasan26/Vernacular_AI.git
    git remote add origin https://github.com/ragulseenivasan26/Vernacular_AI.git
)

echo [*] Setting branch to main...
git branch -M main

echo [*] Pushing updates to GitHub (origin main)...
git push -u origin main

if %errorlevel% equ 0 (
    echo.
    echo ======================================================================
    echo  SUCCESS! Your updates are live on https://github.com/ragulseenivasan26/Vernacular_AI
    echo ======================================================================
) else (
    echo.
    echo [!] Push note: If origin has changes, attempting git pull --rebase...
    git pull --rebase origin main
    git push -u origin main
)

echo.
pause
