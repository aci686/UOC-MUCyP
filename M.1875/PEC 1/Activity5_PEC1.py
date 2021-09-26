# Please use Python 3 version

import sys
# import SHA-256 hash function library


# Version (4 bytes) - version = 1
version =

# Previous hash (32 bytes) - Double sha256 of your first name = sha256(sha256("firstname"))
prev_hash =

# Merkle root (32 bytes)
merkle_root = '6dbba50b72ad0569c2449090a371516e3865840e905483cac0f54d96944eee28'

# Bits (4 bytes)
bits = '1e0fffff'

# Target
target = '00000fffff000000000000000000000000000000000000000000000000000000'

# Nonce (4 bytes) - nonce = 0
nonce =


# Function - Convert transactions from big endian into little endian (hex)
def big_endian_to_little_endian(transaction):
    # CODE HERE


# Function - PoW simulation
def proof_of_work(version, prev_hash, merkle_root, target):
    # Iterate over the nonce to simulate real performance
    for(...):
        timestamp =
        nonce =
        # Header = {version, prev_hash, merkle_root, timestamp, bits, nonce}
        header =
        block_hash = sha256(sha256(header))
        # Check if the block_hash is below the given target
        if():
            # return block_hash

proof_of_work()
