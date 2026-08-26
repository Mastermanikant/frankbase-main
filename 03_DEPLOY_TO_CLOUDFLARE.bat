@echo off
title FrankBase - Deploy to Cloudflare Pages
echo ========================================================
echo   FRANKBASE.COM - CLOUDFLARE PAGES LIVE DEPLOY
echo ========================================================
cd /d "%~dp001_Website_Code"
echo 1. Building Eleventy Static Site...
call npx @11ty/eleventy
echo.
echo 2. Deploying _site to Cloudflare Pages (project: frankbase)...
call npx wrangler pages deploy _site --project-name=frankbase --commit-dirty=true
echo.
echo ========================================================
echo   DEPLOYMENT COMPLETED SUCCESSFULLY!
echo ========================================================
pause
