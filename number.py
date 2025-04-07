sum = 0

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 * num2 > 1000:
    sum = num1 + num2
    print(sum)
else:
    ("The Multiplication is less than 1000, try another combination of numbers")