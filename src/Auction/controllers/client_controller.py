from traceback import print_tb

from services.client_service import ClientService

def client_login():
    """
    Handles the client login process, where the client can log in using their email and password.
    """
    print("\n--- Client Login ---")
    email = input("Enter your email address: ")
    password = input("Enter your password: ")

    # if ClientService.authenticate(email, password):
    #     print("Login successful!")
    #     client_menu_logged_in()  # Proceed to the client menu after login
    # else:
    #     print("Invalid credentials. Please try again.")
    #     client_menu()  # Allow the user to try logging in again

    client_id = ClientService.authenticate(email, password)  # Get the client_id after successful authentication
    if client_id:
        print("Login successful!")
        # print(f"Client ID: {client_id}")  #dubugging mate che aa print statement
        client_menu_logged_in(client_id)
    else:
        print("Invalid credentials. Please try again.")
        client_menu()

def client_menu():
    print("\n--- Client Menu ---")

    while True:
        print("1. Login")
        print("2. Sign Up")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            client_login()
        elif choice == '2':
            ClientService.client_sign_up()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

def client_menu_logged_in(client_id):

    print("\n--- Client Menu ---")

    while True:
        print("1. View Objects")
        print("2. Request Service")
        print("3. Logout")

        choice = input("Enter choice: ")

        if choice == '1':
            ClientService.view_objects()
        elif choice == '2':
            # ClientService.request_service()  # Request a service
            ClientService.request_service(client_id)
        elif choice == '3':
            print("Logging out...")
            break  # Exit the menu and log out
        else:
            print("Invalid choice, please try again.")
