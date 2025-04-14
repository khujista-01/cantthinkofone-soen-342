from http.client import responses

from models.administrator import Administrator
from utils.supabase_client import get_supabase_client
from datetime import datetime


class ClerkService:

    # @staticmethod
    # def authenticate(username, password):
    #     supabase = get_supabase_client()
    #
    #
    #     response = supabase.table('administrator').select('*').eq('username', username).single().execute()
    #     response_data = response.data
    #
    #     if response_data and response_data['password'] == password:
    #         return True
    #     else:
    #         print("Invalid credentials. Please try again.")
    #         return False

    @staticmethod
    def authenticate(username, password):
        # Get the Singleton instance of Administrator
        admin = Administrator()

        # Call the authenticate method on the Administrator instance
        if admin.authenticate(username, password):
            return True
        else:
            return False

    @staticmethod
    def approve_sign_up():
        supabase = get_supabase_client()
        response = supabase.table('clients').select('*').eq('status', 'pending').execute()

        if response.data:
            print("Pending Clients:")
            for client in response.data:
                print(f"{client['id']}: {client['name']}")

            while True:
                try:
                    client_id = int(input("Enter Client ID to approve: "))
                    supabase.table('clients').update({'status': 'approved'}).eq('id', client_id).execute()
                    print("Client approved!")
                    break  # Exit the loop once the client is approved
                except ValueError:
                    print("Invalid input! Please enter a valid Client ID.")
        else:
            print("No pending clients.")

    @staticmethod
    def update_expert_info():
        supabase = get_supabase_client()

        # Retrieve the list of experts from the 'experts' table
        experts = supabase.table('experts').select('id', 'name').execute()

        if not experts.data:
            print("No experts found in the database.")
            return

        # Show a list of all experts with their IDs and names
        print("List of Experts:")
        for expert in experts.data:
            print(f"ID: {expert['id']}, Name: {expert['name']}")

        while True:
            try:
                # Ask the user to select an expert ID
                expert_id = int(input("\nEnter Expert ID to update: "))
                selected_expert = next((expert for expert in experts.data if expert['id'] == expert_id), None)

                if not selected_expert:
                    print("Invalid Expert ID. Please try again.")
                else:
                    break  # Exit the loop once a valid ID is entered
            except ValueError:
                print("Invalid input! Please enter a valid Expert ID.")

        # Ask which field to update
        while True:
            print("\nSelect the information to update:")
            print("1. Name")
            print("2. Expertise")
            print("3. Available Schedule")

            field_choice = input("Enter choice (1, 2, or 3): ")

            if field_choice == '1':  # Update Name
                new_name = input("Enter new name: ")
                # Update the name of the expert in the 'experts' table
                supabase.table('experts').update({'name': new_name}).eq('id', expert_id).execute()
                print("Expert name updated!")
                break

            elif field_choice == '2':  # Update Expertise
                new_expertise = input("Enter new expertise: ")
                # Update the expertise of the expert in the 'experts' table
                supabase.table('experts').update({'expertise': new_expertise}).eq('id', expert_id).execute()
                print("Expert expertise updated!")
                break

            elif field_choice == '3':  # Update Available Schedule
                new_schedule = input("Enter new available schedule: ")
                # Update the available schedule of the expert in the 'experts' table
                supabase.table('experts').update({'availability_schedule': new_schedule}).eq('id', expert_id).execute()
                print("Expert availability schedule updated!")
                break

            else:
                print("Invalid choice, please try again.")

    @staticmethod
    def add_expert_availability():
        supabase = get_supabase_client()

        # Retrieve all experts from the 'experts' table (including their ID and Name)
        experts = supabase.table('experts').select('id', 'name').execute()

        if not experts.data:
            print("No experts found in the database.")
            return

        # Display the list of experts with their IDs and names
        print("List of Experts:")
        for expert in experts.data:
            print(f"ID: {expert['id']}, Name: {expert['name']}")

        while True:
            try:
                # Ask the user to select an expert by their ID
                expert_id = int(input("\nEnter Expert ID to update availability: "))
                selected_expert = next((expert for expert in experts.data if expert['id'] == expert_id), None)

                if not selected_expert:
                    print("Invalid Expert ID. Please try again.")
                else:
                    break  # Exit the loop once a valid ID is entered
            except ValueError:
                print("Invalid input! Please enter a valid Expert ID.")

        # Ask for the availability time slots
        time_slots = input(f"Enter availability time slots for {selected_expert['name']} (comma-separated): ")

        # Insert the new availability into the 'availabilities' table
        supabase.table('availabilities').insert({'expert_id': expert_id, 'time_slots': time_slots}).execute()

        print(f"Expert availability for {selected_expert['name']} added successfully!")

    @staticmethod
    def add_auction_data():
        supabase = get_supabase_client()

        while True:
            # Display options: Add Auction House or Add Auction
            print("Select an option:")
            print("1. Add Auction House")
            print("2. Add Auction")

            choice = input("Enter choice (1 or 2): ")

            if choice == '1':
                # Add a new auction house
                print("\nAdding a new Auction House...")
                auction_house_name = input("Enter new Auction House name: ")
                auction_house_location = input("Enter Auction House location: ")

                # Insert the new auction house into the 'auction_houses' table
                new_auction_house = supabase.table('auction_houses').insert({
                    'name': auction_house_name,
                    'location': auction_house_location  # Ensure column name matches the database
                }).execute()

                print(f"New Auction House '{auction_house_name}' added successfully!")
                break  # Exit the loop after adding auction house

            elif choice == '2':
                # Proceed with adding an auction
                print("\nAdding a new Auction...")

                # Retrieve the list of auction houses
                auction_houses = supabase.table('auction_houses').select('id', 'name',
                                                                         'location').execute()  # Adjust the field name if needed

                if not auction_houses.data:
                    print("No auction houses found. Please add an auction house first.")
                    continue  # Go back to the menu to add an auction house

                # Display the list of auction houses with their IDs and names
                print("List of Auction Houses:")
                for house in auction_houses.data:
                    # Ensure the correct field name is used
                    print(f"ID: {house['id']}, Name: {house['name']}, Location: {house['location']}")

                while True:
                    try:
                        # Ask the user to select an auction house
                        auction_house_id = int(input("\nEnter Auction House ID to associate with the auction: "))
                        selected_house = next(
                            (house for house in auction_houses.data if house['id'] == auction_house_id), None)

                        if not selected_house:
                            print("Invalid Auction House ID. Please try again.")
                        else:
                            break  # Exit the loop once a valid Auction House ID is entered
                    except ValueError:
                        print("Invalid input! Please enter a valid Auction House ID.")

                # Ask for the auction's name, schedule, and type
                auction_name = input("Enter auction name: ")

                while True:
                    auction_date = input("Enter auction date (YYYY-MM-DD): ")
                    try:
                        # Validate if the date is in correct format
                        datetime.strptime(auction_date, '%Y-%m-%d')
                        break
                    except ValueError:
                        print("Invalid date format. Please use YYYY-MM-DD.")

                while True:
                    auction_time = input("Enter auction time (HH:MM, 24-hour format): ")
                    try:
                        # Validate if the time is in correct format
                        datetime.strptime(auction_time, '%H:%M')
                        break
                    except ValueError:
                        print("Invalid time format. Please use HH:MM (24-hour format).")

                auction_type = input("Enter auction type (online/in-person): ").lower()
                while auction_type not in ["online", "in-person"]:
                    print("Invalid auction type. Please enter 'online' or 'in-person'.")
                    auction_type = input("Enter auction type (online/in-person): ").lower()

                # Check if there's an existing auction with the same date and time in the same auction house
                existing_auction = supabase.table('auctions').select('id').eq('auction_house_id', auction_house_id).eq(
                    'schedule', f'{auction_date} {auction_time}').execute()

                if existing_auction.data:
                    print(
                        f"An auction already exists on {auction_date} at {auction_time} in this auction house. Please choose a different time.")
                    return

                # Insert the new auction into the 'auctions' table
                supabase.table('auctions').insert({
                    'name': auction_name,
                    'schedule': f'{auction_date} {auction_time}',
                    'auction_type': auction_type,
                    'auction_house_id': auction_house_id
                }).execute()

                print(f"Auction '{auction_name}' has been added successfully!")
                break  # Exit the loop after adding the auction

            else:
                print("Invalid choice. Please select a valid option (1 or 2).")

    @staticmethod
    def delete_user_account():
        supabase = get_supabase_client()
        user_id = input("Enter User ID to delete: ")

        supabase.table('users').delete().eq('id', user_id).execute()
        print("User account deleted!")

    @staticmethod
    def add_object():
        supabase = get_supabase_client()

        # Ask the admin for object details
        object_name = input("Enter the name of the object: ")
        object_description = input("Enter the description of the object: ")

        while True:
            owned = input("Is the object owned? (yes/no): ").lower()
            if owned == "yes":
                owned = True
                break
            elif owned == "no":
                owned = False
                break
            else:
                print("Invalid input! Please enter 'yes' or 'no'.")

        # Insert the object into the 'objects' table
        response = supabase.table('objects').insert({
            'name': object_name,
            'description': object_description,
            'owned': owned
        }).execute()

        # Check for successful insertion
        if response.data:
            print(f"Object '{object_name}' has been added successfully!")
        elif response.error:
            print(f"There was an error adding the object: {response.error['message']}")
        else:
            print("Unknown error occurred. Please try again.")

    @staticmethod
    def approve_and_assign_expert():
        supabase = get_supabase_client()

        # Fetch all pending service requests
        response = supabase.table('service_requests').select('*').eq('status', 'pending').execute()

        if not response.data:
            print("No pending service requests found.")
            return

        print("\n--- Pending Service Requests ---")
        for idx, request in enumerate(response.data, start=1):
            print(
                f"{idx}. Request ID: {request['id']} | Client ID: {request['client_id']} | Service Type: {request['type']}")

        try:
            request_choice = int(input("Enter the number of the service request to approve: "))
            selected_request = response.data[request_choice - 1]
        except (ValueError, IndexError):
            print("Invalid choice. Please try again.")
            return

        # Fetch available experts
        expert_response = supabase.table('experts').select('id', 'name').execute()
        if not expert_response.data:
            print("No experts found in the database.")
            return

        print("\n--- Available Experts ---")
        for idx, expert in enumerate(expert_response.data, start=1):
            print(f"{idx}. Expert ID: {expert['id']}, Name: {expert['name']}")

        try:
            expert_choice = int(input("Enter the number of the expert to assign: "))
            selected_expert = expert_response.data[expert_choice - 1]
        except (ValueError, IndexError):
            print("Invalid choice. Please try again.")
            return

        # Fetch NOT BOOKED availability of the selected expert
        availability_response = supabase.table('availabilities').select('*') \
            .eq('expert_id', selected_expert['id']).eq('status', 'Not Booked').execute()

        if not availability_response.data:
            print(f"No available (unbooked) time slots for Expert {selected_expert['name']}.")
            return

        print(f"\n--- Available Time Slots for Expert {selected_expert['name']} ---")
        for idx, availability in enumerate(availability_response.data, start=1):
            print(f"{idx}. Time Slot: {availability['time_slots']}")

        try:
            availability_choice = int(input("Enter the number of the time slot to assign: "))
            selected_availability = availability_response.data[availability_choice - 1]
        except (ValueError, IndexError):
            print("Invalid choice. Please try again.")
            return

        # Mark the selected availability as Booked
        supabase.table('availabilities').update({
            'status': 'Booked'
        }).eq('id', selected_availability['id']).execute()

        # Assign the expert to the service request and mark it as approved
        update_response = supabase.table('service_requests').update({
            'status': 'approved',
            'assigned_expert_id': selected_expert['id']
        }).eq('id', selected_request['id']).execute()

        if update_response.data:
            print(
                f"✅ Service request {selected_request['id']} has been approved and Expert {selected_expert['name']} is assigned for the time slot: {selected_availability['time_slots']}.")
        else:
            print("❌ Failed to approve the service request.")

    @staticmethod
    def make_expert_account():
        supabase = get_supabase_client()

        # Ask for expert details from the admin
        name = input("Enter the expert's name: ")
        expertise = input("Enter the expert's expertise: ")
        available_schedule = input("Enter the expert's available schedule (e.g., 10:30 - 11:30): ")
        email = input("Enter the expert's email address: ")
        password = input("Enter the expert's password: ")

        # Remove 'id' from the data and let the database auto-generate the ID
        expert_data = {
            'name': name,
            'expertise': expertise,
            'available_schedule': available_schedule,
            'email': email,
            'password': password
        }

        # Insert the new expert into the 'experts' table
        response = supabase.table('experts').insert(expert_data).execute()

        if response.data:
            print(f"Expert account for {name} has been successfully created.")
        elif response.error:
            print(f"Error: {response.error['message']}. Please try again.")
        else:
            print("Unknown error occurred while creating the expert account.")

    @staticmethod
    def delete_expert_account():
        supabase = get_supabase_client()

        # Ask for the expert ID to delete
        expert_id = input("Enter the Expert ID to delete: ")

        # Check if the expert exists
        expert_check = supabase.table('experts').select('id').eq('id', expert_id).execute()
        if not expert_check.data:
            print("Expert not found. Please check the ID and try again.")
            return

        # Delete the expert account from the 'experts' table
        delete_response = supabase.table('experts').delete().eq('id', expert_id).execute()

        if delete_response.data:
            print(f"Expert account with ID {expert_id} has been successfully deleted.")
        elif delete_response.error:
            print(f"Error: {delete_response.error['message']}. Please try again.")
        else:
            print("Unknown error occurred while deleting the expert account.")