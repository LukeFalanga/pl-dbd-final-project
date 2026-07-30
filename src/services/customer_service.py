from models.customer import Customer
# Class definition for customer services
class CustomerService:
    def __init__(self, db):
        self.__db = db

    # Adds a customer to the database
    def add_customer(self, customer):
        cursor = self.__db.get_cursor()

        # The code through the two while loops ensures UNIQUE emails, preventing a database error
        cursor.execute("SELECT COUNT(*) FROM Customer WHERE Email = ?", (customer.email,))
        email_exists = cursor.fetchone()[0]

        while email_exists > 0:
            newEmail = str(input("Email taken, choose another: "))

            while len(newEmail) < 1:
                newEmail = str(input("Please enter your Email: "))

            customer.email = newEmail
            cursor.execute("SELECT COUNT(*) FROM Customer WHERE Email = ?", (customer.email,))
            email_exists = cursor.fetchone()[0]

        cursor.execute("INSERT INTO Customer (FirstName, LastName, Email) VALUES (?, ?, ?)", (customer.first_name, customer.last_name, customer.email))

        self.__db.commit()
        cursor.close()

    # Retrieves a customer from the database as a Customer object, via email
    def get_customer_by_id(self, customer_id):
        cursor = self.__db.get_cursor()

        cursor.execute("SELECT * FROM Customer WHERE CustID = ?", (customer_id,))

        custTuple = cursor.fetchone()

        if custTuple is None:
            print(f"Customer with ID: {customer_id} not found.")
            return None

        customer = Customer(customer_id=custTuple[0],first_name=custTuple[1],last_name=custTuple[2],email=custTuple[3])

        cursor.close()
        return customer

    # Retrieves a customer from the database as a Customer object, via email
    def get_customer_by_email(self, email):
        cursor = self.__db.get_cursor()

        cursor.execute("SELECT * FROM Customer WHERE Email = ?", (email,))

        custTuple = cursor.fetchone()

        if custTuple is None:
            print(f"Customer with Email: {email} not found.")
            return None

        customer = Customer(customer_id=custTuple[0],first_name=custTuple[1],last_name=custTuple[2],email=custTuple[3])

        cursor.close()
        return customer
