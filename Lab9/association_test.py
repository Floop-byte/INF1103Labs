from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct

supplier = Supplier(1111, "Amazon", "amazon@aws.com")

physical = PhysicalProduct(
    "P1", "Keyboard", 50.0, 5, 1.0, supplier
)
digital = DigitalProduct(
    "D1", "E-book", 10.0, 20, 25.0, supplier
)

del supplier

physical.display_information()
digital.display_information()