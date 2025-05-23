from Crypto.Cipher import AES
import os

def unpad(data):
    return data[:-data[-1]]

def decrypt_file(file_path, key):
    with open(file_path, "rb") as f:
        iv = f.read(16)
        ciphertext = f.read()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext))
    original_path = file_path.replace(".enc", "")
    with open(original_path, "wb") as f:
        f.write(plaintext)
    os.remove(file_path)

def decrypt_directory(directory, key):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".enc"):
                full_path = os.path.join(root, file)
                decrypt_file(full_path, key)
