import json
import os

INVENTORY_FILE = "inventory.json"
LINE = "-" * 48


def load_inventory():
    """Load inventory from inventory.json if it exists, else return an empty list."""
    if os.path.exists(INVENTORY_FILE):
        print(f"{INVENTORY_FILE} found.")
        try:
            with open(INVENTORY_FILE, "r") as f:
                inventory = json.load(f)
            print("Inventory loaded successfully.")
            return inventory
        except (json.JSONDecodeError, OSError):
            print("Error reading inventory file. Starting with empty inventory.")
            return []
    print(f"{INVENTORY_FILE} not found. Starting with empty inventory.")
    return []


def save_inventory(inventory):
    """Save the inventory list to inventory.json."""
    with open(INVENTORY_FILE, "w") as f:
        json.dump(inventory, f, indent=4)


def find_product(inventory, product_id):
    for product in inventory:
        if product["id"].upper() == product_id.upper():
            return product
    return None


def display_all(inventory):
    print("Current Inventory")
    print(LINE)
    if not inventory:
        print("No products in inventory.")
    for p in inventory:
        print(f"ID: {p['id']} | Name: {p['name']} | Price: ${p['price']:.2f} | Stock: {p['stock']}")
    print(LINE)


def add_product(inventory):
    print("Add New Product")
    product_id = input("Product ID: ").strip().upper()
    if not product_id:
        print("Product ID cannot be empty.")
        return
    if find_product(inventory, product_id):
        print("Product ID already exists.")
        return
    name = input("Product Name: ").strip()
    try:
        price = float(input("Price: "))
        stock = int(input("Stock Quantity: "))
        if price < 0 or stock < 0:
            raise ValueError
    except ValueError:
        print("Invalid price or stock. Product not added.")
        return
    inventory.append({"id": product_id, "name": name, "price": price, "stock": stock})
    print("Product added successfully!")


def update_stock(inventory):
    print("Update Stock")
    product = find_product(inventory, input("Enter Product ID: ").strip())
    if not product:
        print("Product not found.")
        return
    print("Product Found:")
    print(f"Name: {product['name']}")
    print(f"Current Stock: {product['stock']}")
    try:
        new_stock = int(input("New Stock Quantity: "))
        if new_stock < 0:
            raise ValueError
    except ValueError:
        print("Invalid stock quantity. Stock not updated.")
        return
    product["stock"] = new_stock
    print("Stock updated successfully!")


def search_product(inventory):
    print("Search Product")
    product = find_product(inventory, input("Enter Product ID: ").strip())
    if not product:
        print("Product not found.")
        return
    print("Product Found")
    print(LINE)
    print(f"ID: {product['id']}")
    print(f"Name: {product['name']}")
    print(f"Price: ${product['price']:.2f}")
    print(f"Stock: {product['stock']}")
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
    inventory = load_inventory()
    show_menu()

    while True:
        option = input("Enter option: ").strip()
        if option == "1":
            display_all(inventory)
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
