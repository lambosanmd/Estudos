@echo off

set "arquivo=%~1"

marp.exe --pdf --pdf-outlines "%arquivo%" --theme ..\.themes\a4.css

pause

