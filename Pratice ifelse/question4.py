#A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
#Ask user for quantity
#Suppose, one unit will cost 100.
#Judge and print total cost for user.

print("Enter quantity")
quantity = int(input())

if quantity*100 > 1000:
    print("cost is",(quantity*100)-(.1*quantity*100))
else:
    print("Cost is",quantity*100)    