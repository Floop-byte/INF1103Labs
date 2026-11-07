from product import Product
from order_line import OrderLine


class Order:
    """Creates and manages its own order lines."""

    def __init__(self, order_id: str):
        self.order_id: str = order_id
        self.order_lines: list[OrderLine] = []

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity)
        self.order_lines.append(order_line)

    def remove_order_line(self, product_id: str) -> bool:
        """Remove the first matching line without removing its product."""
        for order_line in self.order_lines:
            if order_line.product.get_product_id().upper() == product_id.upper():
                self.order_lines.remove(order_line)
                return True
        return False

    def calculate_total(self) -> float:
        total = 0.0
        for order_line in self.order_lines:
            total += order_line.calculate_subtotal()
        return total
