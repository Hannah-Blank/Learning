# logical operators = evaluate multiple conditions (or, and, not)
#                       or = at least one condition must be True
#                       and = both conditions must be True
#                       not = inverts the condition (not False, not True)

temp = int(input("What is the temperature outside? "))
is_raining = False
is_sunny = False

# if temp > 35 or temp<0 or  is_raining:
   # print("Event will be canceled.")
#else:
   # print("Event is scheduled")


if temp >= 28 and is_sunny:
    print("It is hot🪭")
    print("It is sunny")
elif temp <= 0 and is_sunny:
    print("It is cold ❄️")
    print("It is sunny")
elif temp<= 28 and temp>=0 and is_sunny:
    print("It is moderate")
    print("It is sunny")
if temp >= 28 and not is_sunny:
    print("It is hot🪭")
    print("It is cloudy")
elif temp <= 0 and not is_sunny:
    print("It is cold ❄️")
    print("It is cloudy")
elif temp<= 28 and temp>=0 and not is_sunny:
    print("It is moderate")
    print("It is cloudy")