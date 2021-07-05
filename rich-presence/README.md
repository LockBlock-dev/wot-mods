# WoT Discord Rich Presence

![python](https://img.shields.io/badge/python-3.9-blue?link=https://www.python.org/downloads/) ![python](https://img.shields.io/badge/python-2.7.18-blue?link=https://www.python.org/downloads/release/python-2718/) ![pypresence](https://img.shields.io/badge/pypresence-4.2.0-blue?link=https://pypi.org/project/pypresence/)

The purpose of this mod is to provide you a better Discord rich presence than the default one.

Since WoT uses Python 2.7 and Pypresence Python 3.X, I made a server (executed by the game) and a client (executed by yourself) that communicate together.

The server runs on `127.0.0.1` port `7777`. You can edit these in [server.py](./src/rich_presence.py) and [client.py](./src/client.py).


## How to use

• Download the latest [Python 3 version](https://www.python.org/downloads/)

• Download the project or clone it

• You need to use my own [mod loader](../loader/mod_loader.py) and compile it, see [how in **Building**](../loader/README.md).

• Install [Pypresence](https://pypi.org/project/pypresence/), for that run a command and do :
```bash
pip3 install -r requirements.txt
```

• Move [rich_presence.py](./src/rich_presence.py) to your `World_of_Tanks/res_mods/X.X.X.X/mods/modules/` folder.

• You can edit and use the [starter](./start.bat) (Windows only) or you can :

• Run the client in a command prompt:
```bash
python3 src/client.py
```

• Start **World Of Tanks**, hopefully the rich presence will starts

• You can now see your World of Tanks Discord rich presence

## Debugging

If you have any problem, see what is going on in `World_of_Tanks/python.log`


## Credits

[WoT decompiled code](https://github.com/StranikS-Scan/WorldOfTanks-Decompiled) that I used to make this.

[Korean Random](https://koreanrandom.com/) where I found some answers.


## Copyright

See the [license](/LICENSE).