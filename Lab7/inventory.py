LINE = "-" * 48


class Inventory:
    """Manages a collection of Product objects."""

    def __init__(self):
        self.__products = []

    def add_product(self, product):
        """Add a product. Returns False if its ID already exists."""
        if self.search_product(product.get_product_id()):
            return False
        self.__products.append(product)
        return True

    def search_product(self, product_id):
        """Return the Product with this ID (case-insensitive), or None."""
        for product in self.__products:
            if product.get_product_id().upper() == product_id.upper():
                return product
        return None

    def get_products(self):
        """Return a copy of the product list (e.g. for saving)."""
        return list(self.__products)

    def display_all(self):
        print("Current Inventory")
        print(LINE)
        if not self.__products:
            print("No products in inventory.")
        for product in self.__products:
            product.display_information()
        print(LINE)
