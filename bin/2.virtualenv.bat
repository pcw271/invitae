REM create venv

REM set path as current location and go to parent
cd /D "%~dp0"
cd ../

REM create virtualenv
del env
python -m virtualenv env

REM activate virtualenv
.\env\Scripts\activate.bat

REM download dependencies directly from pip
pip install -r requirements.txt

cmd /k 
PAUSE
