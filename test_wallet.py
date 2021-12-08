from wallet import Wallet


def test_signature_and_verify():
    wallet = Wallet()

    data_hash = 'abcd'

    signature = wallet.sign(data_hash)
    help(signature)

    assert Wallet.verify(public_key=wallet.public_key,
                         signature=signature, data_hash=data_hash)
