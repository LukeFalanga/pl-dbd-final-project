from models.purchaseitem import PurchaseItem

# Class definition for shopping services
class ShoppingServices:
    def __init__(self, db):
        self.db = db

    # Adds an item to the cart
    def add_to_cart(self, product_id, quantity, currTotal, cart):
            cursor = self.db.get_cursor()
    
            cursor.execute("SELECT Stock FROM Product WHERE ProductID = ?", (product_id,))
            itemStock = cursor.fetchone()[0]
    
            # Makes sure users can not buy more than what is available
            if quantity > itemStock:
                print("Attempting to buy at a higher quantity than available! Item not added to cart.")
                return
    
            cursor.execute("SELECT Price FROM Product WHERE ProductID = ?", (product_id,))
            price = cursor.fetchone()[0]
            currTotal += price * quantity
    
            item = PurchaseItem(None, product_id, quantity)
            cart.append(item)
    
            cursor.close()
    
            return currTotal

    # Removes an item from the cart (including its quantity)
    def remove_from_cart(self, product_id, cart):
         for item in cart:
              if item.product_id == product_id:
                   cart.remove(item)

    def view_cart(self, cart):
         for item in cart:
              print(f"Product ID: {item.product_id}, Quantity: {item.quantity}")
         