import chain_util
import time
from wallet import Wallet


class Transaction:
    def __init__(self):
        self.id = chain_util.create_id()
        self.input = None
        self.outputs = []

    @classmethod
    def newTransaction(cls, sender_wallet: Wallet, recipient: str, amount: int):
        transaction = cls()
        if amount > sender_wallet.balance:
            print(
                'Amount: {amount} exceeds balance.'.format(amount=amount))
            return

        transaction.outputs.append({
            'amount': sender_wallet.balance - amount,
            'address': sender_wallet.public_key,
        })
        transaction.outputs.append({
            'amount': amount,
            'address': recipient,
        })
        Transaction.sign_transaction(transaction, sender_wallet)
        return transaction

    @classmethod
    def sign_transaction(cls, transaction, sender_wallet: Wallet):
        transaction.input = dict(
            timestamp=time.time_ns(),
            amount=sender_wallet.balance,
            address=sender_wallet.public_key,
            signature=sender_wallet.sign(chain_util.hash(transaction.outputs))
        )
