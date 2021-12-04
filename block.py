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
