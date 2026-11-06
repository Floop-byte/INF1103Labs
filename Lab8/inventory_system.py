import json
import os

from inventory import Inventory, LINE
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from supplier import Supplier

INVENTORY_FILE = "inventory.json"
amazonSupplier = Supplier(supplier_id=1111, name="Amazon",
                          contact_email="amazon@aws.com")


# ---------- File handling ----------
def product_from_dict(item, supplier):
    """Create the correct Product subclass from a saved dictionary."""
    product_type = item["type"]
    if product_type == "physical":
        return PhysicalProduct(item["id"], item["name"], item["price"],
                               item["stock"], item["weight"], supplier)
    if product_type == "digital":
        return DigitalProduct(item["id"], item["name"], item["price"],
                              item["stock"], item["download_size"], supplier)
    raise ValueError(f"Unknown product type: {product_type}")


def load_inventory(inventory, supplier):
    """Load products from inventory.json into the given Inventory."""
    if not os.path.exists(INVENTORY_FILE):
        print(f"{INVENTORY_FILE} not found. Starting with empty inventory.")
        return
    print(f"{INVENTORY_FILE} found.")
    try:
        with open(INVENTORY_FILE, "r") as f:
            data = json.load(f)
        for item in data:
            inventory.add_product(product_from_dict(item, supplier))
        print("Inventory loaded successfully.")
    except (json.JSONDecodeError, OSError, KeyError, TypeError, ValueError):
        print("Error reading inventory file. Starting with empty inventory.")


def save_inventory(inventory):
    """Save all products in the Inventory to inventory.json."""
    data = [p.to_dict() for p in inventory.get_products()]
    with open(INVENTORY_FILE, "w") as f:
        json.dump(data, f, indent=4)


# ---------- Menu actions ----------
def add_product(inventory):
    print("Add New Product")
    product_id = input("Product ID: ").strip().upper()
    if not product_id:
        print("Product ID cannot be empty.")
        return
    if inventory.search_product(product_id):
        print("Product ID already exists.")
        return
    product_type = input("Product type (1. Physical, 2. Digital): ").strip()
    if product_type not in ("1", "2"):
        print("Invalid product type. Product not added.")
        return
    name = input("Product Name: ").strip()
    try:
        price = float(input("Price: "))
        stock = int(input("Stock Quantity: "))
        if product_type == "1":
            weight = float(input("Weight (kg): "))
            product = PhysicalProduct(product_id, name, price, stock, weight, amazonSupplier)
        else:
            size = float(input("Download size (MB): "))
            product = DigitalProduct(product_id, name, price, stock, size, amazonSupplier)
    except ValueError:
        print("Invalid input. Product not added.")
        return
    inventory.add_product(product)
    print("Product added successfully!")


def update_stock(inventory):
    print("Update Stock")
    product = inventory.search_product(input("Enter Product ID: ").strip())
    if not product:
        print("Product not found.")
        return
    print("Product Found:")
    print(f"Name: {product.get_name()}")
    print(f"Current Stock: {product.get_stock()}")
    try:
        product.update_stock(int(input("New Stock Quantity: ")))
    except ValueError:
        print("Invalid stock quantity. Stock not updated.")
        return
    print("Stock updated successfully!")


def search_product(inventory):
    print("Search Product")
    product = inventory.search_product(input("Enter Product ID: ").strip())
    if not product:
        print("Product not found.")
        return
    print("Product Found")
    print(LINE)
    product.display_information()
    print(f"  Fulfilment: {product.get_fulfilment_info()}")
    print(LINE)


def show_menu():
    print("----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")


def main():
    print("=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 40)
    inventory = Inventory()
    load_inventory(inventory, amazonSupplier)
    show_menu()

    while True:
        option = input("Enter option: ").strip()
        if option == "1":
            inventory.display_all()
        elif option == "2":
            add_product(inventory)
        elif option == "3":
            update_stock(inventory)
        elif option == "4":
            search_product(inventory)
        elif option == "5":
            print("Saving inventory...")
            save_inventory(inventory)
            print(f"Inventory saved successfully to {INVENTORY_FILE}.")
        elif option == "6":
            print("Saving inventory before exit...")
            save_inventory(inventory)
            print("Inventory saved successfully.")
            print("Thank you for using Inventory Management System.")
            print("Program terminated.")
            break
        else:
            print("Invalid option. Please enter 1-6.")
            show_menu()


if __name__ == "__main__":
    main()
