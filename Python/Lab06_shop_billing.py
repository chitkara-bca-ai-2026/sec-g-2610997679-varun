print("========================================")
print("       CLOTHING STORE BILLING SYSTEM")
print("========================================")

# Taking inputs from customer
customername = input("Enter Customer Name: ")
garmentname = input("Enter Garment Name: ")
price = float(input("Enter Price of one garment: "))
quantity = int(input("Enter Number of Garments: "))

# Calculating total cost
totalamount = price * quantity

# Displaying the final bill
print("========================================")
print("                 BILL")
print("========================================")
print("Customer Name :", customername)
print("Garment Name  :", garmentname)
print("Price per Unit : Rs.", price)
print("Quantity      :", quantity)
print("Total Amount  : Rs.", totalamount)
print("========================================")

