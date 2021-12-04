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


def test_validates_a_valid_chain():
    bc1 = Blockchain()
    bc2 = Blockchain()

    bc2.add_block('foo')

    assert bc1.is_valid_chain(bc2)


def test_invalidate_corrupt_genesis_block():
    bc1 = Blockchain()
    bc2 = Blockchain()

    bc2.genesis.data = 'invalid'

    assert not bc1.is_valid_chain(bc2)


def test_invalid_corrupt_chain():
    bc1 = Blockchain()
    bc2 = Blockchain()

    bc2.add_block('foo')
    bc2.chain[1].data = 'not foo'

    assert not bc1.is_valid_chain(bc2)


def test_replace_chain_with_valid_chain():
    bc1 = Blockchain()
    bc2 = Blockchain()
    bc2.add_block('goo')

    bc1.replace_chain(bc2)

    assert bc1 == bc2


def test_does_not_replace_chain_with_shorter_length():
    bc1 = Blockchain()
    bc2 = Blockchain()

    bc1.add_block('d2')

    bc1.replace_chain(bc2)

    assert bc1 != bc2


def test_does_not_replace_chain_with_equal_length():
    bc1 = Blockchain()
    bc2 = Blockchain()

    bc2.add_block('d2')
    bc1.add_block('d1')

    bc1.replace_chain(bc2)

    assert bc1 != bc2


def test_serialize_deserialize():
    bc1 = Blockchain()

    bc2 = Blockchain(bc1.serialize())

    assert bc1 == bc2
