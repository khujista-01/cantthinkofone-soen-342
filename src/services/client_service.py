from models.auction import Auction

class ClientService:
    @staticmethod
    def view_auctions():
        return Auction.get_all_auctions()
