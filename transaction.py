from chain_util import create_id
from wallet import Wallet


class Transaction:
    def __init__(self):
        self.id = create_id()
        self.input = None
        self.outputs = []

    @classmethod
    def newTransaction(cls, senderWallet: Wallet, recipient: str, amount: int):
        transaction = cls()
        if amount > senderWallet.balance:
            print(
                'Amount: {amount} exceeds balance.'.format(amount=amount))
            return

        transaction.outputs.append({
            'amount': senderWallet.balance - amount,
            'address': senderWallet.public_key,
        })
        transaction.outputs.append({
            'amount': amount,
            'address': recipient,
        })
        return transaction
