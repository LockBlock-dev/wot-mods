#!/usr/bin/bash
mkdir -p build/scripts/client/gui/mods
mkdir -p build/mods/modules

python2 -m compileall src/.

mv src/*.pyc build/scripts/client/gui/mods
