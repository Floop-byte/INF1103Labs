import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from inventory import Inventory
from inventory_system import get_positive_float
from product_factory import ProductFactory
from supplier import Supplier


class TestInventoryAndInput(unittest.TestCase):
    def setUp(self) -> None:
        supplier = Supplier(1111, "Amazon", "amazon@aws.com")
        self.product = ProductFactory.create(
            "digital", "D001", "Course", 30.0, 5, 120.0, supplier
        )

    def test_inventory_add_search_remove(self) -> None:
        inventory = Inventory()
        self.assertTrue(inventory.add_product(self.product))
        self.assertFalse(inventory.add_product(self.product))
        self.assertIs(inventory.search_product("d001"), self.product)
        self.assertTrue(inventory.remove_product("D001"))
        self.assertIsNone(inventory.search_product("D001"))

    def test_update_stock_rejects_negative(self) -> None:
        self.product.update_stock(0)
        self.assertEqual(self.product.get_stock(), 0)
        with self.assertRaises(ValueError):
            self.product.update_stock(-1)

    def test_get_positive_float_reprompts_until_valid(self) -> None:
        with patch("builtins.input", side_effect=["abc", "-5", "0", "12.50"]):
            result = get_positive_float("Price: ")
        self.assertEqual(result, 12.50)


if __name__ == "__main__":
    unittest.main()
