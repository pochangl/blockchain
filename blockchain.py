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

    def add_block(self, data: str) -> None:
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

    def replace_chain(self, newChain: 'Blockchain') -> None:
        if (len(newChain.chain) <= len(self.chain)):
            return
        elif (not self.is_valid_chain(newChain)):
            return
        self.chain = newChain.chain

    def __eq__(self, block: 'Blockchain') -> bool:
        if len(self.chain) != len(block.chain):
            return False

        for a, b in zip(self.chain, block.chain):
            if a != b:
                return False

        return True
