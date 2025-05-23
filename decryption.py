from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def decrypt_file(file_path, key):
    """Decrypts a file encrypted by encrypt_file()."""
    with open(file_path, 'rb') as f:
        iv = f.read(16)
        ciphertext = f.read()
    
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    
    orig_file_path = file_path[:-4]  # remove '.enc'
    with open(orig_file_path, 'wb') as f:
        f.write(plaintext)
    
    # Optionally delete encrypted file after decryption
    # os.remove(file_path)
