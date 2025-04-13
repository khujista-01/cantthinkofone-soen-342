class ObjectOfInterest:
    objects = []

    def __init__(self, obj_id, name, description, owned):
        self.obj_id = obj_id
        self.name = name
        self.description = description
        self.owned = owned

    @classmethod
    def add_object(cls, obj):
        cls.objects.append(obj)

    @classmethod
    def get_all_objects(cls):
        return cls.objects
