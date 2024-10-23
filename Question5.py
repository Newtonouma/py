a = int(input("Enter your age: "))

if a < 18:
    print("You are a minor.")
elif 18 <= a <= 65:
    print("You are an adult.")
else:
    print("You are a senior.")
