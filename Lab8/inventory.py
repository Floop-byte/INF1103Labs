from product import Product


LINE = "-" * 48


class Inventory:
    """Manages a collection of Product objects."""

    def __init__(self):
        self.__products: list[Product] = []

    def add_product(self, product: Product) -> bool:
        """Add a product. Returns False if its ID already exists."""
        if self.search_product(product.get_product_id()):
            return False
        self.__products.append(product)
        return True

    def search_product(self, product_id: str) -> Product | None:
        """Return the Product with this ID (case-insensitive), or None."""
        for product in self.__products:
            if product.get_product_id().upper() == product_id.upper():
                return product
        return None

    def find_product(self, product_id: str) -> Product | None:
        """Return the matching product, or None if it is not present."""
        return self.search_product(product_id)

    def remove_product(self, product_id: str) -> bool:
        """Remove the inventory's reference without destroying the product."""
        product = self.find_product(product_id)
        if product is None:
            return False
        self.__products.remove(product)
        return True

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
