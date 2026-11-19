# 1. Initial Data Setup: Nested dictionary with 3 default students
students = {
    "101": {
        "Name": "Aman",
        "Branch": "BCA AI",
        "Semester": "1",
        "Marks": [85, 90, 78]
    },
    "102": {
        "Name": "Riya",
        "Branch": "BCA AI",
        "Semester": "1",
        "Marks": [92, 88, 95]
    },
    "103": {
        "Name": "Karan",
        "Branch": "BCA AI",
        "Semester": "1",
        "Marks": [74, 80, 82]
    }
}

print("==================================================")
print("       STUDENT INFORMATION MANAGEMENT SYSTEM      ")
print("==================================================")

# 2. Control Flow: Infinite loop until user chooses Exit (7)
while True:
    print("\nSelect an operation:")
    print("1. View All Students")
    print("2. Search Student by Roll Number")
    print("3. Register New Student")
    print("4. Update Student Details")
    print("5. View Academic Performance")
    print("6. Delete Student Record")
    print("7. Exit")
    
    choice = input("\nEnter your choice (1-7): ")

    # Choice 1: View All Students using .items()
    if choice == "1":
        print("\n--- Enrolled Student Records ---")
        if len(students) == 0:
            print("No student records found.")
        else:
            for roll, details in students.items():
                print(f"Roll No: {roll}  | Name: {details['Name']}       | Branch: {details['Branch']}")
                print(f"| Sem: {details['Semester']} | Marks: {details['Marks']}")
            print(f"Total Enrolled Students: {len(students)}")

    # Choice 2: Search Student by Roll Number using .get()
    elif choice == "2":
        roll = input("Enter Roll Number to search: ")
        student = students.get(roll)
        
        if student is not None:
            print(f"\n[FOUND] Record for Roll No {roll}:")
            print(f"Name     : {student['Name']}")
            print(f"Branch   : {student['Branch']}")
            print(f"Semester : {student['Semester']}")
            print(f"Marks    : {student['Marks']}")
        else:
            print(f"\n[ERROR] Student with Roll No {roll} not found.")

    # Choice 3: Register New Student
    elif choice == "3":
        print("\n--- Register New Student ---")
        roll = input("Enter Roll Number: ")
        
        if roll in students:
            print(f"[ERROR] Roll Number {roll} already exists!")
        else:
            name = input("Enter Student Name: ")
            branch = input("Enter Branch (e.g. BCA AI): ")
            semester = input("Enter Semester: ")
            
            print("Enter marks obtained in 3 subjects:")
            m1 = int(input("Subject 1: "))
            m2 = int(input("Subject 2: "))
            m3 = int(input("Subject 3: "))
            
            students[roll] = {
                "Name": name,
                "Branch": branch,
                "Semester": semester,
                "Marks": [m1, m2, m3]
            }
            print(f"\n[SUCCESS] Student '{name}' (Roll No: {roll}) registered successfully.")

    # Choice 4: Update Student Details
    elif choice == "4":
        roll = input("Enter Roll Number to update: ")
        
        if roll in students:
            student = students[roll]
            print(f"Current details for {student['Name']} (Roll {roll}):")
            print(f"1. Branch: {student['Branch']} | 2. Semester: {student['Semester']}")
            field_choice = input("Choose field to update (1 for Branch, 2 for Semester): ")
            
            if field_choice == "1":
                new_branch = input("Enter new branch: ")
                students[roll]["Branch"] = new_branch
                print(f"[SUCCESS] Branch updated to '{new_branch}'.")
            elif field_choice == "2":
                new_sem = input("Enter new semester: ")
                students[roll]["Semester"] = new_sem
                print(f"[SUCCESS] Semester updated to '{new_sem}'.")
            else:
                print("[ERROR] Invalid choice.")
        else:
            print(f"[ERROR] Student with Roll No {roll} not found.")

    # Choice 5: View Academic Performance
    elif choice == "5":
        roll = input("Enter Roll Number for Academic Performance: ")
        student = students.get(roll)
        
        if student is not None:
            marks = student["Marks"]
            total = sum(marks)
            average = total / len(marks)
            
            if average >= 40:
                status = "PASS"
            else:
                status = "FAIL"
                
            print("\n================ ACADEMIC REPORT ================")
            print(f"Student Name : {student['Name']} (Roll: {roll})")
            print(f"Subject Marks: {marks}")
            print(f"Total Marks  : {total} / 300")
            print(f"Average Marks: {average:.2f}%")
            print(f"Final Result : {status}")
            print("=================================================")
        else:
            print(f"[ERROR] Student with Roll No {roll} not found.")

    # Choice 6: Delete Student Record using .pop()
    elif choice == "6":
        roll = input("Enter Roll Number to delete: ")
        removed = students.pop(roll, None)
        
        if removed is not None:
            print(f"\n[SUCCESS] Record for '{removed['Name']}' (Roll No: {roll}) deleted successfully.")
        else:
            print(f"\n[ERROR] Student with Roll No {roll} not found.")

    # Choice 7: Exit
    elif choice == "7":
        print("\nThank you for using Student Information System.")
        print("Goodbye!")
        break

    # Invalid Menu Choice
    else:
        print("\n[ERROR] Invalid choice! Please enter a number between 1 and 7.")