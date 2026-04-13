# Python Calculator

operator = input("Enter an operator (+ - * /): ")
firstn = float(input("Enter the first number: "))
secondn = float(input("Enter the second number: "))

if operator == "+":
    result = firstn + secondn
    print(f"Your result is {result}")
elif operator == "-":
    result = firstn - secondn
    print(f"Your result is {result}")
elif operator == "*":
    result = firstn * secondn
    print(f"Your result is {result}")
elif operator == "/":
    result = firstn / secondn
    print(f"Your result is {result}")