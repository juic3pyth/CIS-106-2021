print("Input the quantity of items")
itemquan = int(input())
if itemquan >= 1000:
    itemprice = 5
else:
    itemprice = 3
extendedprice = itemquan * itemprice
tax = extendedprice * 0.07
total = extendedprice + tax
unitprice = total / itemquan
print("The Quantity is")
print(itemquan)
print("The extended price is")
print(extendedprice)
print("The tax is")
print(tax)
print("The total cost is")
print(total)
print("The Price per unit is")
print(unitprice)
