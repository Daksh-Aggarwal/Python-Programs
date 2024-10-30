from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key) 

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            username, password, note = data.split(" | ")
            print(f"Username: {username} | Password: {fer.decrypt(password.encode()).decode()} | Note: {note}")

def add():
    username = input("Username: ")
    password = input("Password: ")
    note = input("Note: ")

    with open('passwords.txt', 'a') as f:
        f.write(f"{username} | {fer.encrypt(password.encode()).decode()} | {note}\n")

while True:
    function = input("Would you like to view your passwords or add a new password (view/add)? Type 'Q' to quit. ").lower()
    
    if function == 'q':
        break

    if function == 'view':
        view()
    elif function == 'add':
        add()
    else:
        print("Invalid input! Please try again.")
        continue