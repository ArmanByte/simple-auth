import time
import re
class Account:
    def __init__(self, email, username, password, status, balance):
        self.email = email
        self.username = username
        self.password = password
        self.status = status
        self.balance = balance

# Load Data
def load_data():
    data = []
    try:
        with open('data.txt', 'r') as file:
            for line in file:
                email, username, password, status, balance = eval(line.strip())
                balance = int(balance)
                data.append(Account(email, username, password, status, balance))
    except FileNotFoundError:
        print("Something went wrong (Data File Error). Try again later.")
        exit()
    return data

# Start
def start():
    data = load_data()
    print("\nWelcome. PyAuth by Arman.")
    print("1: Log In.")
    print("2: Register.")
    print("3: Verification.")
    print("4: Exit.")

    auth_type = input("\nChoice: ")

    if auth_type == "1":
        print("\nLog into your account.")
        return 'login'

    elif auth_type == "2":
        print("\nRegistration.")
        registration()
        return None

    elif auth_type == "3":
        print("\nVerification.")
        print("Coming soon.\n")
        time.sleep(1)
        return None

    elif auth_type == "4":
        print("\nThank you for visiting PyAuth. Good luck.")
        exit()

    else:
        print("\nInvalid choice. Please try again.\n")
        time.sleep(1)
        return None

# Registration function
def registration():
    data = load_data()
    reg_email = input("Email: ")

    # Check for uniqueness and type
    while True:
        if (reg_email.lower().endswith("@gmail.com") or reg_email.lower().endswith("@mail.ru")) and reg_email.lower() != "@gmail.com":
            if any(account.email.lower() == reg_email.lower() for account in data):
                print(f"\nAn account with the email {reg_email} already exists.")
                reg_email = input("Email: ")
            else:
                break
        else:
            print("\nWrong email type. Try again.")
            reg_email = input("Email: ")

    # Input registration username
    reg_username = input("Username [5-15]: ")
    while True:
        if len(reg_username) > 15 or len(reg_username) < 5:
            print("\nWrong username, it should be 5-15 characters. Try again.")
            reg_username = input("Username [5-15]: ")
        elif not re.match("^[a-zA-Z0-9]*$", reg_username):
            print("\nOnly letters and numbers are allowed. Please try another.")
            reg_username = input("Username [5-15]: ")
        elif any(account.username.lower() == reg_username.lower() for account in data):
            print(f"\nUsername {reg_username} is taken. Try another one.")
            reg_username = input("Create username: ")
        else:
            break

    # Create password
    reg_pass = input("Create password [8-20]: ")
    while(len(reg_pass) < 8 or len(reg_pass) > 20):
        print("\nPassword should be 8-20 characters. Try again.")
        reg_pass =  input("Create password [8-20]: ")
    # Enter password again
    reg_pass_match = input("Confirm password: ")
    attempts = 0

    while True:
        attempts += 1
        if reg_pass == reg_pass_match:
            print("\nAccount successfully created. You can log in now.\n")
            with open('data.txt', 'a') as file:
                reg_email_lower = reg_email.lower()
                file.write(f"\n('{reg_email_lower}','{reg_username}','{reg_pass}', 'n', 0)")
            time.sleep(1)
            login()
            break
        else:
            if attempts == 3:
                print("\nNo more attempts. Registration failed.")
                exit()
            elif attempts < 3:
                reg_pass_match = input(f"Confirmation failed. Attempts left: {3-attempts}. Confirm password: ")

# Log in function
def login():
    data = load_data()
    input_email = input("Email: ")
    email_lower = input_email.lower()
    attempts = 0
    user = next((account for account in data if account.email == email_lower), None)
    
    while attempts < 4:
        user = next((account for account in data if account.email == email_lower), None)
        if not user:
            if attempts == 3:
                print("\nNo more attempts. Can't log in.")
                exit()
            print(f"\nUnable to find account with this email: {email_lower}, try again. Attempts left: {3-attempts}.")
            input_email = input("Email: ")
            email_lower = input_email.lower()
        else:
            break
        attempts += 1

    input_password = input("Password: ")
    attempts = 0

    while True:
        attempts += 1
        if input_password == user.password:
            print(f"\nWelcome back {user.username}.")
            if user.status == 'n':
                print("Status: Not verified. Verify your email to get access.\n")
                exit()
            elif user.status == 'b':
                print("Status: Banned.")
                exit()
            elif user.status == 'v':
                print("Status: Verified.")
            elif user.status == 'p':
                print("Status: Premium.")
            elif user.status == 'e':
                print("Status: Elite.")
            elif user.status == "a":
                print("Status: Admin.")
            else:
                print("Status: Forbidden. No access.")
            return user
        else:
            if attempts < 3:
                print(f"Wrong password, try again. Attempts left: {3-attempts}.")
                input_password = input("Password: ")
            elif attempts == 3:
                print("\nWrong password. No more attempts, can't log in.")
                exit()

# Balance synchronization
def synchronization(user):
    with open("data.txt", "r") as file:
        lines = file.readlines()
    with open("data.txt", "w") as file:
        for line in lines:
            sync = line.replace(str(user.balance), str(user.balance))
            file.write(sync)
