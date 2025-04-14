from controllers.clerk_controller import login_as_clerk
from controllers.client_controller import client_menu
from controllers.expert_controller import login_as_expert


def main():
    print("Welcome to Art Advisory System")
    print("1. Clerk")
    print("2. Expert")
    print("3. Client")
    print("4. Bye")

    choice = input("Select your role: ")

    if choice == '1':
        login_as_clerk()
    elif choice == '2':
        login_as_expert()
    elif choice == '3':
        client_menu()  # Redirect to the client menu
    elif choice == '4':
        exit()
    else:
        print("Invalid choice, try again.")
        main()

if __name__ == "__main__":
    main()
