# Mod auto-packer

![python](https://img.shields.io/badge/python-2.7.18-blue?link=https://www.python.org/downloads/release/python-2718/)

A tiny script to compile and exports your world of tanks mod easily.
It compiles and exports your mod as a .wotmod with its meta.xml file.

## How to use

-   Download [Python 2.7](https://www.python.org/downloads/release/python-2718/)

-   Download the project or clone it

-   The parameters are the following:

    -   `-u` | `--username` : developer name
    -   `-n` | `--name` : mod name, default: `mod`
    -   `-v` | `--version` : mod version, default: `1.0.0`
    -   `-d` | `--description` : mod description, default: `no description`
    -   `-f` | `--folder` : res folder path, default: `./res`

-   Run `python packer.py -u your_name etc...`

-   Find the packed mod inside `/build`

## Copyright

See the [license](/LICENSE).
