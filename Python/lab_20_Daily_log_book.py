import os

FILENAME = "daily_log.txt"

# Pre-populate daily_log.txt with sample office entries if it doesn't exist yet
if not os.path.exists(FILENAME):
    with open(FILENAME, "w") as file:
        file.write("09:00 AM - System server startup verified.\n")
        file.write("10:30 AM - Morning attendance synchronized.\n")


# 1. File Handling Operations

def append_entry(filename, entry):
    """Opens the file in append mode ('a') and adds a new entry on a new line."""
    with open(filename, "a") as file:
        file.write(entry + "\n")
    print(f"[SUCCESS] New entry logged to '{filename}'.")


def display_log(filename):
    """Opens the file in read mode ('r') and displays all entries with count."""
    print("================ DAILY LOG BOOK ================")
    if not os.path.exists(filename):
        print("No log entries found.")
        print("================================================")
        print("\nTotal Logged Entries: 0")
        return

    with open(filename, "r") as file:
        entries = [line.strip() for line in file.readlines() if line.strip()]

    for index, entry in enumerate(entries, start=1):
        print(f"[{index:02d}] {entry}")

    print("================================================")
    print(f"\nTotal Logged Entries: {len(entries)}")


# 2. Main Menu Control Flow
print("==================================================")
print("               OFFICE DAILY LOG BOOK              ")
print("==================================================")

while True:
    print("\nSelect an operation:")
    print("1. Add Log Entry")
    print("2. Display Complete Log")
    print("3. Exit")

    choice = input("\nEnter choice (1-3): ")

    # Choice 1: Add Log Entry
    if choice == "1":
        entry = input("Enter log entry: ")
        append_entry(FILENAME, entry)

    # Choice 2: Display Complete Log
    elif choice == "2":
        display_log(FILENAME)

    # Choice 3: Exit
    elif choice == "3":
        print("Thank you for using the Daily Log Book. Goodbye!")
        break

    # Invalid Choice
    else:
        print("[ERROR] Invalid choice! Please enter a number between 1 and 3.")