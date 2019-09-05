@echo off

set sqlcmd="C:\Program Files\Microsoft SQL Server\110\Tools\Binn\SQLCMD.EXE"
set work_dir=%~dp0
cd %work_dir%
for %%B in (%work_dir%DDL\*Audit*table*.sql) do sqlcmd -S . -E -i "%%B"
for %%C in (%work_dir%DDL\*Audit*constraint*.sql) do sqlcmd -S . -E -i "%%C"

pause
