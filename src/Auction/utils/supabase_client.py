import os
from supabase import create_client, Client

# Environment variables should be keys, not full URLs or tokens
url: str = os.environ.get("SUPABASE_URL", "https://itgwoviyzqdeuuczcztb.supabase.co")
key: str = os.environ.get("SUPABASE_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Iml0Z3dvdml5enFkZXV1Y3pjenRiIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDMyODkwOTQsImV4cCI6MjA1ODg2NTA5NH0.NNGfVlzLIJGPMDxzOf3CShtd2BzGEscwD0pSD0elb_A")

supabase: Client = create_client(url, key)

def get_supabase_client() -> Client:
    return supabase
