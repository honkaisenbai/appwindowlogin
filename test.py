from cryptography.fernet import Fernet
import hashlib

def generate_key():
    return Fernet.generate_key()

def encrypt_data(data: str, key: bytes) -> bytes:
    f = Fernet(key)
    return f.encrypt(data.encode())

def decrypt_data(token: bytes, key: bytes) -> str:
    f = Fernet(key)
    return f.decrypt(token).decode()

key_manually = b'e5SHVMqe7ob2qc9CAHD1o3nfqz7lYRxr1VotSAW2X5o='
data = "Hello, World!"

encryp = encrypt_data(data,generate_key())
decryp = decrypt_data(encryp,generate_key())

print("Encrypted:", encryp)
print("Decrypted:", decryp)
