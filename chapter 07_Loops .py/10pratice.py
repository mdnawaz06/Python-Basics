# write a program to find a given number is prime or not.
num = int(input("Enter the number"))
prime = True
for i in range(2,num):
    if i%num == 0:
        prime=False

if prime:
    print("This number is prime")
else:
    print("This number is not prime")
    