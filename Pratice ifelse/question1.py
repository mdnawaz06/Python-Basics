#A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
#Ask user for their salary and year of service and print the net bonus amount.

print("Enter salary")
salary = float(input())  # Convert the input to a floating-point number
print("Enter year of service")
yos = int(input())  # Convert the input to an integer

if yos > 5:
    bonus = 0.05 * salary
    print("Bonus is", bonus)
else:
    print("No bonus")
