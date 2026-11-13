from abc import ABC, abstractmethod


class CanBeShipped(ABC):
    """Interface-style contract for anything that can be shipped."""

    @abstractmethod
    def calculate_shipping_cost(self) -> float:
        """Return the cost of shipping this object."""
