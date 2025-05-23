import tkinter as tk
from tkinter import messagebox
from encryptor import encrypt_directory, generate_key, load_key
from decryptor import decrypt_directory
import os

TARGET_FOLDER = "test_folder"  # Change to your dummy folder path

def run_simulation():
    key = generate_key()
    encrypt_directory(TARGET_FOLDER, key)
    status_label.config(text="🔐 Files encrypted! Ransom note added.")

def run_decryption():
    try:
        key = load_key()
        decrypt_directory(TARGET_FOLDER, key)
        status_label.config(text="✅ Files decrypted successfully.")
    except Exception as e:
        messagebox.showerror("Error", "Decryption failed.\n" + str(e))

app = tk.Tk()
app.title("Ransomware Simulator")
app.geometry("420x300")

tk.Label(app, text="🛡️ Ransomware Simulator (Educational Use Only)", font=("Helvetica", 14)).pack(pady=10)

tk.Button(app, text="🔐 Start Simulation", width=30, command=run_simulation).pack(pady=10)
tk.Button(app, text="🔓 Decrypt Files", width=30, command=run_decryption).pack(pady=10)

status_label = tk.Label(app, text="", font=("Helvetica", 10), fg="blue")
status_label.pack(pady=20)

tk.Label(app, text="Target: ./test_folder", font=("Helvetica", 8), fg="gray").pack()

app.mainloop()