def recurSum(n):
    if n <= 1:
        return n
    return n + recurSum(n - 1)
  
# Driver code
n = 12 
print(recurSum(n))