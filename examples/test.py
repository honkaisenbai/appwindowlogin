from cryptography.fernet import Fernet
from assets.encryption import EncryptionProcess


key_manually = b'e5SHVMqe7ob2qc9CAHD1o3nfqz7lYRxr1VotSAW2X5o='
data = "SDHSJALDSAHJDSALJDSAKL, World!"
gen = EncryptionProcess.generate_key()
encryp = EncryptionProcess.encrypt_data(data,gen)
decryp = EncryptionProcess.decrypt_data(encryp,gen)

print("Encrypted:", encryp)
print("Decrypted:", decryp)
