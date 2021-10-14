# Please use Python 3 version

import sys
# import SHA-256 hash function library
from hashlib import sha256
import binascii
import time
import struct

# Version (4 bytes) - version = 1
version = 1

# Previous hash (32 bytes) - Double sha256 of your first name = sha256(sha256("firstname"))
prev_hash = sha256(sha256('Aaron'.encode('utf-8')).digest()).hexdigest()[::-1]

# Merkle root (32 bytes)
merkle_root = '6dbba50b72ad0569c2449090a371516e3865840e905483cac0f54d96944eee28'

# Bits (4 bytes)
bits = '1e0fffff'

# Target
target = '00000fffff000000000000000000000000000000000000000000000000000000'

# Nonce (4 bytes) - nonce = 0
nonce = 0

# Function - Convert values from big endian into little endian (hex)
def big_endian_to_little_endian(value):
    # CODE HERE
    return (binascii.unhexlify(value)[::-1])

# Function - PoW simulation
# Don't forget to use the "big_endian_to_little_endian(value)" function!
# Don't forget to save the nonce and timestamp values!
def proof_of_work():
    # Iterate over the nonce to simulate real performance
    nonce = 0
    for _ in iter(int, 1):
        v = binascii.hexlify(struct.Struct('<L').pack(version)).decode()
        m = binascii.hexlify(big_endian_to_little_endian(merkle_root.encode('utf-8'))).decode()
        s_timestamp = time.time()
        t = binascii.hexlify(struct.Struct('<L').pack(int(s_timestamp))).decode()
        b = binascii.hexlify(big_endian_to_little_endian(bits.encode('utf-8'))).decode()
        n = binascii.hexlify(struct.Struct('<L').pack(nonce)).decode()
        header = str(v) + prev_hash + str(m) + str(t) + bits + str(n)
        block_hash = sha256(sha256(header.encode('utf-8')).digest()).hexdigest()
        # Check if the block_hash is below the given target
        if str(block_hash) < target:
            print('Version: ' + str(v))
            print('Prev Hash: ' + str(prev_hash))
            print('Merkle Root: ' + str(m))
            print('Timestamp: ' + str(t))
            print('Bits: ' + str(b))
            print('Nonce: ' + str(n))
            print('Header: ' + str(header))
            return block_hash
        nonce += 1

# Print block hash
print(proof_of_work())
