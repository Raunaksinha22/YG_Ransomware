from Crypto.Cipher import AES
import os
from kivy.utils import platform

# Get platform-safe file path
if platform == 'android':
    from android.storage import app_storage_path
    BASE_PATH = app_storage_path()
else:
    BASE_PATH = os.getcwd()

KEY_FILE = os.path.join(BASE_PATH, "key.bin")

def unpad(data):
    padding_len = data[-1]
    return data[:-padding_len]

def decrypt_file(path, key):
    try:
        with open(path, "rb") as f:
            iv = f.read(16)
            ciphertext = f.read()
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted = unpad(cipher.decrypt(ciphertext))
        with open(path[:-4], "wb") as f:  # remove ".enc"
            f.write(decrypted)
        os.remove(path)
        print(f"Decrypted: {path}")
    except Exception as e:
        print(f"Failed to decrypt {path}: {e}")

def decrypt_folder(folder, key):
    for root, _, files in os.walk(folder):
        for name in files:
            if name.endswith(".enc"):
                path = os.path.join(root, name)
                decrypt_file(path, key)
