from utils.supabase_client import get_supabase_client

class ClientService:

    @staticmethod
    def client_sign_up():
        supabase = get_supabase_client()

        institutions = supabase.table('institutions').select('id', 'name', 'location').execute()

        if not institutions.data:
            print("No institutions found in the database.")
            return

        print("List of Institutions:")
        for institution in institutions.data:
            print(f"ID: {institution['id']}, Name: {institution['name']}, Location: {institution['location']}")

        institution_id = input("Enter the ID of the institution you are associated with: ")

        selected_institution = next((inst for inst in institutions.data if str(inst['id']) == institution_id), None)
        if not selected_institution:
            print("Invalid institution ID. Please try again.")
            return

        client_name = input("Enter your full name: ")
        email = input("Enter your email address: ")
        password = input("Enter your password: ")


        client_data = {
            'name': client_name,
            'email': email,
            'password': password,
            'institution_id': institution_id,
            'status': 'pending'
        }

        response = supabase.table('clients').insert(client_data).execute()

        if response.data:
            print(
                f"Client '{client_name}' has been successfully registered with status 'pending'. Please wait for admin approval.")
        elif response.error:
            print(f"Error: {response.error['message']}. Please try again.")
        else:
            print("Unknown error occurred during client registration.")

    @staticmethod
    def authenticate(email, password):
        supabase = get_supabase_client()

        response = supabase.table('clients').select('*').eq('email', email).execute()

        if not response.data:
            print("No account found with that email address. Please try again.")
            return False


        client_data = response.data[0]
        if client_data['password'] == password:
            if client_data['status'] == 'pending':
                print("Your account is pending approval by an admin.")
                return False
            return client_data['id']  # Successful login
        else:
            print("Invalid credentials. Please try again.")
            return False  # Incorrect password

    @staticmethod
    def view_objects():
        supabase = get_supabase_client()

        objects = supabase.table('objects').select('name', 'description', 'owned').execute()

        if objects.data:
            print("\n--- Objects Available ---")
            for obj in objects.data:
                owned_status = "Owned" if obj['owned'] else "Not Owned"
                print(f"Name: {obj['name']}, Description: {obj['description']}, Status: {owned_status} by institution")
        else:
            print("No objects available.")

    @staticmethod
    def request_service(client_id):
        supabase = get_supabase_client()

        service_types = ['Consultation', 'Accompany to Auction', 'Attend Auction']

        print("\n--- Available Service Types ---")
        for idx, service in enumerate(service_types, start=1):
            print(f"{idx}. {service}")

        service_choice = input(f"Enter the number for the service you would like to request (1-{len(service_types)}): ")

        try:
            service_type = service_types[int(service_choice) - 1]
        except (ValueError, IndexError):
            print("Invalid choice. Please try again.")
            return

        service_data = {
            'client_id': client_id, # client id authenticate function mathi aave che
            'type': service_type,
            'status': 'pending',
            'assigned_expert_id': None
        }

        response = supabase.table('service_requests').insert(service_data).execute()

        if response.data:
            print(f"Your service request for '{service_type}' has been submitted and is pending approval.")
        elif response.error:
            print(f"Error: {response.error['message']}. Please try again.")
        else:
            print("Unknown error occurred during service request submission.")