print("This is a program that takes the scores of users and output their grade")
score = int(input("Enter your score: "))
def grade(score):
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    elif score >= 60:
        print("D")
    else:
        print("F")
grade(score)