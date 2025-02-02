from typing import Iterable

PAK_ENTRY_HEADER_SIZE = 64
PAK_HEADER_SIZE = 12

class PakFile:
    def __init__(self):
        self.entries: 'list[PakEntry]' = []

    def append(self, *entries: 'Iterable[PakEntry]'):
        self.entries.extend(entries)

    def get(self, path: str) -> 'PakEntry | None':
        for i in self.entries:
            if i.path == path: return i

    def listDir(self, dir: str = '') -> 'list[str]':
        dirlist = []
        if dir: dir += '/'
        for i in self.entries:
            if not i.path.startswith(dir): continue
            path = i.path[len(dir):].split('/')[0]
            if path in dirlist: continue
            dirlist.append(path)
        return dirlist

class PakEntry:
    def __init__(self, path: str, data: bytes):
        self.path = path
        self.data = data
