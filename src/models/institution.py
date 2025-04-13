from models.object_of_interest import ObjectOfInterest

class Institution:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def add_object_of_interest(self, obj):
        ObjectOfInterest.add_object(obj)
