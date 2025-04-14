from utils.supabase_client import get_supabase_client

class Administrator:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, username=None, password=None):
        if not hasattr(self, '_initialized'):
            self._initialized = True
            self.username = username
            self.password = password
            self.logged_in = False

    def authenticate(self, username, password):
        supabase = get_supabase_client()

        try:

            response = supabase.table('administrator').select('*').eq('username', username).single().execute()


            response_data = response.data
            if response_data and response_data['password'] == password:

                self.username = username
                self.password = password
                self.logged_in = True
                print(f"Administrator {self.username} logged in successfully!")
                return True
            else:
                print("Invalid credentials. Please try again.")
                return False
        except Exception as e:

            print(f"Error during authentication: {e}. Could not find the username or there was an issue with the query.")
            return False

    def logout(self):
        self.logged_in = False
        print(f"Administrator {self.username} logged out.")

    def is_logged_in(self):
        return self.logged_in
