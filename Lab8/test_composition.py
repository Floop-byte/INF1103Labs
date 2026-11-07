from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from order import Order


def display_order(order: Order) -> None:
    print(f"Order {order.order_id}")
    for line in order.order_lines:
        print(f"  {line.product.get_name()} | Quantity: {line.quantity} | "
              f"Subtotal: ${line.calculate_subtotal():.2f}")
    print(f"Total: ${order.calculate_total():.2f}")
    print()

supplier = Supplier(1111, "Amazon", "amazon@aws.com")
physical = PhysicalProduct("P1", "Keyboard", 50.0, 5, 1.0, supplier)
digital = DigitalProduct("D1", "E-book", 10.0, 20, 25.0, supplier)

order_a = Order("A")
order_b = Order("B")

order_a.add_order_line(physical, 2)
order_b.add_order_line(physical, 1)

print("Same OrderLine object (expected False):",
      order_a.order_lines[0] is order_b.order_lines[0])
print("Same Product object (expected True):",
      order_a.order_lines[0].product is order_b.order_lines[0].product)
print("At this point: 2 order lines reference 1 shared physical product.")
print("The separate digital product exists but has not been ordered yet.")
print()     

order_a.add_order_line(digital, 3)
print("Expected totals: Order A = $130.00, Order B = $50.00")
display_order(order_a)
display_order(order_b)

order_a.remove_order_line("P1")
print("After removing the keyboard line from Order A:")
print("Expected totals: Order A = $30.00, Order B = $50.00")
display_order(order_a)
display_order(order_b)

print("The keyboard product still exists independently:")
physical.display_information()
