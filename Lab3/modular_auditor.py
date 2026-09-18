def get_valid_input():
    entry = input("Enter stock quantity (or 'quit' to exit): ")

    if entry == "quit":
        return "quit"

    if not entry.isdigit():
        print("Error: please enter a valid non-negative integer.")
        return None

    return int(entry)


def process_delivery(current_total, new_value):
    return current_total + new_value


def calculate_tax(amount):
    return amount * 0.10


def generate_report(total_units, failed_attempts):
    print(f"Total Units Processed: {total_units}")
    print(f"Number of Failed/Rejected Entries: {failed_attempts}")


def main():
    total_inventory = 0
    units_processed = 0
    failed_entries = 0

    while True:
        entry = get_valid_input()

        if entry == "quit":
            break

        if entry is None:
            failed_entries += 1
            continue

        quantity = entry
        total_inventory = process_delivery(total_inventory, quantity)
        units_processed += quantity
        tax = calculate_tax(quantity)

        print(f"Accepted. Current total inventory: {total_inventory}")
        print(f"Tax for this delivery: {tax:.2f}")

        if total_inventory > 500:
            print("ALERT: Overstock! Total inventory exceeds 500 units.")
            break

    generate_report(units_processed, failed_entries)


if __name__ == "__main__":
    main()
