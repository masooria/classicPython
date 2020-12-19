
from secrets import token_bytes
from typing import Tuple


def random_key(length: int) -> int:
    tb: bytes = token_bytes(length)
    return int.from_bytes(tb, "big")


def encrypt(orig: str) -> Tuple[int, int]:
    orig_bytes: bytes = orig.encode()
    dummy: int = random_key(len(orig_bytes))
    orig_key: int = int.from_bytes(orig_bytes, "big")
    encrypted: int = orig_key ^ dummy
    return dummy, encrypted


def decrypt(key1: int, key2: int) -> str:
    decrypted: int = key1 ^ key2
    temp: bytes = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, "big")
    return temp.decode()


if __name__ == "__main__":
    key1, key2 = encrypt("masooria")
    result: str = decrypt(key1, key2)
    print(result)
