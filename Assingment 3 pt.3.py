#This Program will calculate the discounted price of a single item 

print ("Input the price of the item you are purchasing" )

itemprice= float(input()) 

print ("Input the percentage of the discount") 

discountper= float(input()) 

finalprice=(itemprice-(itemprice*(discountper*.01))) 

print ("The Final price of the item is")
print (finalprice)
