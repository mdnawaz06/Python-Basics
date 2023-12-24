a = int(input("Enter the quantity of the product"))
if(a*100>1000):
    print("cost is:",(a*100)-(0.1*a*100))
else:
    print("cost is:",a*100)