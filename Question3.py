score = int(input("Enter the score (0-100): "))

# Determine the grade and prints the grade
if 90 <= score <= 100:
    print(f"The grade for the score {score} is: A")
elif 80 <= score < 90:
    print(f"The grade for the score {score} is: B")
elif 70 <= score < 80:
    print(f"The grade for the score {score} is: C")
elif 60 <= score < 70:
    print(f"The grade for the score {score} is: D")
elif 0 <= score < 60:
    print(f"The grade for the score {score} is: F")
else:
    print(f"The score {score} You have Entered is Invalid")


