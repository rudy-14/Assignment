print("This program takes the current temperature and outputs whether it is hot, warm or cold")
temperature = int(input("What is the current temperature in degree Celcius? "))
if temperature >= 30:
    print("It is hot")
elif temperature >= 15:
    print("It is warm")
else:
    print("It is cold")