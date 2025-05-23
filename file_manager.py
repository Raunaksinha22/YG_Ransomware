# file_manager.py

import os
from config import TARGET_EXTENSIONS

def find_target_files(start_path):
    target_files = []
    for root, _, files in os.walk(start_path):
        for file in files:
            if any(file.endswith(ext) for ext in TARGET_EXTENSIONS):
                full_path = os.path.join(root, file)
                target_files.append(full_path)
    return target_files
