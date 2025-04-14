class InPerson():
    def __init__(self, name, schedule, auction_house_id, catalog):
        # Initialize the parent class
        super().__init__(name, schedule, 'In-Person', auction_house_id)
        self.catalog = catalog  # Catalog of items for the auction

    def create_auction(self):
        """
        Override create_auction method for in-person-specific logic.
        """
        print(f"In-Person Auction '{self.name}' created successfully at {self.schedule}. Catalog: {self.catalog}")

    def __str__(self):
        return f"In-Person Auction - {self.name}, Type: {self.auction_type}, Schedule: {self.schedule}, Catalog: {self.catalog}"