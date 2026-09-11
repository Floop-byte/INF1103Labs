total_inventory = 0
units_processed = 0
failed_entries = 0

while True:
    entry = input("Enter stock quantity (or 'quit' to exit): ")

    if entry == "quit":
        break

    if not entry.isdigit():
        print("Error: please enter a valid non-negative integer.")
        failed_entries += 1
        continue

    quantity = int(entry)

    total_inventory += quantity
    units_processed += quantity
    print(f"Accepted. Current total inventory: {total_inventory}")

    if total_inventory > 500:
        print("ALERT: Overstock! Total inventory exceeds 500 units.")
        break

print(f"Total Units Processed: {units_processed}")
print(f"Number of Failed/Rejected Entries: {failed_entries}")
