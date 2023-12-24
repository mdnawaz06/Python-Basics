# Write a python function to print multiplication table of a given number.
def multiTable(n):
    for i in range(1,11):
      print(n, 'x', i, '=', n*i)
    
n = 5
p = multiTable(n)
print(p)    