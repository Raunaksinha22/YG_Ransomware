from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os
from kivy.utils import platform

# Get platform-safe file path
if platform == 'android':
    from android.storage import app_storage_path
    BASE_PATH = app_storage_path()
else:
    BASE_PATH = os.getcwd()

KEY_FILE = os.path.join(BASE_PATH, "key.bin")

def generate_key():
    key = get_random_bytes(32)  # AES-256 key
    with open(KEY_FILE, "wb") as f:
        f.write(key)
    return key

def load_key():
    with open(KEY_FILE, "rb") as f:
        return f.read()

def pad(data):
    padding_len = AES.block_size - len(data) % AES.block_size
    return data + bytes([padding_len]) * padding_len

def encrypt_file(path, key):
    try:
        with open(path, "rb") as f:
            data = f.read()
        cipher = AES.new(key, AES.MODE_CBC)
        ciphertext = cipher.encrypt(pad(data))
        with open(path + ".enc", "wb") as f:
            f.write(cipher.iv + ciphertext)
        os.remove(path)
        print(f"Encrypted: {path}")
    except Exception as e:
        print(f"Failed to encrypt {path}: {e}")

def encrypt_folder(folder, key):
    for root, _, files in os.walk(folder):
        for name in files:
            if not name.endswith(".enc") and name != "key.bin":
                path = os.path.join(root, name)
                encrypt_file(path, key)
