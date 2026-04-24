# indexing = accessing elements of sequence using [] (indexing operator)
#            [start : end : step]

credit_number ="1234 5678 9012 3456"

credit_number[0] # first position

#print(credit_number[:4])
#print(credit_number[5:9])
#print(credit_number[10:14])
#print(credit_number[5:])
#print(credit_number[::4]) # step= 4, start=0, end= len(credit_number)

credit_number = credit_number[::-1]
print(credit_number)
last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")