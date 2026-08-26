@echo off
title FrankBase GitHub Remote Push
echo ========================================================
echo   FRANKBASE.COM - GITHUB REMOTE PUSH
echo ========================================================
git add .
set /p commit_msg="Enter commit message (or press enter for default): "
if "%commit_msg%"=="" set commit_msg="feat: update frankbase website and core pages"
git commit -m "%commit_msg%"
git push origin main
echo.
echo ========================================================
echo   PUSH COMPLETED SUCCESSFULLY!
echo ========================================================
pause
