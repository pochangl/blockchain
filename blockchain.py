from block import Block


class Blockchain:
    def __init__(self):
        self.chain = [Block.genesis()]

    chain: list

    @property
    def last_block(self) -> Block:
        return self.chain[-1]

    @property
    def genesis(self) -> Block:
        return self.chain[0]

    def add_block(self, data: str):
        block = Block.mine_block(self.last_block, data)

        self.chain.append(block)

    def is_valid_chain(self, chain2: 'Blockchain') -> bool:
        print('testing')

        if chain2.genesis != Block.genesis():
            return False

        last_block = chain2.genesis

        for block in chain2.chain[1:]:
            if block.last_hash != last_block.hash or block.hash != block.get_hash():
                return False
            last_block = block

        return True
