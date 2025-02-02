from pakutil import PakFile, PakEntry, PAK_ENTRY_HEADER_SIZE
from typing import Any

def readPakFile(pak: Any) -> PakFile:
    '''
        Reads PAK file 'pak'
    '''
    if not hasattr(pak, 'read'):
        raise TypeError('Argument pak is not a valid file! (Method read not found)')
    data = pak.read()
    if not isinstance(data, bytes):
        raise ValueError('Data read from pak is not bytes!')
    return readPakBytes(data)

def readPakBytes(pak: bytes) -> PakFile:
    '''
        Reads PAK file data 'pak'
    '''
    if pak[:4] != b'PACK':
        raise ValueError('pak not a valid PAK file! (Missing id)')
    
    dir_offset = int.from_bytes(pak[4:8], 'little')
    dir_size = int.from_bytes(pak[8:12], 'little')
    dir_end = dir_offset + dir_size
    
    dir_bytes = pak[dir_offset:dir_end]
    dir_entrycount = int(dir_size / PAK_ENTRY_HEADER_SIZE)

    pakFile = PakFile()

    for i in range(dir_entrycount):
        o = i * PAK_ENTRY_HEADER_SIZE
        entry_bytes = dir_bytes[o:o+PAK_ENTRY_HEADER_SIZE]

        entry_path = entry_bytes[:56].split(b'\0')[0].decode('utf-8')
        entry_offset = int.from_bytes(entry_bytes[56:60], 'little')
        entry_size = int.from_bytes(entry_bytes[60:], 'little')
        entry_end = entry_offset + entry_size
        entry_data = pak[entry_offset:entry_end]
        
        entry = PakEntry(entry_path, entry_data)
        pakFile.append(entry)

    return pakFile
