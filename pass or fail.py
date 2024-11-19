print("""This is a program that check if the users pass a test or not
 It takes input from 0 to 100. If the score is 50 and above, it outputs pass else, it outputs fail""")
score = int(input("Enter your score: "))
if  score > 100:
    print("Error, score cannot be more than 100")
elif score >= 50: 
    print("Pass")
else:
    print("Fail")
