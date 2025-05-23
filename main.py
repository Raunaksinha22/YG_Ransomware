from encryptor import generate_key, encrypt_folder
from lockscreen import show_lock_screen
import os

target_folder = "test_files"
os.makedirs(target_folder, exist_ok=True)

key = generate_key()
encrypt_folder(target_folder, key)

# Now launch lock screen and wait for input
show_lock_screen(key, target_folder)
