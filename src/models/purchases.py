# Class definition for purchases
class Purchases:
    def __init__(self, CustomerID, purchaseDate, total, purchaseID=None):
        self.purchaseID = purchaseID
        self.CustomerID = CustomerID
        self.purchaseDate = purchaseDate
        self.total = total