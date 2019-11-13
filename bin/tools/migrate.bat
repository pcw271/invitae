REM migrate

cd /D "%~dp0"
cd ../../app

REM migrate
python manage.py makemigrations && python manage.py migrate

cmd /k 
PAUSE