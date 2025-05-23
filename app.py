#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox
from encryptor import encrypt_folder, generate_key, load_key, KEY_FILE
from decryptor import decrypt_folder
import os

TARGET_FOLDER = "test_folder"  # Folder with files to encrypt/decrypt

def run_simulation():
    if not os.path.exists(TARGET_FOLDER):
        messagebox.showerror("Error", f"Target folder '{TARGET_FOLDER}' does not exist.")
        return
    key = generate_key()
    encrypt_folder(TARGET_FOLDER, key)
    status_label.config(text="🔐 Files encrypted! Keep your key safe.")
    print("Encryption complete.")

def run_decryption():
    if not os.path.exists(KEY_FILE):
        messagebox.showerror("Error", f"Key file '{KEY_FILE}' not found.")
        return
    try:
        key = load_key()
        decrypt_folder(TARGET_FOLDER, key)
        status_label.config(text="✅ Files decrypted successfully.")
        print("Decryption complete.")
    except Exception as e:
        messagebox.showerror("Error", "Decryption failed.\n" + str(e))

app = tk.Tk()
app.title("Ransomware Simulator (Educational Use Only)")
app.geometry("420x300")

tk.Label(app, text="🛡️ Ransomware Simulator", font=("Helvetica", 14)).pack(pady=10)

tk.Button(app, text="🔐 Start Simulation (Encrypt Files)", width=30, command=run_simulation).pack(pady=10)
tk.Button(app, text="🔓 Decrypt Files", width=30, command=run_decryption).pack(pady=10)

status_label = tk.Label(app, text="", font=("Helvetica", 10), fg="blue")
status_label.pack(pady=20)

tk.Label(app, text=f"Target folder: ./{TARGET_FOLDER}", font=("Helvetica", 8), fg="gray").pack(pady=5)
tk.Label(app, text=f"Key file: {KEY_FILE}", font=("Helvetica", 8), fg="gray").pack()

app.mainloop()
