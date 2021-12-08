import hashlib
import time
from settings import DIFFICULTY, MINE_RATE
import chain_util


class Block:
    def __init__(self, timestamp: int, last_hash: str, hash: str, data: str, nonce: int, difficulty: int):
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.hash = hash
        self.data = data
        self.nonce = nonce
        self.difficulty = difficulty

    timestamp: int
    last_hash: str
    hash: str
    data: str
    nonce: int

    def __str__(self):
        return '''Block -
        Timestamp: {timestamp}
        Last Hash: {last_hash}
        Hash: {hash}
        data: {data}
        nonce: {nonce}
        difficulty: {difficulty}
        '''.format(**self.serialize())

    @classmethod
    def genesis(cls):
        g = cls(
            0, '', '', [], 0, difficulty=DIFFICULTY)
        g.mine()
        return g

    @classmethod
    def mine_block(cls, last_block: 'Block', data: str):
        nonce = 0
        timestamp = time.time_ns()
        difficulty = Block.adjust_difficulty(last_block, timestamp)
        print(last_block.difficulty, difficulty)
        block = cls(
            nonce=nonce,
            timestamp=time.time_ns(),
            last_hash=last_block.hash,
            hash='',
            data=data,
            difficulty=difficulty,
        )
        block.mine()
        return block

    @classmethod
    def adjust_difficulty(cls, last_block: 'Block', current_time: int) -> int:
        if (last_block.timestamp + MINE_RATE > current_time):
            return last_block.difficulty + 1
        else:
            return last_block.difficulty - 1

    @classmethod
    def hash(cls, **kwargs):
        data = '{timestamp}{last_hash}{data}{nonce}{difficulty}'.format(
            **kwargs)
        return chain_util.hash(data)

    def mine(self):
        while True:
            self.hash = self.get_hash()
            if (self.hash[:self.difficulty] == '0' * self.difficulty):
                break
            self.nonce += 1

    def __eq__(self, block: 'Block'):
        return self.serialize() == block.serialize()

    def get_hash(self):
        data = self.serialize()
        data.pop('hash')
        return Block.hash(**data)

    def serialize(self) -> dict:
        return dict(
            timestamp=self.timestamp,
            last_hash=self.last_hash,
            hash=self.hash,
            data=self.data,
            nonce=self.nonce,
            difficulty=self.difficulty,
        )
