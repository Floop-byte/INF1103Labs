from product import Product
from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory


def show_product_details(product: Product) -> None:
    product.display_information()
    print(f"Fulfilment: {product.get_fulfilment_info()}")
    print()

supplier = Supplier(1111, "Amazon", "amazon@aws.com")
physical = PhysicalProduct("P1", "Keyboard", 50.0, 5, 1.0, supplier)
digital = DigitalProduct("D1", "E-book", 10.0, 20, 25.0, supplier)

inventory = Inventory()
inventory.add_product(physical)
inventory.add_product(digital)

for product in inventory.get_products():
    show_product_details(product)
