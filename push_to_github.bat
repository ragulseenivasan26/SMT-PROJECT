@echo off
chcp 65001 >nul
title AI Vernacular Pedagogy - Push to GitHub
echo ======================================================================
echo           AI VERNACULAR PEDAGOGY - 1-CLICK GITHUB PUSH WIZARD
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
git commit -m "update: AI Vernacular Pedagogy with Multimodal Video Translation, Live Camera OCR & Schemes Hub"

echo.
echo [*] Checking remote smt-project...
git remote get-url smt-project >nul 2>nul
if %errorlevel% neq 0 (
    echo [*] Setting remote smt-project to https://github.com/ragulseenivasan26/SMT-PROJECT.git
    git remote add smt-project https://github.com/ragulseenivasan26/SMT-PROJECT.git
)

echo [*] Setting branch to main...
git branch -M main

echo [*] Pushing updates to GitHub (smt-project main)...
git push -u smt-project main

if %errorlevel% equ 0 (
    echo.
    echo ======================================================================
    echo  SUCCESS! Your updates are live on https://github.com/ragulseenivasan26/SMT-PROJECT
    echo ======================================================================
) else (
    echo.
    echo [!] Push note: Attempting git pull --rebase...
    git pull --rebase smt-project main
    git push -u smt-project main
)

echo.
pause
