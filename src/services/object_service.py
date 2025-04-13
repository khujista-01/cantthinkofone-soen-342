
from supabase import create_client
from utils.config import SUPABASE_URL, SUPABASE_API_KEY


supabase_client = create_client(SUPABASE_URL, SUPABASE_API_KEY)

def view_all_objects():

    response = supabase_client.table("objects_of_interest").select("*").execute()


    if response.status_code == 200:
        return response.data
    else:
        return {"error": "Failed to fetch objects"}
