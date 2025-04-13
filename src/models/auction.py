class Auction:
    auctions = []

    def __init__(self, name, schedule):
        self.name = name
        self.schedule = schedule

    @classmethod
    def schedule_auction(cls, name, schedule):
        auction = cls(name, schedule)
        cls.auctions.append(auction)

    @classmethod
    def get_all_auctions(cls):
        return cls.auctions
