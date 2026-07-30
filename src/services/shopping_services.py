from models.purchaseitem import PurchaseItem

# Class definition for shopping services
class ShoppingServices:
    def __init__(self, db):
        self.__db = db

    # Adds an item to the cart
    def add_to_cart(self, product_id, quantity, cart):
            cursor = self.__db.get_cursor()

            cursor.execute("SELECT ProductID From Product WHERE ProductID = ?", (product_id,))
            prod = cursor.fetchone()
            if prod is None:
                print("Product does not exist. Item not added to cart")
                return 0

            cursor.execute("SELECT Stock FROM Product WHERE ProductID = ?", (product_id,))
            itemStock = cursor.fetchone()[0]
    
            # Makes sure users can not buy more than what is available
            if quantity > itemStock:
                print("Attempting to buy at a higher quantity than available! Item not added to cart.")
                return 0
    
            cursor.execute("SELECT Price FROM Product WHERE ProductID = ?", (product_id,))
            price = cursor.fetchone()[0]
            itemTotal = price * quantity
    
            item = PurchaseItem(None, product_id, quantity)
            cart.append(item)

            cursor.close()
            print("Item succesfully added to cart.")

            return itemTotal

    # Removes an item from the cart (including its quantity)
    def remove_from_cart(self, product_id, cart):
         for item in cart:
              if item.product_id == product_id:

                   cursor = self.__db.get_cursor()
                   cursor.execute("SELECT Price FROM Product WHERE ProductID = ?", (product_id,))

                   price = cursor.fetchone()[0]
                   cursor.close()

                   total_removed = price * item.get_purchase_quantity()

                   cart.remove(item)
                   return total_removed
                   

    def view_cart(self, cart):
         for item in cart:
              print(f"Product ID: {item.get_purchase_product_id()}, Quantity: {item.get_purchase_quantity()}")
         