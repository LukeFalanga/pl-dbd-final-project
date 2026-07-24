import mariadb

# Class for managing the database connection and simple operations
class DatabaseManager:
    def __init__(self):
        self.connection = mariadb.connect(
            host="localhost",
            user="root",
            password="Hudson56",
            database="ecommerce"
        )

    def get_cursor(self):
        return self.connection.cursor()

    def commit(self):
        self.connection.commit()

    def close(self):
        self.connection.close()