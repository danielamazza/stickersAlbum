# stickersAlbum
Python program to manage a **stickers album**.

The file 'fig.txt' is an example that stores the IDs of the stickers and, for every ID, the amount of stickers you own.

For managing new stickers acquisitions and changes, from the shell you can digit:

```
python album.py fig.txt
```

If you want to initialize a new album, go to the python shell and digit:

```python
from album import *
crea_file([filename],[number of stickers that make up the album])

```

This creates a file [filename] that stores the IDs of the stickers and, for every ID, sets to 0 the amount of stickers you own.

For managing new stickers acquisitions and changes, from the shell you can digit:

```
python album.py [filename]
```
