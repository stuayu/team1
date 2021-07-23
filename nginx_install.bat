@echo off


echo =============================================
echo.
echo           nginxのダウンロードを行います
echo                               Auther stuayu
echo =============================================

rem nginxのバーションを指定する
set nginx_ver=nginx-1.21.1

rem nginx公式サイトからダウンロード
call powershell -command "wget 'https://nginx.org/download/%nginx_ver%.zip' -o %nginx_ver%.zip"

rem zipの展開
call powershell -command "Expand-Archive -Force %nginx_ver%.zip"
xcopy /e /y %nginx_ver%\%nginx_ver% nginx
rmdir /s /q %nginx_ver%
del %nginx_ver%.zip

rem 設定ファイルの自動コピー
xcopy /y nginx\setting\*.conf nginx\conf\

echo.
echo.
echo ----------------------------------------------
echo.
echo           nginxのダウンロードが完了しました
echo.
pause
