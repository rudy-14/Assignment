print("This is a simple calculator program that requires you to enter two nummbers and an operation sign to generate your result")
print("Below are the available operations")
print("1.) Addition (+)")
print("2.) Subtraction (-)")
print("3.) Multiplication (*)")
print("4.) Division (/)")
operation = input("Enter any number corresponding to the operation sign you wanna use: ")
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

def calculator(number1, operation, number2):
    if operation == "1":
        print("The result is: ", number1 + number2)
    elif operation == "2":
        print("The result is: ", number1 - number2)
    elif operation == "3":
        print("The result is: ", number1 * number2)
    elif operation == "4":
        print("The result is: ", number1 / number2)
calculator(number1, operation, number2)