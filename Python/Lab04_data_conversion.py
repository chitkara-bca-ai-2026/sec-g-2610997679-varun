print("-------------------------------------------")
print("               DATA CONVERSION             ")
print("-------------------------------------------")


product = input("Enter Product Name")
price = float(input("Enter Price"))
quantity = int(input("Enter Quantity"))

totalprice = price * quantity

amountstr = str(totalprice)
print("/n-----------------------------------------")
print("              TYPE CASTING                 ")
print("-------------------------------------------")
print("Variable            Value                  ")
print("-------------------------------------------")

print("product   ", product, "      ", type(product))
print("price     ", price, "        ", type(price))
print("quantity  ", quantity, "     ", type(quantity))
print("totalprice", totalprice, "  ", type(totalprice))
print("amountstr ", amountstr, "    ", type(amountstr))

print("/n-----------------------------------------")
print("               TAX INVOICE                 ")
print("-------------------------------------------")

