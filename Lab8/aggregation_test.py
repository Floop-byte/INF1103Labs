from supplier import Supplier
from physical_product import PhysicalProduct
from inventory import Inventory

supplier = Supplier(1111, "Amazon", "amazon@aws.com")


product = PhysicalProduct("P1", "Keyboard", 50.0, 5, 1.0, supplier)
original_id = id(product)

inventory_a = Inventory()
inventory_b = Inventory()

inventory_a.add_product(product)
print("Product added to Inventory A:")
inventory_a.display_all()

inventory_a.remove_product("P1")
print("Inventory A after removal:")
inventory_a.display_all()

print("Product still works outside either inventory:")
product.update_stock(10)
product.display_information()
product.get_stock() == 10
id(product) == original_id

inventory_b.add_product(product)
print("Same product added to Inventory B:")
inventory_b.display_all()

print("Aggregation test passed: removing a product does not destroy it.")
