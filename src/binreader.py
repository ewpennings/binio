import os
from struct import unpack


class Reader:
    def __init__(self, filename):
        self._fh = open(filename, 'rb')
        if self._fh:
            self._fh.seek(0, os.SEEK_END)
            self._file_size = self._fh.tell()
            self._fh.seek(0)

    def close(self):
        if self._fh:
            self._fh.close()

    def read_int32(self):
        return unpack('>i', self._fh.read(4))[0]
