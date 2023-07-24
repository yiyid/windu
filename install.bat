@echo off
set "script=windu.py"
set "destination=C:\Windows\System32"

echo Moving %script% to %destination% ...

REM 此处将脚本移动到System32目录中
move %script% %destination%

echo %script% moved successfully to %destination%.
pause
