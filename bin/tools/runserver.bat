REM run server

cd /D "%~dp0"
cd ../../app

REM run
python manage.py runserver

cmd /k 
PAUSE