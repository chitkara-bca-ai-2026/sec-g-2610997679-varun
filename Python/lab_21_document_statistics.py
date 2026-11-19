import os

FILENAME = "document.txt"

# Pre-populate document.txt with sample publishing text if it doesn't exist
if not os.path.exists(FILENAME):
    with open(FILENAME, "w") as file:
        file.write("Artificial Intelligence is transforming modern industries.\n")
        file.write("Python provides powerful libraries for text processing and data analysis.\n")
        file.write("Developers use file handling to store and retrieve persistent records.\n")
        file.write("Modular programming ensures code is clean, reusable, and easy to maintain.\n")


# 1. Document Analysis Functions

def get_document_statistics(filename):
    """Reads the entire file and returns a tuple: (line_count, word_count, char_count)."""
    if not os.path.exists(filename):
        return 0, 0, 0

    with open(filename, "r") as file:
        content = file.read()

    lines = content.splitlines()
    line_count = len(lines)
    word_count = len(content.split())
    char_count = len(content)

    return line_count, word_count, char_count


def display_document(filename):
    """Reads and prints each line prefixed by its line number."""
    print(f"--- Document Preview ({filename}) ---")
    if not os.path.exists(filename):
        print("[ERROR] Document file not found.")
        return

    with open(filename, "r") as file:
        lines = file.readlines()

    for index, line in enumerate(lines, start=1):
        print(f"{index} | {line.rstrip()}")


# 2. Main Menu Control Flow
print("==================================================")
print("            DOCUMENT STATISTICS ANALYZER          ")
print("==================================================")

while True:
    print("\nSelect an operation:")
    print("1. Calculate Document Statistics")
    print("2. Display Document Content")
    print("3. Exit")

    choice = input("\nEnter choice (1-3): ")

    # Choice 1: Calculate Document Statistics
    if choice == "1":
        lines, words, chars = get_document_statistics(FILENAME)
        print("---------------- DOCUMENT REPORT ----------------")
        print(f"Target File      : {FILENAME}")
        print(f"Total Lines      : {lines}")
        print(f"Total Words      : {words}")
        print(f"Total Characters : {chars}")
        print("-------------------------------------------------")

    # Choice 2: Display Document Content
    elif choice == "2":
        display_document(FILENAME)

    # Choice 3: Exit
    elif choice == "3":
        print("Thank you for using Document Statistics Analyzer. Goodbye!")
        break

    # Invalid Choice
    else:
        print("[ERROR] Invalid choice! Please enter a number between 1 and 3.")