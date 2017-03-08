import os
from struct import pack, unpack


class ByteOrder:
    NATIVE = 0
    LITTLE_ENDIAN = 1
    BIG_ENDIAN = 2

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        if self.value == ByteOrder.NATIVE:
            return '='
        elif self.value == ByteOrder.LITTLE_ENDIAN:
            return '<'
        elif self.value == ByteOrder.BIG_ENDIAN:
            return '>'

    def __eq__(self, other):
        return self.value == other.value


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

    def is_eof(self):
        return self._fh.tell() == self._file_size

    def read_int8(self, byte_order=ByteOrder(ByteOrder.BIG_ENDIAN)):
        fmt = "{0}b".format(byte_order)
        return unpack(fmt, self._fh.read(1))[0]

    def read_int16(self, byte_order=ByteOrder(ByteOrder.BIG_ENDIAN)):
        fmt = "{0}h".format(byte_order)
        return unpack(fmt, self._fh.read(2))[0]

    def read_int24(self, byte_order=ByteOrder(ByteOrder.BIG_ENDIAN)):
        unsigned = self.read_uint24(byte_order)
        return unsigned if not (unsigned & 0x800000) else unsigned - 0x1000000

    def read_int32(self, byte_order=ByteOrder(ByteOrder.BIG_ENDIAN)):
        fmt = "{0}i".format(byte_order)
        return unpack(fmt, self._fh.read(4))[0]

    def read_uint8(self, byte_order=ByteOrder(ByteOrder.BIG_ENDIAN)):
        fmt = "{0}B".format(byte_order)
        return unpack(fmt, self._fh.read(1))[0]

    def read_uint16(self, byte_order=ByteOrder(ByteOrder.BIG_ENDIAN)):
        fmt = "{0}H".format(byte_order)
        return unpack(fmt, self._fh.read(2))[0]

    def read_uint24(self, byte_order=ByteOrder(ByteOrder.BIG_ENDIAN)):
        fmt = "{0}i".format(byte_order)
        buf = self._fh.read(3)
        if byte_order.value == ByteOrder.LITTLE_ENDIAN:
            buf += b'\x00'
        else:
            buf = b'\x00' + buf
        return unpack(fmt, buf)[0]

    def read_uint32(self, byte_order=ByteOrder(ByteOrder.BIG_ENDIAN)):
        fmt = "{0}I".format(byte_order)
        return unpack(fmt, self._fh.read(4))[0]


class Writer:
    def __init__(self, filename):
        self._fh = open(filename, 'wb')

    def close(self):
        if self._fh:
            self._fh.close()

    def write_int8(self, val, byte_order=ByteOrder(ByteOrder.BIG_ENDIAN)):
        fmt = "{0}b".format(byte_order)
        self._fh.write(pack(fmt, val))

    def write_int16(self, val, byte_order=ByteOrder(ByteOrder.BIG_ENDIAN)):
        fmt = "{0}h".format(byte_order)
        self._fh.write(pack(fmt, val))

    def write_int24(self, val, byte_order=ByteOrder(ByteOrder.BIG_ENDIAN)):
        fmt = "{0}i".format(byte_order)
        buf = pack(fmt, val)
        if byte_order.value == ByteOrder.LITTLE_ENDIAN:
            buf = buf[:-1]
        else:
            buf = buf[1:]
        self._fh.write(buf)

    def write_int32(self, val, byte_order=ByteOrder(ByteOrder.BIG_ENDIAN)):
        fmt = "{0}i".format(byte_order)
        self._fh.write(pack(fmt, val))

    def write_uint8(self, val, byte_order=ByteOrder(ByteOrder.BIG_ENDIAN)):
        fmt = "{0}B".format(byte_order)
        self._fh.write(pack(fmt, val))

    def write_uint16(self, val, byte_order=ByteOrder(ByteOrder.BIG_ENDIAN)):
        fmt = "{0}H".format(byte_order)
        self._fh.write(pack(fmt, val))

    def write_uint24(self, val, byte_order=ByteOrder(ByteOrder.BIG_ENDIAN)):
        fmt = "{0}I".format(byte_order)
        buf = pack(fmt, val)
        if byte_order.value == ByteOrder.LITTLE_ENDIAN:
            buf = buf[:-1]
        else:
            buf = buf[1:]
        self._fh.write(buf)

    def write_uint32(self, val, byte_order=ByteOrder(ByteOrder.BIG_ENDIAN)):
        fmt = "{0}I".format(byte_order)
        self._fh.write(pack(fmt, val))
