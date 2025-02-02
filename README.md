# PakUtil
A Python library for reading and writing Quake PAK files.

## Importing
The library is loaded using `import pakutil`  
All of PakUtil's classes and functions can be accessed via this module.

## Classes

### PakFile
The PakFile class has following attributes:
- `entries` - A list of entries from a PAK file.

and following Methods:
- `append` - Appends one or more entries to a PAK file.
- `get` - Gets an entry from a PAK file via its path. 
- `listDir` - Lists all entries within a given directory of a PAK file.

### PakEntry
The PakEntry class has following attributes:
- `path` - A PAK entry's path
- `data` - A PAK entry's data

## Fuctions

### readPakBytes
This function reads a PAK file from a bytes object.

### readPakFile
This function reads a PAK file from a file object.

### createPakBytes
This function creates a bytes object of a PAK file using the PAK format.

### writePakFile
This function writes a PAK file to a file object using the PAK format.
