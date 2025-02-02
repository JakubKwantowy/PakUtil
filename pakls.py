#!/bin/python3
import pakutil
from sys import argv

def main():
    print("PakUtil (C) 2025 JakubKwantowy")

    if len(argv) < 2:
        print(f'Usage: {argv[0]} <pakfile> [dir]')
        print(f'    Prints directory listing in PAK')
        return
    
    PAKFILE = argv[1]
    if len(argv) < 3: DIR = ''
    else: DIR = argv[2]
    
    with open(PAKFILE, 'rb') as f: pak = pakutil.readPakFile(f)
    
    for i in pak.listDir(DIR):
        print(i)

if __name__ == '__main__': main()
