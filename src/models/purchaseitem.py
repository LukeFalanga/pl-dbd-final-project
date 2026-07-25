# Class definition for the PurchaseItem model

class PurchaseItem:
    def __init__(self, purchase_id, product_id, quantity):
        self.purchase_id = purchase_id
        self.product_id = product_id
        self.quantity = quantity