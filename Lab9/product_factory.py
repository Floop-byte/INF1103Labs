from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from supplier import Supplier
from product import Product


class ProductFactory:
    @staticmethod
    def create(product_type: str, product_id: str, name: str, price: float,
               stock_quantity: int, extra: float, supplier: Supplier) -> Product:
        if product_type == "physical":
            return PhysicalProduct(product_id, name, price, stock_quantity, extra, supplier)
        elif product_type == "digital":
            return DigitalProduct(product_id, name, price, stock_quantity, extra, supplier)
        else:
            raise ValueError(f"Unknown product type: {product_type}")
