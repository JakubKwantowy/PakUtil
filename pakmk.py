#!/bin/python3
import pakutil
from pakutil import PakFile, PakEntry
from sys import argv
from os import listdir
from os.path import isdir, join

def main():
    print("PakUtil (C) 2025 JakubKwantowy")

    if len(argv) < 3:
        print(f'Usage: {argv[0]} <pakfile> <dir>')
        print(f'    Creates PAK from Directory')
        return
    
    PAKFILE = argv[1]
    DIR = argv[2]
    
    def getAbspath(p: str): return f'{DIR}{p}' if DIR.endswith('/') or not DIR else f'{DIR}/{p}'

    pakfile = PakFile()

    def recurseDir(dir: str = ''):
        curdir = getAbspath(dir)
        listing = listdir(curdir)
        for i in listing:
            path = join(curdir, i)
            pakpath = join(dir, i)
            if isdir(path): recurseDir(pakpath)
            else:
                with open(path, 'rb') as f: data = f.read() 
                pakentry = PakEntry(pakpath, data)
                pakfile.append(pakentry)

    recurseDir()
    with open(PAKFILE, 'wb') as f: pakutil.writePakFile(pakfile, f)

if __name__ == '__main__': main()
