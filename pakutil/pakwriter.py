from pakutil import PakFile, PakEntry, PAK_HEADER_SIZE
from typing import Any

def writePakFile(pakfile: PakFile, pak: Any):
    '''
        Writes PAK bytes from 'pakfile' to 'pak'
    '''
    if not hasattr(pak, 'write'):
        raise TypeError('Argument pak is not a valid file! (Method write not found)')
    data = createPakBytes(pakfile)
    pak.write(data)

def createPakBytes(pakfile: PakFile) -> bytes:
    '''
        Creates PAK bytes from 'pakfile'
    '''
    pak_bytes = bytearray()

    header_bytes = bytearray(b'PACK')
    data_bytes = bytearray()
    dir_bytes = bytearray()

    data_idx = PAK_HEADER_SIZE

    for i in pakfile.entries:
        entry_path_bytes = i.path.encode('utf-8')[:55].ljust(56, b'\0')
        entry_offset_bytes = int.to_bytes(data_idx, 4, 'little')
        entry_size = len(i.data)
        entry_size_bytes = int.to_bytes(entry_size, 4, 'little')
        
        entry_bytes = bytearray()
        entry_bytes.extend(entry_path_bytes)
        entry_bytes.extend(entry_offset_bytes)
        entry_bytes.extend(entry_size_bytes)

        data_bytes.extend(i.data)
        data_idx += entry_size
        dir_bytes.extend(entry_bytes)

    header_offset_bytes = int.to_bytes(data_idx, 4, 'little')
    header_size_bytes = int.to_bytes(len(dir_bytes), 4, 'little')

    header_bytes.extend(header_offset_bytes)
    header_bytes.extend(header_size_bytes)

    pak_bytes.extend(header_bytes)
    pak_bytes.extend(data_bytes)
    pak_bytes.extend(dir_bytes)

    return bytes(pak_bytes)
