@echo off
:: Get the current directory of the batch file
set currentDir=%~dp0

:: Run the Python script using the current directory path
python "%currentDir%main.py"

:: Pause to keep the command prompt open
pause