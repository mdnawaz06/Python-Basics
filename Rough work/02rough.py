# Write a program using function to find greatest of three number.


#def maximum(num1, num2, num3):
 #   if(num1>num2):
 #       if(num1>num3):
 #           return num1
 #       else:
#            return num3
#    else:
# #           if(num2>num3):
 #               return num2
 #           else:
  #              return num3

#m = maximum(3,5,234)
#print("The maximum number is ",m)

if year%4==0:
    if year%100==0:
        if year%400==0:
            leap=True
        else:
            leap=False
    else:
        leap=False
else:
    leap=False
                        