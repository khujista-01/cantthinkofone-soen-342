
from supabase import create_client
from utils.config import SUPABASE_URL, SUPABASE_API_KEY


supabase_client = create_client(SUPABASE_URL, SUPABASE_API_KEY)



def get_objects_from_db():
    response = supabase_client.table("objects_of_interest").select("*").execute()


    print("Response Data:", response.data)
    print("Response Status:", response.status_code)
    print("Response Error:", response.error_message)

    if response.data:
        return response.data
    else:
        return []



def add_object_to_db(name, description, owned):
    response = supabase_client.table("objects_of_interest").insert({
        "name": name,
        "description": description,
        "owned": owned
    }).execute()


    print("Add Object Response Status:", response.status_code)
    print("Add Object Response Error:", response.error_message)

    if response.status_code == 201:
        return True
    else:
        return False
