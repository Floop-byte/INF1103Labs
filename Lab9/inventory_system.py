import json
import os

from inventory import Inventory, LINE
from product_factory import ProductFactory
from supplier import Supplier

INVENTORY_FILE = "inventory.json"


# ---------- File handling ----------
def product_from_dict(item, supplier: Supplier):
    """Create the correct Product subclass from a saved dictionary."""
    product_type = item["type"]
    if product_type == "physical":
        extra = item["weight"]
    elif product_type == "digital":
        extra = item["download_size"]
    else:
        raise ValueError(f"Unknown product type: {product_type}")
    return ProductFactory.create(
        product_type, item["id"], item["name"], item["price"],
        item["stock"], extra, supplier
    )


def load_inventory(inventory, supplier: Supplier):
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


# ---------- Input helpers ----------
def get_positive_float(prompt: str) -> float:
    """Prompt repeatedly until the user enters a positive float."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a number greater than zero.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number, e.g. 12.50")


# ---------- Menu actions ----------
def add_product(inventory, supplier: Supplier):
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
        price = get_positive_float("Price: ")
        stock = int(input("Stock Quantity: "))
        if product_type == "1":
            extra = get_positive_float("Weight (kg): ")
            type_name = "physical"
        else:
            extra = get_positive_float("Download size (MB): ")
            type_name = "digital"
        product = ProductFactory.create(
            type_name, product_id, name, price, stock, extra, supplier
        )
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
    # Create the supplier independently, then share it with the products.
    supplier = Supplier(1111, "Amazon", "amazon@aws.com")
    inventory = Inventory()
    load_inventory(inventory, supplier)
    show_menu()

    while True:
        option = input("Enter option: ").strip()
        if option == "1":
            inventory.display_all()
        elif option == "2":
            add_product(inventory, supplier)
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
