from utils.supabase_client import get_supabase_client
from datetime import datetime

class ExpertService:
    @staticmethod
    def authenticate(email, password):
        supabase = get_supabase_client()

        # Query the experts table for the email
        response = supabase.table('experts').select('*').eq('email', email).execute()

        if len(response.data) == 0:
            print("Expert not found. Please check the email or sign up.")
            return False
        elif len(response.data) > 1:
            print("Multiple experts found with the same email. Please contact the administrator.")
            return False
        else:

            expert_data = response.data[0]
            if expert_data['password'] == password:
                return True  # Authentication successful
            else:
                print("Invalid password. Please try again.")
                return False  # Incorrect password

    @staticmethod
    def add_availability():
        supabase = get_supabase_client()

        expert_id = input("Enter your Expert ID: ")


        expert_check = supabase.table('experts').select('id').eq('id', expert_id).execute()
        if not expert_check.data:
            print("Expert not found. Please check the ID and try again.")
            return

        time_slot = input("Enter the time slot for availability (e.g., 10:00 - 11:00): ")

        availability_data = {
            'expert_id': expert_id,
            'time_slots': time_slot,
            'status': 'Not Booked'  # Default status is 'Not Booked'
        }

        response = supabase.table('availabilities').insert(availability_data).execute()

        if response.data:
            print(f"Availability for Expert ID {expert_id} has been successfully added.")
        elif response.error:
            print(f"Error: {response.error['message']}. Please try again.")
        else:
            print("Unknown error occurred while adding availability.")

    @staticmethod
    def update_availability():
        supabase = get_supabase_client()

        expert_id = input("Enter your Expert ID: ")

        expert_check = supabase.table('experts').select('id').eq('id', expert_id).execute()
        if not expert_check.data:
            print("Expert not found. Please check the ID and try again.")
            return

        time_slot = input("Enter the current time slot you want to update (e.g., 10:00 - 11:00): ")

        availability_response = supabase.table('availabilities').select('*').eq('expert_id', expert_id).eq('time_slots', time_slot).execute()

        if not availability_response.data:
            print(f"No availability found for the time slot {time_slot}.")
            return

        current_status = availability_response.data[0]['status']
        if current_status == 'Booked':
            print(f"Cannot update the availability for time slot {time_slot} as it is already booked.")
            return

        new_time_slot = input(f"Enter the new time slot (current: {time_slot}): ")

        update_response = supabase.table('availabilities').update({
            'time_slots': new_time_slot
        }).eq('expert_id', expert_id).eq('time_slots', time_slot).execute()

        if update_response.data:
            print(f"Availability for Expert ID {expert_id} has been successfully updated to {new_time_slot}.")
        elif update_response.error:
            print(f"Error: {update_response.error['message']}. Please try again.")
        else:
            print("Unknown error occurred while updating availability.")

    @staticmethod
    def view_auctions():
        supabase = get_supabase_client()

        # Fetch the auction details along with the related auction house details
        response = supabase.table('auctions').select('id', 'name', 'schedule', 'auction_type',
                                                     'auction_house_id').execute()

        if not response.data:
            print("No auctions found.")
            return

        print("\n--- Auction Details ---")
        for auction in response.data:
            # Fetch the auction house details using the auction_house_id
            auction_house_response = supabase.table('auction_houses').select('name', 'location').eq('id', auction[
                'auction_house_id']).execute()

            if not auction_house_response.data:
                print(f"Auction House for Auction ID {auction['id']} not found.")
                continue

            auction_house = auction_house_response.data[0]

            # Display auction details
            print(f"Auction Name: {auction['name']}")
            print(f"Schedule: {auction['schedule']}")
            print(f"Auction Type: {auction['auction_type']}")
            print(f"Auction House: {auction_house['name']} - Location: {auction_house['location']}")
            print("-" * 40)