import hashlib
import time

hash = hashlib.sha256()

DIFFICULTY = 4


class Block:
    def __init__(self, timestamp: int, last_hash: str, hash: str, data: str, nonce: int):
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.hash = hash
        self.data = data
        self.nonce = nonce

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
        '''.format(**self.serialize())

    @classmethod
    def genesis(cls):
        g = cls(
            0, '', '', [], 0)
        g.mine()
        return g

    def mine(self):
        while True:
            self.hash = self.get_hash()
            if (self.hash[:DIFFICULTY] == '0' * DIFFICULTY):
                break
            self.nonce += 1

    @classmethod
    def mine_block(cls, last_block: 'Block', data: str):
        nonce = 0
        block = cls(
            nonce=nonce,
            timestamp=time.time_ns(),
            last_hash=last_block.hash,
            hash='',
            data=data,
        )
        block.mine()
        return block

    @classmethod
    def hash(cls, **kwargs):
        data = '{timestamp}{last_hash}{data}{nonce}'.format(**kwargs)
        m = hashlib.sha256()
        m.update(data.encode())
        return m.hexdigest()

    def __eq__(self, block: 'Block'):
        return self.serialize() == block.serialize()

    def get_hash(self):
        return Block.hash(timestamp=self.timestamp, last_hash=self.last_hash, data=self.data, nonce=self.nonce)

    def serialize(self) -> dict:
        return dict(
            timestamp=self.timestamp,
            last_hash=self.last_hash,
            hash=self.hash,
            data=self.data,
            nonce=self.nonce,
        )
