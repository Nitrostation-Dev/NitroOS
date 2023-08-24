from cryptography.fernet import Fernet


def decrypt_str(key: str, enc_msg: str):
    return Fernet(key).decrypt(enc_msg).decode()
