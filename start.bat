@echo off

echo =========================================
echo.
echo        �V�X�e�����N�����܂�
echo                          Auther stuayu
echo =========================================

rem nginx�N��
cd nginx
start nginx

rem start�R�}���h�ŕʃv���Z�X�Ƃ��Ď��s
cd ..\Server
start powershell -command "uvicorn main:app"

cd ..\Client
start powershell -command "npm start"

echo.
echo �V�X�e�����I������ۂɂ� Control+C �ŏI�����Ă��������B
pause