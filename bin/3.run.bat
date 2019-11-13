REM run server from venv

REM set path as current location and go to parent
cd /D "%~dp0"
cd ../

REM activate virtualenv, run server
.\env\Scripts\activate.bat && cd app && python manage.py runserver

cmd /k 
PAUSE
