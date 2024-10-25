# Getting the lengths of the three sides
First_side = float(input("Enter the length of the first side: "))
Second_side = float(input("Enter the length of the second side: "))
Third_Side = float(input("Enter the length of the third side: "))

# Checking for Equality of all sides
if First_side == Second_side == Third_Side:
    print("The triangle is Equilateral.")
# Checking for Equality of two sides
elif First_side == Second_side or First_side == Third_Side or Second_side == Third_Side:
    print("The triangle is Isosceles.")
else:
    print("The triangle is Scalene.")
