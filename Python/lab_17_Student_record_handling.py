# 1. Data Setup: Pre-populated dictionary with 3 student records
students = {
    "101": {
        "Name": "Aman",
        "Marks": [85, 90, 78]
    },
    "102": {
        "Name": "Riya",
        "Marks": [92, 88, 95]
    },
    "103": {
        "Name": "Karan",
        "Marks": [74, 80, 82]
    }
}

# 2. Functions to Implement

def calculate_results(marks):
    """Receives a list of marks, calculates and returns total and average."""
    total = sum(marks)
    average = total / len(marks)
    return total, average

def display_student(roll, student):
    """Calls calculate_results() and prints a formatted student record line."""
    total, average = calculate_results(student["Marks"])
    print(f"Roll No: {roll} | Name: {student['Name']:<8} | Marks: {student['Marks']} | Total: {total} | Average: {average:.2f}%")

def add_student(records, roll, name, marks):
    """Adds a new student if roll number is unique, otherwise shows an error."""
    if roll in records:
        print(f"[ERROR] Student with Roll Number '{roll}' already exists!")
    else:
        records[roll] = {
            "Name": name,
            "Marks": marks
        }
        print(f"[SUCCESS] Student '{name}' (Roll No: {roll}) added successfully.")


# 3. Main Menu Control Flow
print("==================================================")
print("         STUDENT RECORDS MANAGEMENT SYSTEM        ")
print("==================================================")

while True:
    print("\nSelect an operation:")
    print("1. Display All Students")
    print("2. Add New Student")
    print("3. Search Student")
    print("4. Exit")

    choice = input("\nEnter choice (1-4): ")

    # Choice 1: Display All Students
    if choice == "1":
        print("\n--- All Student Records ---")
        if len(students) == 0:
            print("No student records available.")
        else:
            for roll, student in students.items():
                display_student(roll, student)
            print(f"Total Students: {len(students)}")

    # Choice 2: Add New Student
    elif choice == "2":
        print("\n--- Add New Student ---")
        roll = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")
        print("Enter marks for 3 subjects:")
        m1 = int(input("Subject 1: "))
        m2 = int(input("Subject 2: "))
        m3 = int(input("Subject 3: "))
        
        add_student(students, roll, name, [m1, m2, m3])

    # Choice 3: Search Student
    elif choice == "3":
        roll = input("Enter Roll Number to search: ")
        student = students.get(roll)
        
        if student is not None:
            print("[RECORD FOUND]")
            display_student(roll, student)
        else:
            print(f"[ERROR] No student found with Roll Number '{roll}'.")

    # Choice 4: Exit
    elif choice == "4":
        print("\nThank you for using the Student Records System. Goodbye!")
        break

    # Invalid Input
    else:
        print("\n[ERROR] Invalid choice! Please enter a number between 1 and 4.")