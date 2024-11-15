@echo off
setlocal

:: 设置源目录和目标目录
set "src_dir=%CD%"
set "dest_dir=%CD%\..\assets\config\level"

:: 确保目标目录存在，如果不存在则创建
if not exist "%dest_dir%" (
    mkdir "%dest_dir%"
)

:: 遍历源目录中的所有 JSON 文件
for %%f in (*.json) do (
    :: 复制文件并覆盖已存在的文件
    copy /Y "%%f" "%dest_dir%\%%f"
    echo Copied %%f to %dest_dir%\%%f
)

endlocal
pause