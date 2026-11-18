print("============================================")
print("          SCHOOL RESULT PROCESSING")
print("============================================")

# 1. Accept student details
name = input("Enter Student Name : ")
roll_number = input("Enter Roll Number  : ")
print()

print("--- Enter Marks for 5 Subjects (0-100) ---")

total_marks = 0
has_failed = False

# 2. Input marks for 5 subjects using a loop
for i in range(1, 6):
    mark = float(input("Enter marks for Subject " + str(i) + ": "))
    
    # Validate each mark
    if mark < 0 or mark > 100:
        print("Error: Marks must be between 0 and 100. Exiting program.")
        exit()
        
    total_marks = total_marks + mark
    
    # Check passing status for each subject
    if mark < 40:
        has_failed = True

print("============================================")
print()

# 3. Calculate total and percentage
percentage = (total_marks / 500) * 100

# 4. Assign Grade & Remark using if-elif-else
if has_failed == True:
    result = "FAIL"
    grade = "F"
    remarks = "Failed in one or more subjects"
else:
    result = "PASS"
    if percentage >= 90 and percentage <= 100:
        grade = "A+"
        remarks = "Outstanding"
    elif percentage >= 80 and percentage < 90:
        grade = "A"
        remarks = "Excellent"
    elif percentage >= 70 and percentage < 80:
        grade = "B"
        remarks = "Very Good"
    elif percentage >= 60 and percentage < 70:
        grade = "C"
        remarks = "Good"
    elif percentage >= 50 and percentage < 60:
        grade = "D"
        remarks = "Satisfactory"
    elif percentage >= 40 and percentage < 50:
        grade = "E"
        remarks = "Pass"
    else:
        grade = "F"
        remarks = "Fail"

# 5. Display a formatted Report Card
print("============================================")
print("            STUDENT REPORT CARD")
print("============================================")
print("Student Name :", name)
print("Roll Number  :", roll_number)
print("--------------------------------------------")
print("Total Marks  :", total_marks, "/ 500.0")
print("Percentage   :", round(percentage, 2), "%")
print("Result       :", result)
print("Grade        :", grade)
print("Remarks      :", remarks)
print("============================================")