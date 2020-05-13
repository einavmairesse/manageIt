import hashlib
import uuid


class Security:

    @staticmethod
    def get_string_hash(string_to_hash: str):
        return hashlib.sha3_256(bytes(string_to_hash, encoding='utf-8')).hexdigest()