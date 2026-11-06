from product import Product
from can_be_shipped import CanBeShipped

SHIPPING_BASE_FEE = 5.00
SHIPPING_RATE_PER_KG = 2.50


class PhysicalProduct(Product, CanBeShipped):
    """A product that is stored in a warehouse and shipped."""

    def __init__(self, product_id, name, price, stock, weight, supplier):
        super().__init__(product_id, name, price, stock, supplier)
        if weight < 0:
            raise ValueError("Weight cannot be negative.")
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def display_information(self):
        super().display_information()
        print(f"  Weight: {self.__weight} kg")

    def get_fulfilment_info(self):
       return "Requires physical shipping."

    def calculate_shipping_cost(self):
        """Base fee plus a per-kilogram rate."""
        return SHIPPING_BASE_FEE + SHIPPING_RATE_PER_KG * self.__weight

    def to_dict(self):
        data = super().to_dict()
        data.update({"type": "physical", "weight": self.__weight})
        return data
