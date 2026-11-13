from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, total: float) -> float:
        pass

    def calculate_total(self) -> float:
        total = sum(line.calculate_subtotal() for line in self.order_lines)
        return self.discount.apply(total)

class NoDiscount(DiscountStrategy):
    def apply(self, total: float) -> float:
        return total

class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage: float) -> None:
        if percentage < 0 or percentage > 100:
            raise ValueError("Percentage must be between 0 and 100.")
        self.percentage = percentage

    def apply(self, total: float) -> float:
        discount_amount = total * (self.percentage / 100)
        return total - discount_amount

class BulkDiscount(DiscountStrategy):
    def __init__(self, threshold: float, discount_amount: float) -> None:
        if threshold < 0 or discount_amount < 0:
            raise ValueError("Threshold and discount amount must be non-negative.")
        self.threshold = threshold
        self.discount_amount = discount_amount

    def apply(self, total: float) -> float:
        if total >= self.threshold:
            return total - self.discount_amount
        return total

class StudentDiscount(DiscountStrategy):
    def apply(self, total: float) -> float:
        discount_amount = total * 0.05  # 5% discount
        return total - discount_amount