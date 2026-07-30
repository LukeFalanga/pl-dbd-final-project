import sys

# DBMS Class Import
from database.mariadb_connection import DatabaseManager

# Entity class imports
from models.purchaseitem import PurchaseItem
from models.product import Product
from models.customer import Customer
from models.purchases import Purchases

# Service Class Imports
from services.product_service import ProductService
from services.customer_service import CustomerService
from services.shopping_services import ShoppingServices
from services.purchase_service import PurchaseService

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a number.")

def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a number.")


def show_home():
        while True:
            print("==== Luke's E-commerce System ====\n")
            print("1. Customer Login\n2. Customer Registration\n3. Inventory Management\n4. Exit")

            home_selection = str(input("Selection: "))
            if home_selection in ["1", "2", "3", "4"]:
                return home_selection

            print("Invalid Selection.")


def staff_menu(prs):
    while True:
        print("\n==== Inventory Management ====")
        print("1. Add Stock")
        print("2. Add New Product")
        print("3. Back")

        choice = input("Selection: ")

        if choice == "1":
            print("Showing all product below:\n")
            prs.show_all_products()

            prod_id = get_integer("Please enter the ID of the product you wish to restock: ")
            quantity = get_integer("Please enter the quantity you wish to add to the product's stock: ")

            if prs.add_stock(prod_id, quantity):
                print("Stock successfully added.")
            else:
                print("Stock failed to add!")

        elif choice == "2":
            print("Adding New Product!")

            name = str(input("Please enter product name: "))
            while len(name) < 1:
                name = str(input("Invalid. Please enter product name: "))

            price = get_float("Please enter product price: ")
            while price < 0:
                price = get_float("Invalid. Please enter product price: ")

            stock = get_integer("Please enter current stock of the product: ")
            while stock < 0:
                stock = get_integer("Invalid. Please enter current stock: ")

            newProd = Product(name, price, stock)
            prs.add_product(newProd)

        elif choice == "3":
            return

        else:
            print("Invalid Selection")


def customer_menu(prs, ss, pus, currCustomer):
    customer_cart = []
    currTotal = 0 
    while True:
        print("\n==== Customer Menu ====")
        print("1. Browse All Products")
        print("2. Browse Product by Name")
        print("3. Add Product to Cart")
        print("4. Remove Item from Cart")
        print("5. Clear Cart")
        print("6. View Cart")
        print("7. Checkout")
        print("8. View Purchase History")
        print("9. View Specific Items from a Purchase")
        print("10. Back")

        choice = input("Selection: ")

        if choice == "1":
            print("Showing all Available Products")
            prs.show_all_products()

        elif choice == "2":
            search_term = str(input("Please enter the name of the product you wish to browse for: "))
            print(f"Showing all products related to {search_term}")
            prs.search_product(search_term)

        elif choice == "3":
            prod_id = get_integer("Please enter the product ID of the item you wish to add to your cart: ")
            quantity = get_integer(f"Please enter the amount of product ID: {prod_id} you wish to buy: ")
            currTotal += ss.add_to_cart(prod_id, quantity, customer_cart) 

        elif choice == "4":
            item_to_remove = get_integer("Please enter the product ID of the item you wish to remove from your cart: ")
            removed_price = ss.remove_from_cart(item_to_remove, customer_cart)
            currTotal -= removed_price

        elif choice == "5":
            print("Clearing Cart.")
            customer_cart = []
            currTotal = 0

        elif choice == "6":
            print("Viewing all Items in Cart:")
            ss.view_cart(customer_cart)

        elif choice == "7":

            if len(customer_cart) == 0:
                print("Your cart is empty!")
                continue

            print("Checking out all items in the cart!")
            latest_purchase_id = pus.make_purchase(currCustomer.get_customer_id(), customer_cart, currTotal)
            print(f"Purchase Successful for ${currTotal}! Showing Receipt at: ")
            pus.show_purchase_items(latest_purchase_id)
            print("\n Clearing cart and total.")
            currTotal = 0
            customer_cart = []

        elif choice == "8":
            print("Viewing Purchase History:")
            pus.show_purchase_history(currCustomer.get_customer_id())

        elif choice == "9":
            purchase_id = get_integer("Please enter the ID of the purchase you wish to see the items you bought for: ")
            pus.show_purchase_items(purchase_id)

        elif choice == "10":
            return

        else:
            print("Invalid selection.")



def login_customer(cs):

    # Emails are Unique, so any customer can be retrieved with an email
    email = str(input("Please enter your email: "))
    currCustomer = cs.get_customer_by_email(email)

    if currCustomer is None:
        print("Customer not found.")
        return None

    return currCustomer

          
def register_customer(cs):

    print("Registering as a customer!")
    
    firstName = str(input("Please enter your first name: "))
    while len(firstName) < 1:
        firstName = str(input("Please enter your first name: "))

    lastName = str(input("Please enter your last name: "))
    while len(lastName) < 1:
        lastName = str(input("Please enter your last name: "))

    email = str(input("Please enter your Email: "))
    while len(email) < 1:
        email = str(input("Please enter your Email: "))

    new_customer = Customer(firstName, lastName, email)

    cs.add_customer(new_customer)

    print("Successfully Registered! Logging into portal!")

    # This will return the newly created customer in the database with their Customer ID, which was not known previously
    return cs.get_customer_by_email(new_customer.get_customer_email())

    

def main():

    # Initialize database object
    db = DatabaseManager()

    # Initialize service objects
    prs = ProductService(db)
    cs = CustomerService(db)
    ss = ShoppingServices(db)
    pus = PurchaseService(db)

    while True:
        selection = show_home()
    
        if selection == "1":
            currCustomer = login_customer(cs)
            if currCustomer:
                customer_menu(prs, ss, pus, currCustomer)

        elif selection == "2":
            currCustomer = register_customer(cs)
            customer_menu(prs, ss, pus, currCustomer)

        elif selection == "3":
            staff_menu(prs)

        elif selection == "4":
            print("Closing system! Goodbye!")
            break

    return 0

if __name__ == "__main__":
    sys.exit(main())