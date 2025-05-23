import os

def generate_key():
    return os.urandom(32)  # AES-256
