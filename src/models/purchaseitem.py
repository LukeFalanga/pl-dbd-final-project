# Class definition for the PurchaseItem model

class PurchaseItem:
    def __init__(self, purchase_id, product_id, quantity):
        self.__purchase_id = purchase_id
        self.__product_id = product_id
        self.__quantity = quantity

    def get_purchase_id(self):
        return self.__purchase_id

    def get_purchase_product_id(self):
        return self.__product_id(self)

    def get_purchase_quantity(self):
        return self.__quantity