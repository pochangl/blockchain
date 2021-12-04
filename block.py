import hashlib
import time

hash = hashlib.sha256()


class Block:
    def __init__(self, timestamp: int, last_hash: str, hash: str, data: str):
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.hash = hash
        self.data = data

    timestamp: int
    last_hash: str
    hash: str
    data: str

    def __str__(self):
        return '''Block -
        Timestamp: {timestamp}
        Last Hash: {last_hash}
        Hash: {hash}
        data: {data}
        '''.format(**vars(self))

    @classmethod
    def genesis(cls):
        return cls(0, '', 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855', [])

    @classmethod
    def mine_block(cls, last_block: 'Block', data: str):
        timestamp = time.time_ns()
        last_hash = last_block.hash
        hash = Block.hash(timestamp=timestamp, last_hash=last_hash, data=data)
        return cls(timestamp=timestamp, last_hash=last_hash, hash=hash, data=data)

    @classmethod
    def hash(cls, **kwargs):
        data = '{timestamp}{last_hash}{data}'.format(**kwargs)
        m = hashlib.sha256()
        m.update(data.encode())
        return m.hexdigest()

    def __eq__(self, block: 'Block'):
        return self.timestamp == block.timestamp and self.data == block.data and self.hash == block.hash and self.last_hash == block.last_hash

    def get_hash(self):
        return Block.hash(timestamp=self.timestamp, last_hash=self.last_hash, data=self.data)

    def serialize(self) -> dict:
        return dict(
            timestamp=self.timestamp,
            last_hash=self.last_hash,
            hash=self.hash,
            data=self.data,
        )
