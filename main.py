from block import Block

genesis = Block.genesis()
print(genesis)

m = Block.mine_block(last_block=genesis, data='data')
print(m)
