class Institution:
    def __init__(self, name, location, owns_objects):
        self.name = name
        self.location = location
        self.owns_objects = owns_objects

    def add_institution(self):
        print(f"Institution '{self.name}' located at {self.location} added successfully.")

    def __str__(self):
        return f"Institution Name: {self.name}, Location: {self.location}, Owns Objects: {self.owns_objects}"
