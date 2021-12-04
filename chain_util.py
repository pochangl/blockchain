import secp256k1
import uuid


def createPrivateKey():
    return secp256k1.PrivateKey()


def create_id():
    return uuid.uuid1()
