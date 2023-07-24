@echo off
set "script=windu.py"
set "destination=C:\Windows\System32"

echo Uninstalling %script% from %destination% ...

REM 使用findstr命令检查脚本是否在System32目录中
echo %destination%\%script% | findstr /i /c:"\%script%"

REM 如果脚本不存在于System32目录中，不进行卸载操作
if %errorlevel% neq 0 (
    echo %script% is not found in %destination%. No action required.
    pause
    exit
)

REM 此处将脚本从System32目录中移除
del %destination%\%script%

echo %script% uninstalled successfully from %destination%.
pause
