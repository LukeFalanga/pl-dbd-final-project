import sys
from database.mariadb_connection import DatabaseManager
from services.product_service import ProductService

def main():

    db = DatabaseManager()
    product_service = ProductService(db)
    product_service.show_all_products()
    product_service.search_product("Laptop")
    db.close()

    return 0

if __name__ == "__main__":
    sys.exit(main())