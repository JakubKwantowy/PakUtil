#!/bin/python3
import pakutil
from sys import argv
from os import mkdir

def main():
    print("PakUtil (C) 2025 JakubKwantowy")

    if len(argv) < 2:
        print(f'Usage: {argv[0]} <pakfile> [dir]')
        print(f'    Extracts all entries from PAK')
        return
    
    PAKFILE = argv[1]
    if len(argv) < 3: DIR = ''
    else: DIR = argv[2]
    
    with open(PAKFILE, 'rb') as f: pak = pakutil.readPakFile(f)
    
    def getAbspath(p: str): return f'{DIR}{p}' if DIR.endswith('/') or not DIR else f'{DIR}/{p}'

    madedirs = []

    for i in pak.entries:
        name = i.path
        
        dirs = name.split('/')[:-1]
        dir = ''
        for j in dirs:
            dir += f'{j}/'
            if dir in madedirs: continue
            madedirs.append(dir)
            try:
                mkdir(getAbspath(dir))
            except FileExistsError: pass

        path = getAbspath(name)
        with open(path, 'wb') as f: f.write(i.data)

if __name__ == '__main__': main()
