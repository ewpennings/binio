from binio import Reader, Writer
from random import randint

filename = 'test.dat'

writer = Writer(filename)

# Write upper limits
writer.write_int8(127)
writer.write_int16(32767)
writer.write_int24(8388607)
writer.write_int32(2147483647)
writer.write_uint8(255)
writer.write_uint16(65535)
writer.write_uint24(1677216)
writer.write_uint32(4294967295)

# Write lower limits
writer.write_int8(-128)
writer.write_int16(-32768)
writer.write_int24(-8388608)
writer.write_int32(-2147483648)
writer.write_uint8(0)
writer.write_uint16(0)
writer.write_uint24(0)
writer.write_uint32(0)

# Write random values
r1 = randint(-128, 127)
r2 = randint(-32768, 32767)
r3 = randint(-8388608, 8388607)
r4 = randint(-2147483648, 2147483647)
r5 = randint(0, 255)
r6 = randint(0, 65535)
r7 = randint(0, 1677216)
r8 = randint(0, 4294967295)
writer.write_int8(r1)
writer.write_int16(r2)
writer.write_int24(r3)
writer.write_int32(r4)
writer.write_uint8(r5)
writer.write_uint16(r6)
writer.write_uint24(r7)
writer.write_uint32(r8)

writer.close()
reader = Reader(filename)

# Read upper limits
assert(reader.read_int8() == 127)
assert(reader.read_int16() == 32767)
assert(reader.read_int24() == 8388607)
assert(reader.read_int32() == 2147483647)
assert(reader.read_uint8() == 255)
assert(reader.read_uint16() == 65535)
assert(reader.read_uint24() == 1677216)
assert(reader.read_uint32() == 4294967295)

# Read lower limits
assert(reader.read_int8() == -128)
assert(reader.read_int16() == -32768)
assert(reader.read_int24() == -8388608)
assert(reader.read_int32() == -2147483648)
assert(reader.read_uint8() == 0)
assert(reader.read_uint16() == 0)
assert(reader.read_uint24() == 0)
assert(reader.read_uint32() == 0)

# Read random values
assert(reader.read_int8() == r1)
assert(reader.read_int16() == r2)
assert(reader.read_int24() == r3)
assert(reader.read_int32() == r4)
assert(reader.read_uint8() == r5)
assert(reader.read_uint16() == r6)
assert(reader.read_uint24() == r7)
assert(reader.read_uint32() == r8)
