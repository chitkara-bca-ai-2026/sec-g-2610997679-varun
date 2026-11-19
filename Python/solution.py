# Initialize the inventory list
inventory = ["Notebook", "Pen", "Eraser", "Ruler"]

print("==========================================")
print("         INVENTORY CONTROL SYSTEM         ")
print("==========================================")

# Run the menu continuously until the user exits
while True:
    print("\nSelect an operation:")
    print("1. View Inventory")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Sort Inventory")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ")

    if choice == "1":
        print("\n--- Current Inventory ---")
        # Loop through the list using index numbers to display 1, 2, 3...
        for i in range(len(inventory)):
            print(f"{i + 1}. {inventory[i]}")

    elif choice == "2":
        item = input("Enter item name to add: ")
        inventory.append(item)
        print(f'[SUCCESS] "{item}" added to inventory.')

    elif choice == "3":
        item = input("Enter item name to remove: ")
        # Check if the item exists before removing to avoid errors
        if item in inventory:
            inventory.remove(item)
            print(f'[SUCCESS] "{item}" removed from inventory.')
        else:
            print(f'[ERROR] "{item}" not found in inventory.')

    elif choice == "4":
        inventory.sort()
        print("\n[SUCCESS] Inventory sorted alphabetically.")
        print("Updated Inventory:")
        for i in range(len(inventory)):
            print(f"{i + 1}. {inventory[i]}")

    elif choice == "5":
        print("Exiting Inventory Control System. Goodbye!")
        break

    else:
        print("[ERROR] Invalid choice! Please enter a number between 1 and 5.")