# WoT Mods Loader

![python](https://img.shields.io/badge/python-2.7.18-blue?link=https://www.python.org/downloads/release/python-2718/)

This loader works in a same way XVM works, you can use it to loads you own mods.

The purpose of this script is to provide a loader and a compiler in one mod to easily load your mods.


## Building

**[OPTIONAL]** : You can specify a [path](./src/mod_loader.py) for your `res_mods `folder, without a custom path, the script will tries to find the greater WoT version:
```python
hardCoded_path = ''
#eg: './res_mods/X.X.X.X/mods/modules'
```

You need to compile [the loader](./src/mod_loader.py), for that you can :

• Use the [builder.bat](build.bat) (Windows) / [builder.sh](build.sh) (Linux) and then copy the content of `/build` inside your `World_of_Tanks/res_mods/X.X.X.X/` folder.

• Compile manually by doing:
```bat
python2 -m compileall src/.
```
Then move `mod_loader.pyc` file inside [`src/`](./src) to `World_of_Tanks/res_mods/X.X.X.X/scripts/client/gui/mods/`


## How to use

• Download [Python 2.7](https://www.python.org/downloads/release/python-2718/)

• Download the project or clone it

• Start **World Of Tanks**, hopefully the loader will starts, compiles and loads all your mods in `World_of_Tanks/res_mods/X.X.X.X/mods/modules/`


## Debugging

If you have any problem, see what is going on in `World_of_Tanks/python.log`


## Credits

Original [mods loader](https://github.com/juho-p/wot-debugserver/blob/master/loader/mod_.py) I used to make my own.


## Copyright

See the [license](/LICENSE).