# Class definition for the Customer
class Customer:
    def __init__(self, first_name, last_name,email, customer_id=None):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

