import os

# 1. File Handling Functions

def write_notes(filename, content):
    """Opens the file in write mode ('w') and saves the notes."""
    with open(filename, "w") as file:
        file.write(content)
    print(f"[SUCCESS] Notes successfully saved to '{filename}'.")


def read_notes(filename):
    """Checks if file exists using os.path.exists(), then reads and returns content."""
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return file.read()
    else:
        return "[INFO] No notes file exists yet. Please write some notes first."


# 2. Main Menu Control Flow
FILENAME = "notes.txt"

print("==================================================")
print("          STUDENT NOTES MANAGEMENT SYSTEM         ")
print("==================================================")

while True:
    print("\nSelect an operation:")
    print("1. Write / Save Notes")
    print("2. View Saved Notes")
    print("3. Exit")

    choice = input("\nEnter choice (1-3): ")

    # Choice 1: Write / Save Notes
    if choice == "1":
        notes_text = input("Enter notes to save: ")
        write_notes(FILENAME, notes_text)

    # Choice 2: View Saved Notes
    elif choice == "2":
        print(f"--- Notes Content ({FILENAME}) ---")
        content = read_notes(FILENAME)
        print(content)

    # Choice 3: Exit
    elif choice == "3":
        print("Thank you for using the Notes Management System. Goodbye!")
        break

    # Invalid Choice
    else:
        print("[ERROR] Invalid choice! Please enter a number between 1 and 3.")