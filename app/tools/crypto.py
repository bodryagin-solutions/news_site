from hashlib import sha256


def get_hash(password: str):
    return sha256(password.encode("utf-8")).hexdigest()