# stickersAlbum
Python program to manage a **stickers album**.

The file 'fig.txt' is an example that stores the IDs of the stickers and, for every ID, the amount of stickers you own.

There are two different manage type:
 1. from the **shell**
 2. **graphically**

## From the shell
For managing new stickers acquisitions and changes **from the shell** you can digit:

```
python3 album.py fig.txt
```

If you want to initialize a new album, go to the python shell and digit:

```python3
from album import *
crea_file([filename],[number of stickers that make up the album])

```

This creates a file [filename] that stores the IDs of the stickers and, for every ID, sets to 0 the amount of stickers you own.

For managing new stickers acquisitions and changes, from the shell you can digit:

```
python3 album.py [filename]
```
## Graphically
The fig.txt file is the record of the stickers.
The images folder contains two images for every sticker, one normal an one semitransparent (for representing missing sticker).
For launching the program from the shell digit: 

```
python3 graficaAlbumIntegrato.py
```

