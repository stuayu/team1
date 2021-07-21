@echo off

echo ===========================================================
echo.
echo                  Team1のシステムのインストール
echo. 
echo                               Auther stuayu and contributor
echo ============================================================
echo.
echo. 
echo    (注意)システムをインストールする前に確認してください。
echo.
echo    NodeJS
echo    Python
echo    MariaDB
echo              をインストールしましたか？
echo.
echo    インストールしていない場合はインストールしてください。
echo.
pause
echo.
echo ============================================================
echo.
echo                   Webサーバインストール
echo.
echo ============================================================
cd Client
npm install
npm run build
echo.
echo                  Webのインストールが完了しました
echo.
echo ============================================================
echo.
echo                  WebAPIサーバインストール
echo.
echo ============================================================
echo.
cd ../Server/
pip install -r requirements.txt
echo.
echo.
echo           WebAPIサーバのインストールが完了しました
echo ============================================================

pause