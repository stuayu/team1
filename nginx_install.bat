@echo off


echo =============================================
echo.
echo           nginx�̃_�E�����[�h���s���܂�
echo                               Auther stuayu
echo =============================================

rem nginx�̃o�[�V�������w�肷��
set nginx_ver=nginx-1.21.1

rem nginx�����T�C�g����_�E�����[�h
call powershell -command "wget 'https://nginx.org/download/%nginx_ver%.zip' -o %nginx_ver%.zip"

rem zip�̓W�J
call powershell -command "Expand-Archive -Force %nginx_ver%.zip"
xcopy /e /y %nginx_ver%\%nginx_ver% nginx
rmdir /s /q %nginx_ver%
del %nginx_ver%.zip

rem �ݒ�t�@�C���̎����R�s�[
xcopy /y nginx\setting\*.conf nginx\conf\

echo.
echo.
echo ----------------------------------------------
echo.
echo           nginx�̃_�E�����[�h���������܂���
echo.
pause
