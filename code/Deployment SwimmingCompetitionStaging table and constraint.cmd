@echo off

set sqlcmd="C:\Program Files\Microsoft SQL Server\110\Tools\Binn\SQLCMD.EXE"
set work_dir=%~dp0
cd %work_dir%
for %%A in (%work_dir%DDL\*SwimmingCompetitionStaging*CreateDatabase*.sql) do sqlcmd -S . -E -i "%%A"
for %%B in (%work_dir%DDL\*SwimmingCompetitionStaging*table*.sql) do sqlcmd -S . -E -i "%%B"
for %%C in (%work_dir%DDL\*SwimmingCompetitionStaging*constraint*.sql) do sqlcmd -S . -E -i "%%C"

pause
