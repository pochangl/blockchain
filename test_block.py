import pytest
from block import Block, DIFFICULTY


genesis = Block.genesis()

block1 = Block.mine_block(genesis, data='data')


def test_initialize_block():
    assert isinstance(block1.timestamp, int)
    assert block1.data == 'data'
    assert isinstance(block1.data, str)
    assert isinstance(block1.hash, str)
    assert isinstance(block1.last_hash, str)


def test_last_hash():
    assert block1.last_hash == genesis.hash


def test_difficulty():
    assert genesis.hash[:genesis.difficulty] == '0000'
    assert block1.hash[:block1.difficulty] == '0' * block1.difficulty


def test_dynamic_difficulty():
    block1 = Block.mine_block(genesis, 'abc')
    block2 = Block.mine_block(block1, 'abc')
    assert genesis.difficulty == 4
    assert block1.difficulty == 3
    assert block2.difficulty == 4
