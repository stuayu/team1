@echo off

echo ===========================================================
echo.
echo                  Team1�̃V�X�e���̃C���X�g�[��
echo.
echo                               Auther stuayu and contributor
echo ============================================================
echo.
echo.
echo    (����)�V�X�e�����C���X�g�[������O�Ɋm�F���Ă��������B
echo.
echo    NodeJS
echo    Python
echo    MariaDB
echo              ���C���X�g�[�����܂������H
echo.
echo    �C���X�g�[�����Ă��Ȃ��ꍇ�̓C���X�g�[�����Ă��������B
echo.
pause
echo.
echo ============================================================
echo.
echo                   Web�T�[�o�C���X�g�[��
echo.
echo ============================================================
cd Client
npm install
npm run build
echo.
echo                  Web�̃C���X�g�[�����������܂���
echo.
echo ============================================================
echo.
echo                  WebAPI�T�[�o�C���X�g�[��
echo.
echo ============================================================
echo.
cd ../Server/
pip install -r requirements.txt
echo.
echo.
echo           WebAPI�T�[�o�̃C���X�g�[�����������܂���
echo ============================================================

pause