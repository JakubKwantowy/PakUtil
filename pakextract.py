#!/bin/python3
import pakutil
from sys import argv

def main():
    print("PakUtil (C) 2025 JakubKwantowy")

    if len(argv) < 3:
        print(f'Usage: {argv[0]} <pakfile> <entry> [dir]')
        print(f'    Extracts entry from PAK')
        return
    
    PAKFILE = argv[1]
    ENTRY = argv[2]
    if len(argv) < 4: DIR = ''
    else: DIR = argv[3]
    
    with open(PAKFILE, 'rb') as f: pak = pakutil.readPakFile(f)
    
    entry = pak.get(ENTRY)
    if not entry: 
        print('Entry not found')
        exit(1)

    name = entry.path.split('/')[-1]
    path = f'{DIR}{name}' if DIR.endswith('/') or not DIR else f'{DIR}/{name}'
    
    with open(path, 'wb') as f: f.write(entry.data)

if __name__ == '__main__': main()
