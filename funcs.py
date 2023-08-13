from cryptography.fernet import Fernet, InvalidToken

SECRET_KEY = b'3nnm1tK4m32vBOrTDk95yleV27zf3QxUbjC3XHTib_4='

def encrypt_token(data):
    return Fernet(SECRET_KEY).encrypt(data.encode())

def decrypt_token(encrypted_token):
    return Fernet(SECRET_KEY).decrypt(encrypted_token).decode()

def getSessionData(session_url):
    pass
