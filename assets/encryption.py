from cryptography.fernet import Fernet
import hashlib


class EncryptionProcess:
    # Two-way encryption (symmetric encryption)
    def generate_key():
        return Fernet.generate_key()

    def encrypt_data(data: str, key: bytes) -> bytes:
        f = Fernet(key)
        return f.encrypt(data.encode())

    def decrypt_data(token: bytes, key: bytes) -> str:
        f = Fernet(key)
        return f.decrypt(token).decode()
    
    # One-way encryption (hashing)
    def hash_data(data: str) -> str:
        return hashlib.sha256(data.encode()).hexdigest()