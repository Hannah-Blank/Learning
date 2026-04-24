# while loop = execute some code WHILE some condition remains true

name = input("Enter your name: ")
age = int(input("Enter your age: "))
food = input("Enter your favorite food (q to quit): ")

while name =="":
    print("You did not enter your name.")
    name = input("Enter your name: ")
print(f"Hello {name}!")

while age < 0:
    print("Age cannot be negative.")
    age = int(input("Enter your age: "))
print(f"You are {age} years old.")

while not food =="q":
    print(f"{food} is a great food!")
    food = input("Enter another food (q to quit): ")
print("Goodbye!")