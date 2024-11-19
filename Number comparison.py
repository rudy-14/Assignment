print("This is a number comparison program. It takes too numbers from the user, compares them and outputs the result")
print("You are required to enter two numbers")
number1 = int(input("Enter your first number: "))
number2 = int(input("Enter your second number: "))

def compare(number1, number2):
    if number1 > number2:
        print("The first number is greater")
    elif number1 < number2:
        print("The second number is greater")
    else:
        print("The numbers are equal")
compare(number1, number2)