# format specifiers = {value:flags} format a value based on what
# flags are inserted

# .(number)f = round to that many decimal places
# :(number) = allocate that many spaces
# :03 = allocate and zeor pad that many spaces
# :< = left align
# :> = right align
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place the sign to the left most position
# :  = insert a space before positive numbers
# :, = use a comma as a thousand separator

price1 = 300000000.14159
price2 = -9870.65
price3 = 1200.34

print(f"Price 1: {price1:,.2f}€")
print(f"Price 2: {price2:^10}€")
print(f"Price 3: {price3:<10}€")