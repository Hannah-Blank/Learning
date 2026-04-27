# while loop = execute some code WHILE some condition remains true

name = input("Enter your name: ")
while name =="":
    print("You did not enter your name.")
    name = input("Enter your name: ")
print(f"Hello {name}!")

age = int(input("Enter your age: "))
while age < 0:
    print("Age cannot be negative.")
    age = int(input("Enter your age: "))
print(f"You are {age} years old.")

food = input("Enter your favorite food (q to quit): ")
while not food =="q":
    print(f"{food} is a great food!")
    food = input("Enter another food (q to quit): ")
print("Goodbye!")

num = int(input("Enter a number between 1- 10:  "))

while num <1 or num >10:
    print(f"{num} is not valid.")
    num= int(input("Enter a number between 1- 10:  "))
print(f"{num} is a valid number.")