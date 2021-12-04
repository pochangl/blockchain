from blockchain import Blockchain

from block import Block


def test_start_with_genesis():
    bc = Blockchain()
    assert bc.chain[0] == Block.genesis()


def test_add_data():
    bc = Blockchain()
    data = 'foo'
    bc.add_block(data)

    assert bc.last_block.data == data
