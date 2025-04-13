from models.institution import Institution
from models.object_of_interest import ObjectOfInterest

class Administrator:
    def __init__(self, name):
        self.name = name

    def make_objects_available(self, institution, obj):
        institution.add_object_of_interest(obj)
