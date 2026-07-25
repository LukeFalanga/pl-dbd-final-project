# Classd definition for products
class Product:
    def __init__(self, name, price, stock, product_id=None):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock