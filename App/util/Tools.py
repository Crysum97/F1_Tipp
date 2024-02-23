import hashlib


def hash_sha256(input_str):
    sha_256 = hashlib.sha256()
    sha_256.update(input_str.encode("utf-8"))
    return sha_256.hexdigest()
