from models.object_of_interest import ObjectOfInterest


class Client:
    def __init__(self, name):
        self.name = name

    def view_objects(self):
        return ObjectOfInterest.get_all_objects()


    def view_objects(self):
        return ObjectOfInterest.get_all_objects()
