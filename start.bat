@echo off

echo =========================================
echo.
echo        システムを起動します
echo                          Auther stuayu
echo =========================================

rem nginx起動
cd nginx
start nginx

rem startコマンドで別プロセスとして実行
cd ..\Server
start powershell -command "uvicorn main:app"

cd ..\Client
start powershell -command "npm start"

echo.
echo システムを終了する際には Control+C で終了してください。
pause