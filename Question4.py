a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

#operation
operation = input("Enter the operation (+, -, *, /): ")

if operation == "+":
    result = a + b
    print(f"{a} + {b} = {result}")
elif operation == "-":
    result = a - b
    print(f"{a} - {b} = {result}")
elif operation == "*":
    result = a * b
    print(f"{a} * {b} = {result}")
elif operation == "/":
    if b != 0:
        result = a / b
        print(f"{a} / {b} = {result}")
    else:
        print("This is a simple calculater, It cannot divide by zero.")
else:
    print("the operator you entered id invalid. Please enter either +, -, *, or /.")
