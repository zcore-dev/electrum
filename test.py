from binascii import hexlify,unhexlify
import binascii
import struct
import array

import lib.zcore as zcore
import time

ts = time.time()
hts = ts.hex()
print(ts)
print(hts)
print(int(bytes.fromhex(hts)))