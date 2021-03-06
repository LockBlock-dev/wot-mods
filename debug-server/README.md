# WoT Debug server

![python](https://img.shields.io/badge/python-2.7.18-blue?link=https://www.python.org/downloads/release/python-2718/)

The purpose of this mod is to provide you a server in the background that listens for local connection to provide an access to the BigWorld and Scaleform engines. This might be useful for figuring how things work.

The server runs on `127.0.0.1` port `2222`. You can edit these in [server.py](./res/scripts/client/gui/mods/mod_server.py) and [client.py](./client.py).


## How to use

-   Download [Python 2.7](https://www.python.org/downloads/release/python-2718/)

-   Download the project or clone it

-   Compile and pack the mod in a .wotmod, you can use my own [mod packer](../auto-packer).

-   Move the .wotmod to your `World_of_Tanks/mods/X.X.X.X/` folder.

-   Run the client in a command prompt:
```bash
python2 client.py
```

-   Start **World Of Tanks**, hopefully the server will starts

-   You can now run python commands:

```
Request > 'hello'
Received > hello

Request > 1+1
Received > 2

Request > import messenger
Received > Success
Request > gui = messenger.MessengerEntry.g_instance.gui
Received > Success
Request > gui.addClientMessage('hello gui', True) #display a client-side message in the battle chat
Received > None

Request > import BigWorld
Received > Success
Request > BigWorld.player().name #displays player username
Received > your-username-here

Request > QUIT #the server will stops
```


## Debugging

If you have any problem, see what is going on in `World_of_Tanks/python.log`


## Credits

Original [debug server](https://github.com/juho-p/wot-debugserver) I used to make my own.


## Copyright

See the [license](/LICENSE).