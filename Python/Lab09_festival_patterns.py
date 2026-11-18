# Take input from the user
n = int(input("Enter the number of rows: "))

# Pattern 1: Star Triangle
print("\nPattern 1: Star Triangle")
print("------------------------")
for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()

# Pattern 2: Number Triangle
print("\nPattern 2: Number Triangle")
print("--------------------------")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# Pattern 3: Inverted Star Triangle
print("\nPattern 3: Inverted Star Triangle")
print("---------------------------------")
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

# Pattern 4: Pyramid
print("\nPattern 4: Pyramid")
print("------------------")
for i in range(1, n + 1):
    # Loop to print spaces
    for j in range(n - i):
        print(" ", end="")
    # Loop to print stars
    for k in range(2 * i - 1):
        print("*", end="")
    print()