# Rename torrent from hash

If your torrent client (like qBittorrent) renamed your torrent's filename to its hash and you want to rename it back to torrent's name, this Python 3 script will help you do that.

## Optimization
make sure you have python installed.
put torrent file in input folder,and execution "run.py".Processed files will show in the"output"folder.
if miss requirements,just run Request Dependency.py(test yet)

## Dependency

* [torrentool](https://github.com/idlesign/torrentool)
* [tqdm](https://tqdm.github.io)

To install, run this command:
```
pip install --upgrade -r requirements.txt
```

## Usage

Run the script with this command:

```
usage: main.py [-h] [-d DEST] [-r] input

Rename torrent hash file to its original name.

positional arguments:
  input                 Path to input folder

options:
  -h, --help            show this help message and exit
  -d DEST, --dest DEST  Path to destination folder
  -r, --remove          Remove original file
```

Note: If torrent name already exist, it will add a number before the ``.torrent`` extension.
