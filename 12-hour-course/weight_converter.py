# Python weight converter
import math

weight = float(input("Enter your weight: "))
unit = input("Is it in kg or lbs?: ")

if unit == "kg":
    result1 = weight * 2.20462262
    print("Your weight is", round(result1, 2) , "lbs.")
elif unit == "lbs":
    result = weight / 2.20462262
    print("Your weight is", round(result, 2), "kg.")

