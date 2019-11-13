REM run unit tests

REM set path as current location and go to parent
cd /D "%~dp0"
cd ../

REM activate virtualenv, run unit test
.\env\Scripts\activate.bat && cd app && python manage.py test invitae

cmd /k 
PAUSE
