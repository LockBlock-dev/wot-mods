@echo off

mkdir build\scripts\client\gui\mods
mkdir build\mods\modules

python2 -m compileall src/.

move src\*.pyc build\scripts\client\gui\mods\
