from auth import start, login
from menu import menu

def main():
    start()
    user = login()
    menu(user)

if __name__ == "__main__":
    main()