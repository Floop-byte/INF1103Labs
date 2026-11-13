"""Section 2.3 'Predict first' check.

Predictions (write yours here BEFORE running):
  1. Order total 250 with BulkDiscount(200, 20)      -> 230.0
  2. Same order, then set_discount(PercentageDiscount(10)) -> 225.0
"""
from supplier import Supplier
from physical_product import PhysicalProduct
from order import Order
from discount_strategy import BulkDiscount, PercentageDiscount

supplier = Supplier(1111, "Amazon", "amazon@aws.com")
keyboard = PhysicalProduct("P1", "Keyboard", 100.0, 10, 1.0, supplier)
mouse = PhysicalProduct("P2", "Mouse", 50.0, 10, 0.2, supplier)

# Lines: 2 x 100 + 1 x 50 = 250
order = Order("O1", BulkDiscount(200, 20))
order.add_order_line(keyboard, 2)
order.add_order_line(mouse, 1)

predicted_bulk = 230.0
predicted_percentage = 225.0

actual_bulk = order.calculate_total()
print(f"BulkDiscount(200, 20):       predicted {predicted_bulk}, actual {actual_bulk}")

order.set_discount(PercentageDiscount(10))
actual_percentage = order.calculate_total()
print(f"PercentageDiscount(10):      predicted {predicted_percentage}, actual {actual_percentage}")

assert actual_bulk == predicted_bulk
assert actual_percentage == predicted_percentage
print("Both predictions matched.")
