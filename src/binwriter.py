from struct import pack


class Writer:
    def __init__(self, filename):
        self._fh = open(filename, 'wb')

    def close(self):
        if self._fh:
            self._fh.close()

    def write_int32(self, val):
        self._fh.write(pack('>i', val))
