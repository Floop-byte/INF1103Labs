import json
import os
import tempfile
from contextlib import redirect_stdout
from io import StringIO
from unittest.mock import patch
import Lab8.inventory_system_bk as ims
from inventory import Inventory
from product import Product
from can_be_shipped import CanBeShipped
from physical_product import PhysicalProduct
from digital_product import DigitalProduct

suppliers = ims.create_suppliers()
supplier = suppliers[2222]
phys = PhysicalProduct("T1", "Guitar", 500.0, 3, 4.0, supplier)
dig = DigitalProduct("T2", "OS", 99.0, 10, 4096, supplier)
assert phys.supplier is supplier and dig.supplier is supplier
assert phys is not dig and phys is not supplier and dig is not supplier
phys.display_information()
dig.display_information()
output = StringIO()
with redirect_stdout(output):
    phys.display_information()
    dig.display_information()
assert output.getvalue().count("Name: Book Haven") == 2

# A supplier can exist without products; products hold independent references.
unused_supplier = suppliers[4444]
assert unused_supplier.get_supplier_id() == 4444
del supplier
assert phys.supplier is dig.supplier is suppliers[2222]
temporary_product = PhysicalProduct("TEMP", "Sample", 1, 1, 1, unused_supplier)
del temporary_product
assert suppliers[4444] is unused_supplier

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
    print(f"{w} kg ->", PhysicalProduct("W", "w", 1, 1, w, suppliers[1111]).calculate_shipping_cost())
assert phys.calculate_shipping_cost() == 15.0

inv = Inventory()
assert inv.add_product(phys) and inv.add_product(dig)
assert not inv.add_product(PhysicalProduct("t1", "dup", 1, 1, 1, suppliers[1111]))
inv.search_product("t1").update_stock(7)
inv.display_all()

# Exercise both product types with different suppliers through the app prompts.
with patch("builtins.input", side_effect=["T3", "1", "3333", "Keyboard", "50", "2", "1"]):
    ims.add_product(inv, suppliers)
with patch("builtins.input", side_effect=["T4", "2", "4444", "E-book", "5", "10", "20"]):
    ims.add_product(inv, suppliers)
assert inv.search_product("T3").supplier is suppliers[3333]
assert inv.search_product("T4").supplier is suppliers[4444]
for invalid_supplier in ("9999", "abc"):
    with patch("builtins.input", side_effect=["BAD", "1", invalid_supplier]):
        ims.add_product(inv, suppliers)
    assert inv.search_product("BAD") is None

with tempfile.TemporaryDirectory() as d, patch.object(ims, "INVENTORY_FILE", os.path.join(d, "inv.json")):
    ims.save_inventory(inv)
    with open(ims.INVENTORY_FILE) as saved_file:
        saved_data = json.load(saved_file)
    assert [item["supplier_id"] for item in saved_data] == [2222, 2222, 3333, 4444]
    inv2 = Inventory()
    reloaded_suppliers = ims.create_suppliers()
    ims.load_inventory(inv2, reloaded_suppliers)
    p, q = inv2.search_product("T1"), inv2.search_product("T2")
    assert type(p) is PhysicalProduct and type(q) is DigitalProduct
    assert p.get_weight() == 4.0 and p.get_stock() == 7 and q.get_download_size() == 4096
    assert p.supplier is q.supplier is reloaded_suppliers[2222]
    assert inv2.search_product("T3").supplier is reloaded_suppliers[3333]
    assert inv2.search_product("T4").supplier is reloaded_suppliers[4444]
print("ALL TESTS PASSED")
