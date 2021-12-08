import chain_util
from secp256k1 import PrivateKey
from settings import INITIAL_BALANCE


class Wallet:
    def __init__(self):
        self.balance = INITIAL_BALANCE
        self.private_key = chain_util.createPrivateKey()
        self.public_key = self.private_key.pubkey.serialize(False).hex()

    balance: int
    private_key: PrivateKey
    public_key: str

    def __str__(self) -> str:
        return '''Wallet -
        Balance: {balance}
        Public Key: {public_key}
        '''.format(**vars(self))

    def sign(self, dataHash: str) -> str:
        signature = self.private_key.ecdsa_sign(dataHash.encode())

        signature

    @classmethod
    def verify(cls, public_key: str, signature: str, data_hash: str):
        return chain_util.verify_signature(
            public_key=public_key, signature=signature, data_hash=data_hash)
