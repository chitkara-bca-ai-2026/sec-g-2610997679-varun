# 1. Modular Function Definitions

def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Returns the difference of two numbers."""
    return a - b

def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

def divide(a, b):
    """Returns a / b, or None if b == 0."""
    if b == 0:
        return None
    return a / b

def modulus(a, b):
    """Returns a % b, or None if b == 0."""
    if b == 0:
        return None
    return a % b

def power(base, exp=2):
    """Returns base raised to exp (defaults to square)."""
    return base ** exp

def format_number(n):
    """Helper returning an int if value has no decimal part, otherwise float."""
    if n == int(n):
        return int(n)
    return round(n, 4)


# 2. Session History List
history = []

print("==================================================")
print("       ENTERPRISE MODULAR UTILITY CALCULATOR      ")
print("==================================================")

# 3. Control Flow & Input Validation
while True:
    print("\nSelect an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus / Remainder (%)")
    print("6. Power / Exponentiation (Default: Square)")
    print("7. View Calculation History")
    print("8. Exit")

    choice = input("\nEnter your choice (1-8): ")

    # Option 1: Addition
    if choice == "1":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        res = add(a, b)
        record = f"{format_number(a)} + {format_number(b)} = {format_number(res)}"
        print(f"[RESULT] {record}")
        history.append(record)

    # Option 2: Subtraction
    elif choice == "2":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        res = subtract(a, b)
        record = f"{format_number(a)} - {format_number(b)} = {format_number(res)}"
        print(f"[RESULT] {record}")
        history.append(record)

    # Option 3: Multiplication
    elif choice == "3":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        res = multiply(a, b)
        record = f"{format_number(a)} * {format_number(b)} = {format_number(res)}"
        print(f"[RESULT] {record}")
        history.append(record)

    # Option 4: Division (Defensive check for zero)
    elif choice == "4":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        res = divide(a, b)
        if res is None:
            print("[ERROR] Division by zero is not allowed!")
        else:
            record = f"{format_number(a)} / {format_number(b)} = {format_number(res)}"
            print(f"[RESULT] {record}")
            history.append(record)

    # Option 5: Modulus (Defensive check for zero)
    elif choice == "5":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        res = modulus(a, b)
        if res is None:
            print("[ERROR] Modulus by zero is not allowed!")
        else:
            record = f"{format_number(a)} % {format_number(b)} = {format_number(res)}"
            print(f"[RESULT] {record}")
            history.append(record)

    # Option 6: Power / Exponentiation (Default argument exp=2)
    elif choice == "6":
        base = float(input("Enter base number: "))
        exp_input = input("Enter exponent (press Enter for default 2): ")
        if exp_input.strip() == "":
            res = power(base)
            record = f"{format_number(base)} ^ 2 = {format_number(res)}"
        else:
            exp = float(exp_input)
            res = power(base, exp)
            record = f"{format_number(base)} ^ {format_number(exp)} = {format_number(res)}"
        print(f"[RESULT] {record}")
        history.append(record)

    # Option 7: View Calculation History
    elif choice == "7":
        print("\n--- Session Calculation History ---")
        if len(history) == 0:
            print("No calculations performed yet.")
        else:
            for index, item in enumerate(history, start=1):
                print(f"{index}. {item}")

    # Option 8: Exit
    elif choice == "8":
        print("\nThank you for using Enterprise Modular Utility Calculator. Goodbye!")
        break

    # Invalid Choice
    else:
        print("\n[ERROR] Invalid choice! Please enter a number between 1 and 8.")