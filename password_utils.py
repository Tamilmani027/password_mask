from cryptography.fernet import Fernet

class FakeStr(str):
	def __str__(self):
		return "****"

	def __repr__(self):
		return "****"

def load_key():
	return open("secret.key", "rb").read()

def decrypt_password(encrypted_password):
	key = load_key()
	f = Fernet(key)
	decrypted = f.decrypt(encrypted_password).decode()
	return FakeStr(decrypted)

def get_decrypted_password():
	encrypted_password =b'gAAAAABoEGr7ajNl2s08xYJpv6JExon-tUGEhkhxSRXBDvQ6LIDt5n4c7wkisYNoFTAX_nE8W75bUUn9iDubdT2b-fV-qw8UdA=='  # 🔐 Paste the encrypted output here
	return decrypt_password(encrypted_password)