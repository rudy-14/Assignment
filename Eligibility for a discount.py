print("This program checks the age of a user and outputs whether they're eligible for a discount")
age = int(input("Enter your age: "))
if age < 12 or age > 65:
    print("You're eligible for a discount")
else:
    print("No discount available")