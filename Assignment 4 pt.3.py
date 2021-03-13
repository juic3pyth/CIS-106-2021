print("input the price of a single book")
price = float(input())
print("input the number of books")
numofbook = int(input())
ordertotal = numofbook * price
if ordertotal <= 50:
    shipping = 0
else:
    shipping = 25
print("The total cost of the order with shipping is")
print(ordertotal + shipping)
print("the cost of the order without shipping is")
print(ordertotal)
print("the cost of shipping is")
print(shipping)
