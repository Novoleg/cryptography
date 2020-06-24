import hashlib
import ecdsa
import os
from binascii import hexlify


def random_secret_exponent(curve_order):
    while True:
        bytes = os.urandom(32)
        random_hex = bytes.hex()
        random_int = int(random_hex, 16)
        if random_int >= 1 and random_int < curve_order:
            return random_int


def generate_private_key():
    curve = ecdsa.curves.SECP256k1
    se = random_secret_exponent(curve.order)
    from_secret_exponent = ecdsa.keys.SigningKey.from_secret_exponent
    return from_secret_exponent(se, curve, hashlib.sha256).to_string()


def get_public_key_uncompressed(private_key_bytes):
    k = ecdsa.SigningKey.from_string(private_key_bytes, curve=ecdsa.SECP256k1)
    return b'\04' + k.get_verifying_key().to_string()  # 0x04 = uncompressed key prefix


private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1).to_string()
public_key = get_public_key_uncompressed(private_key)
print("Открытый ключ ECDSA: ", public_key.hex())
