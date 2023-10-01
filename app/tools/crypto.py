from hashlib import sha256
from random import choice
import string


SALT_LENGHT = 12


def get_salt(lenght: int):
    return ''.join([choice(string.ascii_lowercase) for i in range(lenght)])


def get_hash(password: str, salt: str):
    hashed_password =  sha256((salt+password).encode("utf-8")).hexdigest()
    return  salt + "@" + hashed_password


def verify_password(plain_password:str, hashed_password: str):
    salt, password = hashed_password.split("@")
    return get_hash(plain_password, salt) == hashed_password


# soem _func