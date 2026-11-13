import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from discount_strategy import (
    BulkDiscount,
    NoDiscount,
    PercentageDiscount,
    StudentDiscount,
)
from order import Order
from product_factory import ProductFactory
from supplier import Supplier


class TestDiscountStrategy(unittest.TestCase):
    def setUp(self) -> None:
        supplier = Supplier(1111, "Amazon", "amazon@aws.com")
        self.item = ProductFactory.create(
            "physical", "P001", "Mouse", 50.0, 10, 0.2, supplier
        )

    def test_strategies_apply(self) -> None:
        self.assertEqual(NoDiscount().apply(100.0), 100.0)
        self.assertAlmostEqual(PercentageDiscount(10).apply(100.0), 90.0)
        self.assertEqual(BulkDiscount(100.0, 15.0).apply(100.0), 85.0)
        self.assertEqual(BulkDiscount(100.0, 15.0).apply(99.0), 99.0)
        self.assertAlmostEqual(StudentDiscount().apply(100.0), 95.0)

    def test_order_uses_and_switches_discount_strategy(self) -> None:
        order = Order("O001")
        order.add_order_line(self.item, 2)  # subtotal = 100.0
        self.assertAlmostEqual(order.calculate_total(), 100.0)

        order.set_discount(PercentageDiscount(20))
        self.assertAlmostEqual(order.calculate_total(), 80.0)


if __name__ == "__main__":
    unittest.main()
