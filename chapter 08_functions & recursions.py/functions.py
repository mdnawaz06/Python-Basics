#def mySum(num1, num2):
#    return num1 + num2
#s = mySum(6,6)
#print(s)

def factorial_recursive(n):
    return n * factorial_recursive(n-1)

f = factorial_recursive(0)
print(f)