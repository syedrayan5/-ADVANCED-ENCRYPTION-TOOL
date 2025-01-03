from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os
import tkinter as tk
from tkinter import filedialog, messagebox
import base64

# Generate a 256-bit (32-byte) key
KEY = os.urandom(32)
IV = os.urandom(16)  # Initialization Vector for AES


def encrypt_file(file_path, key, iv):
    with open(file_path, "rb") as file:
        data = file.read()
    
    # Pad data to 16-byte block size
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()
    
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
    
    encrypted_file_path = file_path + ".enc"
    with open(encrypted_file_path, "wb") as enc_file:
        enc_file.write(iv + encrypted_data)  # Store IV in the file
    
    messagebox.showinfo("Success", f"File encrypted successfully!\nSaved as {encrypted_file_path}")
    return encrypted_file_path


def decrypt_file(file_path, key):
    with open(file_path, "rb") as enc_file:
        data = enc_file.read()
    
    iv = data[:16]  # Extract IV
    encrypted_data = data[16:]
    
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_padded_data = decryptor.update(encrypted_data) + decryptor.finalize()
    
    unpadder = padding.PKCS7(128).unpadder()
    decrypted_data = unpadder.update(decrypted_padded_data) + unpadder.finalize()
    
    decrypted_file_path = file_path.replace(".enc", "_decrypted")
    with open(decrypted_file_path, "wb") as dec_file:
        dec_file.write(decrypted_data)
    
    messagebox.showinfo("Success", f"File decrypted successfully!\nSaved as {decrypted_file_path}")
    return decrypted_file_path


def select_file(action):
    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    if action == "encrypt":
        encrypt_file(file_path, KEY, IV)
    elif action == "decrypt":
        decrypt_file(file_path, KEY)


# GUI Application
def create_gui():
    root = tk.Tk()
    root.title("AES-256 File Encryptor")
    root.geometry("400x200")
    
    tk.Label(root, text="AES-256 File Encryption & Decryption", font=("Arial", 12)).pack(pady=10)
    
    tk.Button(root, text="Encrypt File", command=lambda: select_file("encrypt"), width=20).pack(pady=5)
    tk.Button(root, text="Decrypt File", command=lambda: select_file("decrypt"), width=20).pack(pady=5)
    
    root.mainloop()


if __name__ == "__main__":
    create_gui()
