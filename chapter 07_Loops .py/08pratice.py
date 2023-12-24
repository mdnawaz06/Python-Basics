# Write a program to greet all the person name storeds in list l1 which starts from S
l1 = ["Harry", "Sham", "Sachin", "Rahul", "Sony", "Saket"]
for item in l1:
    if item.startswith("S"):
        print("Hello " + item)
