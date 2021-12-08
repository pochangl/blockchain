import chain_util
import json


def test_hash_consistency():
    data1 = {}
    data2 = {}

    data1['a'] = 1
    data1['b'] = 2

    data2['b'] = 2
    data2['a'] = 1

    assert json.dumps(data1) != json.dumps(data2)

    assert chain_util.hash(data1) == chain_util.hash(data1)
