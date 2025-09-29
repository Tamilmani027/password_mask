
from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as f:
        f.write(key)
    print("Key saved to 'secret.key'")

def encrypt_password(password):
    key = open("secret.key", "rb").read()
    f = Fernet(key)
    encrypted = f.encrypt(password.encode())
    print("Encrypted password to copy:")
    print(encrypted)

if __name__ == "__main__":
    generate_key()
    encrypt_password("aaaaaa")
