
from database.db import get_objects_from_db, add_object_to_db


class InstitutionService:
    @staticmethod
    def get_objects():

        objects = get_objects_from_db()

        if objects:
            return objects
        else:
            return []

    @staticmethod
    def add_object(name, description, owned):
        
        success = add_object_to_db(name, description, owned)

        if success:
            print("✅ Object added successfully!")
        else:
            print("❌ Failed to add object.")
