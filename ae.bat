:: @echo off
echo started
cmd /k "venv\scripts\activate.bat"
cd first_django_project
flake8 .
:: isort .
:: black .
echo ended
pause