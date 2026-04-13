import math

a = float(input("Enter length of side a: "))
b = float(input("Enter length of side b: "))

c= round(math.sqrt(pow(a, 2) + pow(b, 2)), 2)

print(f"The hypothenuse of your triangle is {c}cm long")