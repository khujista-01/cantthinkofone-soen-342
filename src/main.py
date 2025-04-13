
from services.client_service import ClientService
from services.institution_service import InstitutionService

def main_menu():
    while True:
        print("\n🎨 Art Advisory System 🎨")
        print("1. View Objects of Interest")
        print("2. Add Object of Interest (Admin Only)")
        print("3. View Auctions")
        print("4. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            view_objects()
        elif choice == "2":
            add_object()
        elif choice == "3":
            view_auctions()
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def view_objects():
    objects = InstitutionService.get_objects()
    if not objects:
        print("\nNo objects available.")
    else:
        print("\nObjects of Interest:")
        for obj in objects:
            print(f"- {obj['name']} ({obj['description']}) - Owned: {obj['owned']}")

def add_object():
    name = input("Enter object name: ")
    description = input("Enter object description: ")
    owned = input("Is this object owned by the institution? (yes/no): ").strip().lower() == "yes"
    InstitutionService.add_object(name, description, owned)

def view_auctions():
    auctions = ClientService.view_auctions()
    if not auctions:
        print("\nNo auctions scheduled.")
    else:
        print("\nUpcoming Auctions:")
        for auction in auctions:
            print(f"- {auction['name']} on {auction['schedule']}")

if __name__ == "__main__":
    main_menu()
