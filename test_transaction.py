from transaction import Transaction
from wallet import Wallet


def test_outputs_the_amount():
    'outputs the amount subtracted from the wallet'
    wallet = Wallet()
    wallet.balance = 500
    recipient = 'rec'

    transaction = Transaction.newTransaction(
        senderWallet=wallet, recipient=recipient, amount=50,
    )

    record = list(
        filter(lambda o: o['address'] == wallet.public_key, transaction.outputs))[0]

    assert record['amount'] == 450

    record = list(
        filter(lambda o: o['address'] == recipient, transaction.outputs))[0]

    assert record['amount'] == 50


def test_exceed():
    wallet = Wallet()
    wallet.balance = 500
    recipient = 'rec'
    transaction = Transaction.newTransaction(
        senderWallet=wallet, recipient=recipient, amount=5000,
    )
    assert transaction is None
