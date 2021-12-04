from block import Block


class Blockchain:
    def __init__(self):
        self.chain = [Block.genesis()]

    chain: list

    @property
    def last_block(self):
        return self.chain[-1]

    def add_block(self, data: str):
        block = Block.mine_block(self.last_block, data)

        self.chain.append(block)
