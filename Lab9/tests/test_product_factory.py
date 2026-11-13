import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from digital_product import DigitalProduct
from physical_product import PhysicalProduct
from product_factory import ProductFactory
from supplier import Supplier


class TestProductFactory(unittest.TestCase):
    def setUp(self) -> None:
        self.supplier = Supplier(1111, "Amazon", "amazon@aws.com")

    def test_create_physical_product(self) -> None:
        product = ProductFactory.create(
            "physical", "P001", "Laptop", 1200.0, 5, 2.1, self.supplier
        )
        self.assertIsInstance(product, PhysicalProduct)
        self.assertEqual(product.get_weight(), 2.1)

    def test_create_digital_product(self) -> None:
        product = ProductFactory.create(
            "digital", "D001", "Ebook", 19.99, 10, 15.0, self.supplier
        )
        self.assertIsInstance(product, DigitalProduct)
        self.assertEqual(product.get_download_size(), 15.0)

    def test_create_unknown_type_raises(self) -> None:
        with self.assertRaises(ValueError):
            ProductFactory.create(
                "bundle", "B001", "Bundle", 50.0, 1, 0.0, self.supplier
            )


if __name__ == "__main__":
    unittest.main()
