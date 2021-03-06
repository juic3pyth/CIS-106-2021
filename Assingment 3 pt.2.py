# This program will take the current price of a stock and give you the amount in dollars that you own in that stock. 

print ("Input the current price of a single share of the stock you wish to check")

stockprice= float(input()) 

print ("Input how many shares of that stock you own")

stockquan= float(input()) 

portfolioval= stockquan*stockprice

print ("You Own")
print (portfolioval) 
print ("dollars worth of that stock")
