from services.client_service import ClientService
from services.expert_service import ExpertService


def login_as_expert():
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if ExpertService.authenticate(username, password):
        print("\nLogin successful!\n")
        show_expert_options()
    else:
        print("Invalid credentials. Please try again.")
        login_as_expert()

def show_expert_options():
    while True:
        print("\n Select an action:")
        print("1. Add Availibility")
        print("2. View Objects")
        print("3. Update Expert Availability")
        print("4. View Auction Data")
        print("5. Logout")

        choice = input("Enter choice: ")

        if choice == '1':
            ExpertService.add_availability()
        elif choice == '2':
            ClientService.view_objects()
        elif choice == '3':
            ExpertService.update_availability()
        elif choice == '4':
            ExpertService.view_auctions()
        elif choice == '5':
            print("Logging out...")
            break  # Exit the loop and log out
        else:
            print("Invalid choice, please try again.")