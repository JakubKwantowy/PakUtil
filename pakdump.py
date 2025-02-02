#!/bin/python3
import pakutil
from sys import argv

def main():
    print("PakUtil (C) 2025 JakubKwantowy")

    if len(argv) < 2:
        print(f'Usage: {argv[0]} <pakfile>')
        print(f'    Prints all entries in PAK')
        return
    
    PAKFILE = argv[1]
    
    with open(PAKFILE, 'rb') as f: pak = pakutil.readPakFile(f)
    
    for i in pak.entries:
        print(i.path)

if __name__ == '__main__': main()
