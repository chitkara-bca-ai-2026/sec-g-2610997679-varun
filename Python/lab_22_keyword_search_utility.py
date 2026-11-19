import os

FILENAME = "report.txt"

# Pre-populate report.txt with sample corporate report text if it doesn't exist
if not os.path.exists(FILENAME):
    with open(FILENAME, "w") as file:
        file.write("Annual Technology and AI Progress Report.\n")
        file.write("The adoption of Artificial Intelligence accelerated across business units.\n")
        file.write("AI algorithms improved diagnostic accuracy in healthcare operations.\n")
        file.write("Data engineering pipelines were upgraded to support real-time data streaming.\n")
        file.write("The company plans further investments in AI research and machine learning.\n")


# 1. Search and Display Functions

def search_keyword(filename, keyword):
    """Searches for keyword line by line (case-insensitive) and displays matches."""
    print(f"--- Search Results for '{keyword}' ---")
    if not os.path.exists(filename):
        print("[ERROR] Report file not found.")
        return

    total_occurrences = 0
    key_lower = keyword.lower()

    with open(filename, "r") as file:
        for line_num, line in enumerate(file, start=1):
            clean_line = line.rstrip()
            line_lower = clean_line.lower()
            
            if key_lower in line_lower:
                matches_in_line = line_lower.count(key_lower)
                total_occurrences += matches_in_line
                match_word = "match" if matches_in_line == 1 else "matches"
                print(f"Line {line_num} ({matches_in_line} {match_word}): {clean_line}")

    if total_occurrences > 0:
        print(f"\n[FOUND] Total occurrences of '{keyword}': {total_occurrences}")
    else:
        print(f"\n[NOT FOUND] No occurrences of '{keyword}' found in the document.")


def display_document(filename):
    """Reads and displays all text lines with line numbers."""
    print(f"--- Full Report Document ({filename}) ---")
    if not os.path.exists(filename):
        print("[ERROR] Report file not found.")
        return

    with open(filename, "r") as file:
        for line_num, line in enumerate(file, start=1):
            print(f"{line_num} | {line.rstrip()}")


# 2. Main Menu Control Flow
print("==================================================")
print("              KEYWORD SEARCH UTILITY              ")
print("==================================================")

while True:
    print("\nSelect an operation:")
    print("1. Search Keyword in Document")
    print("2. View Full Document")
    print("3. Exit")

    choice = input("\nEnter choice (1-3): ")

    # Choice 1: Search Keyword
    if choice == "1":
        keyword = input("Enter keyword to search: ")
        if keyword.strip() == "":
            print("[ERROR] Keyword cannot be empty.")
        else:
            search_keyword(FILENAME, keyword)

    # Choice 2: View Full Document
    elif choice == "2":
        display_document(FILENAME)

    # Choice 3: Exit
    elif choice == "3":
        print("Thank you for using Keyword Search Utility. Goodbye!")
        break

    # Invalid Choice
    else:
        print("[ERROR] Invalid choice! Please enter a number between 1 and 3.")