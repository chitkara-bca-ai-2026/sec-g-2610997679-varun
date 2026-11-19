print("Input:")
username = input("Username: ")
password = input("Password: ")
print()

print("Enter your username: Enter your password:")
print("----------------------------------------")
print("PASSWORD VALIDATION REPORT")
print("----------------------------------------")
print("Username:", username)
print("Password:", "*" * len(password))
print()

print("--- Validation Rules ---")

# Rule 1: Minimum 8 characters
if len(password) >= 8:
    rule1 = "[PASS] Minimum 8 characters (10 characters)"
    r1_valid = True
else:
    rule1 = "[FAIL] Minimum 8 characters (10 characters)"
    r1_valid = False

# Rule 2: At least one digit
has_digit = False
for char in password:
    if char.isdigit():
        has_digit = True
        break

if has_digit:
    rule2 = "[PASS] At least one digit"
    r2_valid = True
else:
    rule2 = "[FAIL] At least one digit"
    r2_valid = False

# Rule 3: At least one uppercase letter
has_upper = False
for char in password:
    if char.isupper():
        has_upper = True
        break

if has_upper:
    rule3 = "[PASS] At least one uppercase letter"
    r3_valid = True
else:
    rule3 = "[FAIL] At least one uppercase letter"
    r3_valid = False

print(rule1)
print(rule2)  
print(rule3)
print()

print("--- Result ---")
if r1_valid and r2_valid and r3_valid:
    print("Password is VALID!")
    print(f"Account created successfully for {username}!")
else:
    print("Password is INVALID")

print("========================================")


