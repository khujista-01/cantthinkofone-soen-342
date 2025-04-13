from models.object_of_interest import ObjectOfInterest


class Expert:
    def __init__(self, name, expertise):
        self.name = name
        self.expertise = expertise

    def view_objects(self):
        return ObjectOfInterest.get_all_objects()
