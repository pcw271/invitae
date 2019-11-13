REM generate models for an existing database in Django

cd /D "%~dp0"
cd ../../app

REM run
python manage.py inspectdb

cmd /k 
PAUSE