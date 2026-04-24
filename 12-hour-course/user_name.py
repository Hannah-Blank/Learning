# validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must no contain digits
user_name = input("Enter your username: ")

if len(user_name)> 12:
    print("Username must be no more than 12 characters.")
elif not user_name.find (" ") == -1:
    print("Username must not contain spaces.")
elif not user_name.isalpha():
    print("Username must not contain digits.")
else:
    print(f"Welcome {user_name}.")