# temperature converting programm

unit = input("Enter the unit of your current temperature (C/F): ")
temperature = float(input("Enter your temperature: "))

if unit == "C":
    result = temperature * 1.8 + 32
    print(f"Your temperature in Fahrenheit is {round(result, 2)} °F")
elif unit == "F":
    result = (temperature - 32) / 1.8
    print(f"Your temperature in Celsius is {round(result, 2)} °C")
elif unit == "" :
    print("You didn't type in a unit")
else: 
    print("You didn't type in a functioning unit")