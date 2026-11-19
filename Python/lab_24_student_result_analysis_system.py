import csv
import os

FILENAME = "students_data.csv"

# 1. Pre-populate students_data.csv with 6 sample records if it doesn't exist
if not os.path.exists(FILENAME):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["RollNo", "Name", "Subject", "Marks"])
        writer.writerow(["101", "Aman", "Python", "85"])
        writer.writerow(["102", "Riya", "Python", "92"])
        writer.writerow(["103", "Karan", "Python", "45"])
        writer.writerow(["104", "Neha", "Python", "76"])
        writer.writerow(["105", "Rohit", "Python", "38"])
        writer.writerow(["106", "Pooja", "Python", "82"])


# 2. Functional Requirements

def read_all_students(filename):
    """Reads the CSV file using csv.DictReader and prints all rows in a table."""
    if not os.path.exists(filename):
        print("[ERROR] CSV file not found.")
        return

    print("---------------- ALL ENROLLED STUDENTS ----------------")
    print(f"{'Roll No':<12}{'Name':<14}{'Subject':<14}{'Marks'}")
    print("-------------------------------------------------------")

    count = 0
    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"{row['RollNo']:<12}{row['Name']:<14}{row['Subject']:<14}{row['Marks']}")
            count += 1

    print("-------------------------------------------------------")
    print(f"Total Records: {count}")


def filter_students_above_threshold(filename, threshold=50):
    """Filters and displays students scoring strictly above threshold."""
    if not os.path.exists(filename):
        print("[ERROR] CSV file not found.")
        return

    print(f"------------ STUDENTS WITH MARKS > {threshold} ------------")
    print(f"{'Roll No':<12}{'Name':<14}{'Subject':<14}{'Marks'}")
    print("-------------------------------------------------------")

    qualified_count = 0
    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if int(row["Marks"]) > threshold:
                print(f"{row['RollNo']:<12}{row['Name']:<14}{row['Subject']:<14}{row['Marks']}")
                qualified_count += 1

    print("-------------------------------------------------------")
    print(f"Qualified Students Count: {qualified_count}")


# 3. Main Menu Control Flow
print("==================================================")
print("          STUDENT RESULT ANALYSIS SYSTEM          ")
print("==================================================")

while True:
    print("\nSelect an operation:")
    print("1. Display All Students from CSV")
    print("2. Filter Students (Marks > 50)")
    print("3. Exit")

    choice = input("\nEnter choice (1-3): ")

    # Choice 1: Display All Students
    if choice == "1":
        read_all_students(FILENAME)

    # Choice 2: Filter Students (Marks > 50)
    elif choice == "2":
        filter_students_above_threshold(FILENAME)

    # Choice 3: Exit
    elif choice == "3":
        print("Thank you for using Student Result Analysis System. Goodbye!")
        break

    # Invalid Choice
    else:
        print("[ERROR] Invalid choice! Please enter a number between 1 and 3.")