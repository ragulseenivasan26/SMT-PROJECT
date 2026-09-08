@echo off
<<<<<<< HEAD
=======
chcp 65001 >nul
>>>>>>> 13b8654 (feat(v2.0): Vernacular AI with Engineering NEC Symbols Studio, Study Themes, Live Circuit Simulators & Cinema Dubbing)
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
<<<<<<< HEAD
git commit -m "feat: Vernacular AI Multi-Lingual Platform (51 Languages, Cinema Dub Studio, Offline Engine, Academic Report Generator)"

echo.
echo ======================================================================
echo  GitHub Remote Setup
echo ======================================================================
echo If you haven't created a GitHub repository yet:
echo   1. Go to https://github.com/new
echo   2. Create a new repository named "Vernacular_AI" (Do NOT check initialize with README)
echo   3. Copy your repository HTTPS URL (e.g. https://github.com/YOUR_USERNAME/Vernacular_AI.git)
echo ======================================================================
echo.

set /p REPO_URL="Paste your GitHub repository URL: "

if "%REPO_URL%"=="" (
    echo [!] No URL entered. Changes have been committed locally.
    echo You can push manually anytime using: git push -u origin main
    pause
    exit /b 0
)

echo.
echo [*] Configuring remote origin: %REPO_URL%...
git remote remove origin 2>nul
git remote add origin %REPO_URL%

echo [*] Setting branch to main...
git branch -M main

echo [*] Pushing to GitHub (origin main)...
=======
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
>>>>>>> 13b8654 (feat(v2.0): Vernacular AI with Engineering NEC Symbols Studio, Study Themes, Live Circuit Simulators & Cinema Dubbing)
git push -u origin main

if %errorlevel% equ 0 (
    echo.
    echo ======================================================================
<<<<<<< HEAD
    echo  SUCCESS! Your project has been pushed to GitHub successfully!
    echo ======================================================================
) else (
    echo.
    echo [!] Push encountered an error. Please check your GitHub credentials or URL.
    echo You can also run: git push -u origin main
=======
    echo  SUCCESS! Your updates are live on https://github.com/ragulseenivasan26/Vernacular_AI
    echo ======================================================================
) else (
    echo.
    echo [!] Push note: If origin has changes, attempting git pull --rebase...
    git pull --rebase origin main
    git push -u origin main
>>>>>>> 13b8654 (feat(v2.0): Vernacular AI with Engineering NEC Symbols Studio, Study Themes, Live Circuit Simulators & Cinema Dubbing)
)

echo.
pause
