# Multpiles of 3 or 5 
#If we list all the natural numbers below 10 that are multiples of 3
#or 5, we get 3,5,6,and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
i = 1
summe_dreier = 0
for i in range(334):
    product = i * 3
    summe_dreier += product
    print(product)

t = 1
summe_fünfer = 0
for t in range(200):
    product2 = t * 5
    summe_fünfer += product2
    print(product2)

x = 1
summe_15 = 0 
for x in range(67):
    product3 = x * 15
    summe_15 += product3
    print(product3)

print (summe_dreier + summe_fünfer - summe_15)