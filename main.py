import json
import hashlib

def hash_password(password):
    # Use a secure hash function (SHA-256 in this case)
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

def create_account():
    print("Create Account:")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email address: ")
    username = input("Enter your username: ")

    # Use input instead of getpass for password input
    password = input("Enter your password: ")

    # Hash the password before storing it
    hashed_password = hash_password(password)

    account = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "username": username,
        "password": hashed_password,
    }

    save_account(account)
    print("Account created and saved successfully.")

def save_account(account):
    with open("accounts.json", "a") as file:
        json.dump(account, file)
        file.write('\n')  # Add a newline to separate entries

def read_accounts():
    try:
        with open("accounts.json", "r") as file:
            accounts = [json.loads(line) for line in file]
        return accounts
    except FileNotFoundError:
        return []

def login():
    while True:
        print("Login:")
        username = input("Enter your username (or type 'exit' to quit): ")

        if username.lower() == 'exit':
            break

        password = input("Enter your password: ")

        hashed_password = hash_password(password)

        accounts = read_accounts()

        for account in accounts:
            if account["username"] == username and account["password"] == hashed_password:
                print("Login successful!")
                return

        print("Login failed. Incorrect username or password.")

def main():
    while True:
        # Choose whether to create an account, login, or exit
        choice = input("Do you want to (1) create an account, (2) login, or (3) exit? Enter 1, 2, or 3: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
