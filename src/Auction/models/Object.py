class Object:
    def __init__(self, obid, name, description, owned):
        self.obid = obid
        self.name = name
        self.description = description
        self.owned = owned

    def add_object(self):
        print(f"Object '{self.name}' added successfully.")

    def __str__(self):
        return f"Object ID: {self.obid}, Name: {self.name}, Description: {self.description}, Owned: {self.owned}"
