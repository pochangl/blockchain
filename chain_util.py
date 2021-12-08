import hashlib
import json
import secp256k1
import uuid


def createPrivateKey():
    return secp256k1.PrivateKey()


def create_id():
    return uuid.uuid1()


def hash(data):
    h = hashlib.sha256()
    txt = json.dumps(data, sort_keys=True)
    h.update(txt.encode())
    return h.hexdigest()


def verify_signature(public_key: str, signature: str, data_hash):
    key = secp256k1.PublicKey(bytes.fromhex(public_key), raw=True)
    return key.ecdsa_verify(data_hash, bytes.fromhex(signature), raw=True)
