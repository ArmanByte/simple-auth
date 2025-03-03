# Menu example
def menu(user):
    if user.status in ("v", "p", "e"):
        print("\nMenu.")
        print("1: Balance.")
        print("2: Exit.\n")
    elif user.status in ("a"):
        print("\nMenu.")
        print("1: Balance.")
        print("2: Exit.\n")
        print("Admin Tools.")
        # Admin tools here using permission