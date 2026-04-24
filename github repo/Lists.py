# A list is a collection of different data types which is ordered and modifiable(mutable). A list can be empty or it may have different data type items.

fruits = ['banana', 'orange', 'mango', 'lemon']                     # list of fruits
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # list of vegetables
animal_products = ['milk', 'meat', 'butter', 'yoghurt']             # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # list of web technologies
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway'] 
lst = ['Asabeneh', 250, True, {'country':'Finland', 'city':'Helsinki'}] # list containing different data types

# Print the lists and its length
#print('Fruits:', fruits)
#print('Number of fruits:', len(fruits))
#print('Vegetables:', vegetables)
#print('Number of vegetables:', len(vegetables))
#print('Animal products:',animal_products)
#print('Number of animal products:', len(animal_products))
#print('Web technologies:', web_techs)
#print('Number of web technologies:', len(web_techs))
#print('Countries:', countries)
#print('Number of countries:', len(countries))
#print('A list containing different data types:', lst[1])

#first_fruit, second_fruit, third_fruit, fourth_fruit = fruits
#print('First fruit:', first_fruit)
#print('Second fruit:', second_fruit)
#print('Third fruit:', third_fruit)
#print('Fourth fruit:', fourth_fruit)

#countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
#gr, fr, bg, sw, *scandic, es = countries
#print(gr) 
#print(fr)
#print(bg)
#print(sw)
#print(scandic)
#print(es)

#fruits.insert(2, 'apple') # insert apple between orange and mango
#print(fruits)           # ['banana', 'orange', 'apple', 'mango', 'lemon']
#fruits.insert(3, 'lime')   # ['banana', 'orange', 'apple', 'lime', 'mango', 'lemon']
#print(fruits)

negative_numbers = [-5,-4,-3,-2,-1]
positive_numbers = [1, 2, 3,4,5]
zero = [0]

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print(negative_numbers)