# from supabase import create_client
#
# # Your actual project details here
# url = "https://itgwoviyzqdeuuczcztb.supabase.co"
# key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Iml0Z3dvdml5enFkZXV1Y3pjenRiIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDMyODkwOTQsImV4cCI6MjA1ODg2NTA5NH0.NNGfVlzLIJGPMDxzOf3CShtd2BzGEscwD0pSD0elb_A"
#
# supabase = create_client(url, key)
#
# # response = supabase.table("administrator").select("*").limit(1).execute()
#
# response = supabase.table("administrator").insert({"name": "Test Item"}).execute()
# print("Insert result:", response.data)
