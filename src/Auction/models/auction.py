class auction:
    def __init__(self, aid, name, schedule, auction_type, auction_house_id):
        self.aid = aid
        self.name = name
        self.schedule = schedule
        self.auction_type = auction_type
        self.auction_house_id = auction_house_id

    def create_auction(self):
        print(f"Auction '{self.name}' created successfully.")

    def view(self):
        print(f"Viewing auction '{self.name}' scheduled for {self.schedule}.")

    def __str__(self):
        return f"Auction ID: {self.aid}, Name: {self.name}, Type: {self.auction_type}, Scheduled: {self.schedule}"
