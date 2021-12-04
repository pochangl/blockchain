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
