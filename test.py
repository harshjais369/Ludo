from cryptography.fernet import Fernet

# Replace this with your secret key (keep it safe and private)
secret_key = b'3nnm1tK4m32vBOrTDk95yleV27zf3QxUbjC3XHTib_4='

# Print the generated key
print("Generated Fernet Key:", secret_key)

# Client Side (Telegram Bot)
# def encrypt_token(user_id, timestamp):
#     data = f'{user_id}:{timestamp}'.encode()
#     cipher_suite = Fernet(secret_key)
#     encrypted_token = cipher_suite.encrypt(data)
#     return encrypted_token

def encrypt_token(data):
    cipher_suite = Fernet(secret_key)
    encrypted_token = cipher_suite.encrypt(data.encode())
    return encrypted_token

def decrypt_token(encrypted_token):
    cipher_suite = Fernet(secret_key)
    decrypted_data = cipher_suite.decrypt(encrypted_token).decode()
    return decrypted_data

# Server Side (Game Server)
def decrypt_token(encrypted_token):
    cipher_suite = Fernet(secret_key)
    decrypted_data = cipher_suite.decrypt(encrypted_token).decode()
    user_id, timestamp = decrypted_data.split(':')
    return user_id, timestamp

print(decrypt_token(secret_key))
