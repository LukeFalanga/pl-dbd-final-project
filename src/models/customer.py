# Class definition for the Customer
class Customer:
    def __init__(self, first_name, last_name,email, customer_id=None):
        self.__customer_id = customer_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email

    def get_customer_id(self):
        return self.__customer_id

    def get_customer_first_name(self):
        return self.__first_name

    def get_customer_last_name(self):
        return self.__last_name

    def get_customer_email(self):
        return self.__email

    def set_customer_email(self, newEmail):
        self.__email = newEmail
    
