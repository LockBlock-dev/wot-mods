# PoC WoT Keylogger

![python](https://img.shields.io/badge/python-2.7.18-blue?link=https://www.python.org/downloads/release/python-2718/)

Proof of Concept of a keylogger mod in World of Tanks Desktop Client. It illustrates how the installation of a simple mod in your game can give attackers access to your email and password. It also gets the server region, country and ip address.

## Disclaimer

-   This mod is not intended to be used without the express consent of the owner of the computer where the World of Tanks client is running.

-   This mod should not be used for malicious purposes such as stealing accounts that do not belong to you.

-   This mod was made for educational purposes only in the scope of a Proof of Concept.

-   Using this mod outside of this scope can raise legal and ethical issues which I don't support nor can be held responsible for. You are responsible for your actions.

## Methods

Login with email and password : ![Implemented](https://img.shields.io/badge/-Implemented-success)

Login with email and remembered password : ![Implemented](https://img.shields.io/badge/-Implemented-success) it will ask for the password by removing the saved one

Login with social networks : ![Not implemented](https://img.shields.io/badge/-Not_implemented-red)

Login with Wargaming ID : ![Not implemented](https://img.shields.io/badge/-Not_implemented-red)

## How to use

-   Download [Python 2.7](https://www.python.org/downloads/release/python-2718/).

-   Download the project or clone it.

-   Edit the script with your webhook.

-   Compile and pack the mod in a .wotmod, you can use my own [mod packer](../auto-packer).

-   Move the .wotmod to your `World_of_Tanks/mods/X.X.X.X/` folder.

-   Start **World Of Tanks** and login with an email and a password.

-   Find the result inside your webhook channel.

## Debugging

If you have any problem, see what is going on in `World_of_Tanks/python.log`

## Credits

[WoT decompiled code](https://github.com/StranikS-Scan/WorldOfTanks-Decompiled) that I used to make this.

## Copyright

See the [license](/LICENSE).
