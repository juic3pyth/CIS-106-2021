# This program will take the inputs from two exam scores and calculate the weighted grades 


print ("Enter your first exam score ")
grade1=float(input())

print ("Enter your second exam score") 
grade2= float(input())

weight1= 0.60
weight2= 0.40 
 
scoretotal= (grade1*weight1)+(grade2*weight2)

print ("Your Total Weighted Score is")
print (scoretotal)
