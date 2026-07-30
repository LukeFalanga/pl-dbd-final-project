# Class definition for purchases
class Purchases:
    def __init__(self, CustomerID, purchaseDate, total, purchaseID=None):
        self.__purchaseID = purchaseID
        self.__CustomerID = CustomerID
        self.__purchaseDate = purchaseDate
        self.__total = total

    def get_purchase_id(self):
        return self.__purchaseID

    def get_customer_id(self):
        return self.__CustomerID

    def get_purchase_date(self):
        return self.__purchaseDate

    def get_purchase_total(self):
        return self.__total