import json
import os
import tempfile
import inventory_system as ims
from inventory import Inventory
from product import Product
from can_be_shipped import CanBeShipped
from physical_product import PhysicalProduct
from digital_product import DigitalProduct

phys = PhysicalProduct("T1", "Guitar", 500.0, 3, 4.0)
dig = DigitalProduct("T2", "OS", 99.0, 10, 4096)
phys.display_information()
dig.display_information()

assert phys.get_weight() == 4.0 and dig.get_download_size() == 4096
assert "shipping" in phys.get_fulfilment_info()
assert "digitally" in dig.get_fulfilment_info()

try:
    Product("X", "x", 1, 1)
    raise SystemExit("FAIL: Product instantiated")
except TypeError as e:
    print("Product() rejected:", e)

assert isinstance(phys, CanBeShipped) and not isinstance(dig, CanBeShipped)
for w in (0, 1, 10):
    print(f"{w} kg ->", PhysicalProduct("W", "w", 1, 1, w).calculate_shipping_cost())
assert phys.calculate_shipping_cost() == 15.0

inv = Inventory()
assert inv.add_product(phys) and inv.add_product(dig)
assert not inv.add_product(PhysicalProduct("t1", "dup", 1, 1, 1))
inv.search_product("t1").update_stock(7)
inv.display_all()

with tempfile.TemporaryDirectory() as d:
    ims.INVENTORY_FILE = os.path.join(d, "inv.json")
    ims.save_inventory(inv)
    print(open(ims.INVENTORY_FILE).read())
    inv2 = Inventory()
    ims.load_inventory(inv2)
    p, q = inv2.search_product("T1"), inv2.search_product("T2")
    assert type(p) is PhysicalProduct and type(q) is DigitalProduct
    assert p.get_weight() == 4.0 and p.get_stock() == 7 and q.get_download_size() == 4096
print("ALL TESTS PASSED")
