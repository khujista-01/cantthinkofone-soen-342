
from services.object_service import view_all_objects

def display_objects():
    objects = view_all_objects()
    if "error" not in objects:
        for obj in objects:
            print(f"Object Name: {obj['name']}, Description: {obj['description']}")
    else:
        print(objects["error"])
