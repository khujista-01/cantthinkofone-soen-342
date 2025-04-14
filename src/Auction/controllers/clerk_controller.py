
from services.clerk_service import ClerkService

def login_as_clerk():
    username = input("Enter Clerk Username: ")
    password = input("Enter Clerk Password: ")

    if ClerkService.authenticate(username, password):
        print("\nLogin successful!\n")
        show_clerk_options()
    else:
        print("Invalid credentials. Please try again.")
        login_as_clerk()

def show_clerk_options():
    while True:
        print("Select an action:")
        print("1. Approve Client Sign-Up")
        print("2. Update Expert Info")
        print("3. Update Expert Availability")
        print("4. Add Auction Data")
        print("5. Delete Expert Account")
        print("6. Add object")
        print("7. Approve service request")
        print("8. Make a Expert Account")
        print("9. Logout")

        choice = input("Enter choice: ")

        if choice == '1':
            ClerkService.approve_sign_up()
        elif choice == '2':
            ClerkService.update_expert_info()
        elif choice == '3':
            ClerkService.add_expert_availability()
        elif choice == '4':
            ClerkService.add_auction_data()
        elif choice == '5':
            ClerkService.delete_expert_account()
        elif choice == '6':
            ClerkService.add_object()
        elif choice == '7':
            ClerkService.approve_and_assign_expert()
        elif choice == '8':
            ClerkService.make_expert_account()
        elif choice == '9':
            print("Logging out...")
            break  # Exit the loop and log out
        else:
            print("Invalid choice, please try again.")