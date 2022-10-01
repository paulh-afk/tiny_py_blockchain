import hashlib as hasher
from datetime import datetime


class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256()
        sha.update(str(self.index).encode() +
                   str(self.timestamp).encode() +
                   str(self.data).encode() +
                   str(self.previous_hash).encode())
        return sha.hexdigest()


def create_genesis_block():
    return Block(0, datetime.now(), "Genesis Block", "0")


def next_block(last_block, data):
    index = last_block.index + 1
    ts = datetime.now()
    prev_hash = last_block.hash
    return Block(index, ts, data, prev_hash)


blockchain = [create_genesis_block()]
nums_of_blocks_to_add = 25

for _ in range(nums_of_blocks_to_add):
    c_id = blockchain[-1].index + 1
    block_to_add = next_block(
        blockchain[-1], "This is the {} block".format(c_id))
    blockchain.append(block_to_add)

    print("Block #{} has been added to the blockchain!".format(
        c_id))
    print("Hash: {}\n".format(block_to_add.hash))
