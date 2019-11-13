REM # generate list of required packages

REM set path as current location and go to parent
cd /D "%~dp0"
cd ../

REM # run pipreqs
python ./lib/pipreqs/pipreqs.py ./app/ --encoding=iso-8859-1 --debug --force --version=greater --savepath=requirements.txt

cmd /k 
PAUSE
