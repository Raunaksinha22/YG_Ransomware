from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

def encrypt_file(file_path, key):
    """Encrypts a file with AES-256-CBC and saves as file_path + '.enc'."""
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    with open(file_path, 'rb') as f:
        plaintext = f.read()
    
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    
    with open(file_path + '.enc', 'wb') as f:
        f.write(iv + ciphertext)  # prepend IV for decryption
    
    # Optionally delete original file after encryption
    # os.remove(file_path)
