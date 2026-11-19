# 1. Recursive Functions

def factorial(n):
    """Calculates factorial of a non-negative integer using recursion."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    """Returns the n-th Fibonacci number (0-indexed) using recursion."""
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# 2. Main Menu Control Flow
print("==================================================")
print("             MATHEMATICS LEARNING TOOL            ")
print("==================================================")

while True:
    print("\nSelect an operation:")
    print("1. Calculate Factorial")
    print("2. Generate Fibonacci Series")
    print("3. Exit")

    choice = input("\nEnter choice (1-3): ")

    # Choice 1: Calculate Factorial
    if choice == "1":
        n = int(input("Enter a non-negative integer: "))
        if n < 0:
            print("[ERROR] Please enter a non-negative integer (n >= 0).")
        else:
            result = factorial(n)
            print(f"[RESULT] Factorial of {n} ({n}!) = {result}")

    # Choice 2: Generate Fibonacci Series
    elif choice == "2":
        terms = int(input("Enter number of terms to generate: "))
        if terms <= 0:
            print("[ERROR] Please enter a positive number of terms.")
        else:
            series = []
            for i in range(terms):
                series.append(fibonacci(i))
            print(f"[RESULT] Fibonacci series ({terms} terms): {series}")

    # Choice 3: Exit
    elif choice == "3":
        print("Thank you for using the Mathematics Learning Tool. Goodbye!")
        break

    # Invalid Choice
    else:
        print("[ERROR] Invalid choice! Please enter a number between 1 and 3.")