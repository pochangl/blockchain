from chain_util import createPrivateKey
from settings import INITIAL_BALANCE


class Wallet:
    def __init__(self):
        self.balance = INITIAL_BALANCE
        self.private_key = createPrivateKey()
        self.public_key = self.private_key.pubkey.serialize(False).hex()

    balance: int
    private_key: str
    public_key: str

    def __str__(self) -> str:
        return '''Wallet -
        Balance: {balance}
        Public Key: {public_key}
        '''.format(**vars(self))
