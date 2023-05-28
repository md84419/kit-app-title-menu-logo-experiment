@echo off

setlocal

call :runme call _build\windows-x86_64\release\robotica.example.app.bat %* <NUL

goto :eof

:runme
%*
goto :eof
