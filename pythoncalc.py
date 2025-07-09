import math
num1 = float(input("Enter the first number:"))
operator = input("choose the operator (+, -, *, /,**):")
num2 = float(input("Enter the second number:"))

if operator == "+":
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is {result}")
elif operator == "-":
    result = num1 - num2
    print(f"The difference of {num1} and {num2} is {result}")
elif operator == "*":
    result = num1 * num2
    print(f"{num1} times {num2} is {result}")
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} divided by {num2} is {result}")
    else:
        print(f"Cannot divide by 0")
elif operator == "**":
    result = math.pow(num1, num2)
    print(f"{num1} power {num2} is {result}")
else:
    print(f"Invalid operator")
