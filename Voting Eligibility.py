print("Welcome to the Ghanaian Voting System")
country = input("Which country are you from? ")
country = country.upper()
age = int(input("How old are you? "))
if age >= 18 and country == "GHANA":
    print("You can vote")
else:
    print("You cannot vote")