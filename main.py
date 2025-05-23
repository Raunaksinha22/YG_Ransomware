import tkinter as tk
from tkinter import filedialog, messagebox
import os
from encryptor import encrypt_file, decrypt_file, generate_key

class RansomwareSimulatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("YG Ransomware Simulator")
        self.key = None
        self.target_folder = None

        self.label = tk.Label(root, text="Select a folder to simulate encryption:")
        self.label.pack(pady=10)

        self.select_button = tk.Button(root, text="Select Folder", command=self.select_folder)
        self.select_button.pack()

        self.encrypt_button = tk.Button(root, text="Encrypt Files", command=self.encrypt_files, state=tk.DISABLED)
        self.encrypt_button.pack(pady=5)

        self.decrypt_button = tk.Button(root, text="Decrypt Files", command=self.decrypt_files, state=tk.DISABLED)
        self.decrypt_button.pack(pady=5)

        self.key_label = tk.Label(root, text="")
        self.key_label.pack(pady=10)

    def select_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.target_folder = folder
            self.encrypt_button.config(state=tk.NORMAL)
            messagebox.showinfo("Folder Selected", f"Target: {folder}")

    def encrypt_files(self):
        self.key = generate_key()
        for file in os.listdir(self.target_folder):
            path = os.path.join(self.target_folder, file)
            if os.path.isfile(path):
                encrypt_file(path, self.key)
        self.key_label.config(text=f"Encryption Key (save this!):\n{self.key.hex()}")
        self.decrypt_button.config(state=tk.NORMAL)
        with open(os.path.join(self.target_folder, "ransom_note.txt"), "w") as f:
            f.write("Your files are encrypted. Pay $X to unlock. Provide the key.")
        messagebox.showinfo("Done", "Files encrypted! Simulated ransom note created.")

    def decrypt_files(self):
        key_hex = tk.simpledialog.askstring("Decrypt", "Enter decryption key (hex):")
        try:
            key = bytes.fromhex(key_hex)
            for file in os.listdir(self.target_folder):
                path = os.path.join(self.target_folder, file)
                if os.path.isfile(path) and file != "ransom_note.txt":
                    decrypt_file(path, key)
            os.remove(os.path.join(self.target_folder, "ransom_note.txt"))
            messagebox.showinfo("Success", "Files decrypted!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to decrypt: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = RansomwareSimulatorApp(root)
    root.mainloop()
