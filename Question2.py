number = float(input("Enter a number: "))

checked = number % 2

if checked == 0:
    print(f"{number} is an even number")
elif checked == 1:
    print(f"{number} is an odd number")
else:
    print("You did not enter a whole number")
