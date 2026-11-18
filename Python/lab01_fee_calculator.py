# 1. Take input from the user
tuition_fee = float(input("Enter Tuition Fee: "))
lab_fee = float(input("Enter Lab Fee: "))
library_fee = float(input("Enter Library Fee: "))
exam_fee = float(input("Enter Exam Fee: "))
discount = float(input("Enter Discount Amount: "))

# 2. Perform calculations
total_fee = tuition_fee + lab_fee + library_fee + exam_fee
fee_after_discount = total_fee - discount
annual_fee = fee_after_discount * 2

# Rounding to 2 decimal places manually for the installment
monthly_installment = round(annual_fee / 12, 2)

# 3. Display the results using basic commas (No 'f' strings used)
print()  # This prints the blank line before the output
print("Tuition Fee:", tuition_fee)
print("Lab Fee:", lab_fee)
print("Library Fee:", library_fee)
print("Exam Fee:", exam_fee)
print("Total Fee:", total_fee)
print("Discount:", discount)
print("Fee after Discount:", fee_after_discount)
print("Annual Fee:", annual_fee)
print("Monthly Installment:", monthly_installment)