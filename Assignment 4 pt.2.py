print("Input which item you want")
item = input()
print("input how many of that item you want")
itemquan = int(input())
if item == "A":
    unitprice = 10
else:
    unitprice = 20
tax = unitprice * itemquan
extendedprice = itemquan * unitprice
print("Extended Price is")
print(extendedprice)
print("item chosen")
print(item)
