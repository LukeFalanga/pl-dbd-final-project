from models.product import Product
# Class definition for Product services
class ProductService:
    def __init__(self, db):
        self.__db = db

    # Displays all available products and their quantities
    def show_all_products(self):
        cursor = self.__db.get_cursor()

        cursor.execute("SELECT * FROM Product")

        rows = cursor.fetchall()

        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Price: {row[2]}, Stock: {row[3]}")

        cursor.close()

    # Displays all products that match the search term
    def search_product(self, product_name):
        cursor = self.__db.get_cursor()

        cursor.execute("SELECT * FROM Product WHERE ProductName LIKE ?", (f"%{product_name}%",))

        rows = cursor.fetchall()

        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Price: {row[2]}, Stock: {row[3]}")

        cursor.close()

    # Allows for stock to be added to a product in the database
    def add_stock(self, product_id, quantity):
        cursor = self.__db.get_cursor()

        # Check if product exists
        cursor.execute("SELECT ProductID FROM Product WHERE ProductID = ?", (product_id,))
        product = cursor.fetchone()

        if product is None:
            print("Product does not exist.")
            cursor.close()
            return False

        cursor.execute("UPDATE Product SET Stock = Stock + ? WHERE ProductID = ?", (quantity, product_id))

        self.__db.commit()
        cursor.close()
        return True

    # Allows for a new product to be added to the database
    def add_product(self, product):
        cursor = self.__db.get_cursor()

        cursor.execute("INSERT INTO Product (ProductName, Price, Stock) VALUES (?, ?, ?)", (product.get_product_name(), product.get_product_price(), product.get_product_stock()))

        self.__db.commit()
        cursor.close()

    # Returns a product by it's ID, in the form of a Product object
    def get_product_by_id(self, product_id):
        cursor = self.__db.get_cursor()

        cursor.execute("SELECT * FROM Product WHERE ProductID = ?", (product_id,))

        prodTuple = cursor.fetchone()

        product = Product(product_id=prodTuple[0], name=product[1], price=prodTuple[2], stock=prodTuple[3])

        cursor.close()
        return product