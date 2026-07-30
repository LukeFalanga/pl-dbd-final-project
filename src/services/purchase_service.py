from datetime import datetime
# Class definition for purchase services
class PurchaseService:
    def __init__(self, db):
        self.__db = db

    # Checks out customer's cart and adds all items to the purchaseItem table and purchases table
    def make_purchase(self, customer_id, cart, total):
        cursor = self.__db.get_cursor()
        purchase_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute("INSERT INTO Purchases(CustID, PurchaseDate, Total) VALUES (?, ?, ?)", (customer_id, purchase_date, total))

        purchase_id = cursor.lastrowid

        for item in cart:
            cursor.execute("INSERT INTO PurchaseItem(PurchaseID, ProductID, Quantity) VALUES (?, ?, ?)", (purchase_id, item.get_purchase_product_id(), item.get_purchase_quantity()))
            cursor.execute("UPDATE Product SET Stock = Stock - ? WHERE ProductID = ?", (item.get_purchase_quantity(), item.get_purchase_product_id()))

        self.__db.commit()
        cursor.close()

        return purchase_id

    # Shows total purchase history
    def show_purchase_history(self, customer_id):
        cursor = self.__db.get_cursor()

        cursor.execute("SELECT * FROM Purchases WHERE CustID = ?", (customer_id,))
        history = cursor.fetchall()

        for p in history:
            print(f"PurchaseID: {p[0]}, CustID: {p[1]}, Date: {p[2]}, Total: {p[3]}")

        cursor.close()

    # Shows all items bought and their quantities in a singular purchase
    def show_purchase_items(self, purchase_id):
        cursor = self.__db.get_cursor()

        cursor.execute("SELECT Product.ProductName, PurchaseItem.Quantity, Product.Price FROM PurchaseItem JOIN Product ON PurchaseItem.ProductID = Product.ProductID WHERE PurchaseItem.PurchaseID = ?", (purchase_id,))

        items = cursor.fetchall()
        for i in items:
            print(f"Name: {i[0]}, Quantity: {i[1]}, Price (for 1): {i[2]}")

        cursor.close()

        
