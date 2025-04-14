class auction_house:
    def __init__(self, auid, name, location):
        self.auid = auid
        self.name = name
        self.location = location

    def add_auction_house(self):
        print(f"Auction House '{self.name}' added successfully.")

    def __str__(self):
        return f"Auction House ID: {self.auid}, Name: {self.name}, Location: {self.location}"
