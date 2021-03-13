print("input your last name")
lastname = input()
print("input how many dependants you have")
dependants = int(input())
print("input your income")
income = float(input())
adgi = income - dependants * 12000
if adgi > 50000:
    taxrate = 0.2
else:
    taxrate = 0.1
incometax = adgi * taxrate
if incometax < 0:
    incometax = 100
print(lastname)
print("Your gross income is")
print(income)
print("your adjusted gross income is")
print(adgi)
print("Your income tax is")
print(incometax)
