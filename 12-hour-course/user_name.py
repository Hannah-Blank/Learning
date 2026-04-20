# validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must no contain digits
user_name = input("Enter your username: ")

if len(user_name)> 12:
    print("Username must be no more than 12 characters.")
elif " " in user_name:
    print("Username must not contain spaces.")
elif any(char.isdigit() for char in user_name):
    print("Username must not contain digits.")
else:
    print("Username is valid.")