cd /D "%~dp0"

REM get access to db
python manage.py dbshell

cmd /k 
PAUSE