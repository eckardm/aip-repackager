# aip-repackager
Repackages Archivematica AIPs into "objects" and "metadata" packages.

Dependencies:
  * Python 2.7
  * [configparser](https://docs.python.org/3/library/configparser.html)
  * [unarMac](https://theunarchiver.com/command-line)
  * [p7zip_16.02](https://sourceforge.net/projects/p7zip/)
  
Example configuration file:

```
[to-do]
path = /path/to/TO-DO/dir

[doing]
path = /path/to/Doing/dir

[ready]
path = /path/to/Ready/dir

[p7zip_16.02]
path = /path/to/p7zip_16.02
```
