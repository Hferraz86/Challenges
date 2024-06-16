#!/bin/python3

from cryptography.fernet import Fernet
import os

# Function to generate an encryption key
def generate_key():
    return Fernet.generate_key()

# Function to encrypt a file
def encrypt_file(filename, key):
    with open(filename, 'rb') as f:
        data = f.read()
    
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)
    
    # Write encrypted data back to the file
    with open(filename + '.encrypted', 'wb') as f:
        f.write(encrypted_data)

    # Optionally delete the original file
    os.remove(filename)

# Function to decrypt a file
def decrypt_file(filename, key):
    with open(filename, 'rb') as f:
        encrypted_data = f.read()
    
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)
    
    # Write decrypted data back to the file
    with open(filename[:-10], 'wb') as f:  # remove the '.encrypted' extension
        f.write(decrypted_data)

    # Optionally delete the encrypted file
    os.remove(filename)

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

# Main function for user interface
def main():
    print("Select mode:")
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    print("3. Encrypt a message")
    print("4. Decrypt a message")
    mode = input("Enter the mode number you want to use: ")

    if mode == '1':
        filepath = input("Enter the path to the file to encrypt: ")
        key = generate_key()
        encrypt_file(filepath, key)
        print("File encrypted successfully.")
    elif mode == '2':
        filepath = input("Enter the path to the file to decrypt: ")
        key = generate_key()  # Assuming we're using the same key for decryption as encryption
        decrypt_file(filepath, key)
        print("File decrypted successfully.")
    elif mode == '3':
        message = input("Enter the message to encrypt: ")
        key = generate_key()
        encrypt_message(message, key)
    elif mode == '4':
        encrypted_message = input("Enter the encrypted message: ")
        key = generate_key()  # Assuming we're using the same key for decryption as encryption
        decrypt_message(encrypted_message, key)
    else:
        print("Invalid mode selected. Please select a mode between 1 to 4.")

if __name__ == "__main__":
    main()
