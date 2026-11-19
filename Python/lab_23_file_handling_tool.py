import os

FILENAME = "student_marks.txt"

# Pre-populate student_marks.txt with sample student records if it doesn't exist
if not os.path.exists(FILENAME):
    with open(FILENAME, "w") as file:
        file.write("Aman,85\n")
        file.write("Riya,92\n")
        file.write("Karan,78\n")


# 1. Functional Requirements

def store_student(filename, name, marks):
    """Opens student_marks.txt in append mode ('a') and stores Name,Marks."""
    with open(filename, "a") as file:
        file.write(f"{name},{marks}\n")
    print(f"[SUCCESS] Record for '{name}' ({marks} marks) stored successfully.")


def display_and_calculate_average(filename):
    """Reads records line-by-line, displays formatted table, and computes class average."""
    if not os.path.exists(filename):
        print("[INFO] No student records file found.")
        return

    names = []
    marks_list = []

    with open(filename, "r") as file:
        for line in file:
            clean_line = line.strip()
            if clean_line != "":
                parts = clean_line.split(",")
                names.append(parts[0])
                marks_list.append(int(parts[1]))

    if len(marks_list) == 0:
        print("[INFO] No student records available.")
        return

    print("---------------- STUDENT MARKS LEDGER ----------------")
    print(f"{'No.':<5}{'Student Name':<19}{'Marks Obtained'}")
    print("------------------------------------------------------")

    for i in range(len(names)):
        print(f"{i + 1:<5}{names[i]:<19}{marks_list[i]}")

    total_marks = sum(marks_list)
    average = total_marks / len(marks_list)

    print("------------------------------------------------------")
    print(f"Total Students : {len(marks_list)}")
    print(f"Total Marks    : {total_marks}")
    print(f"Class Average  : {average:.2f}")


# 2. Main Menu Control Flow
print("==================================================")
print("          STUDENT MARKS FILE HANDLING TOOL        ")
print("==================================================")

while True:
    print("\nSelect an operation:")
    print("1. Display Records & Class Average")
    print("2. Add & Store Student Marks")
    print("3. Exit")

    choice = input("\nEnter choice (1-3): ")

    # Choice 1: Display Records & Class Average
    if choice == "1":
        display_and_calculate_average(FILENAME)

    # Choice 2: Add & Store Student Marks
    elif choice == "2":
        name = input("Enter Student Name: ")
        marks = int(input("Enter Marks (0-100): "))
        
        if marks < 0 or marks > 100:
            print("[ERROR] Marks must be between 0 and 100.")
        else:
            store_student(FILENAME, name, marks)

    # Choice 3: Exit
    elif choice == "3":
        print("Thank you for using Student Marks Tool. Goodbye!")
        break

    # Invalid Choice
    else:
        print("[ERROR] Invalid choice! Please enter a number between 1 and 3.")