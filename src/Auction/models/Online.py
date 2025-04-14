class Online():
    def __init__(self, name, schedule, auction_house_id, start_time, end_time):
        # Initialize the parent class
        super().__init__(name, schedule, 'Online', auction_house_id)
        self.start_time = start_time
        self.end_time = end_time

    def create_auction(self):
        print(f"Online Auction '{self.name}' created successfully from {self.start_time} to {self.end_time}.")

    def __str__(self):
        return f"Online Auction - {self.name}, Type: {self.auction_type}, Schedule: {self.schedule}, Start: {self.start_time}, End: {self.end_time}"
