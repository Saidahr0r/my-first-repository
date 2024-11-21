# car_0 = {'model':'ferrari', 'color': 'red'}
# print(car_0['model'])
# print(car_0['color'])

# en_uz = {'apple':'olma', 'apricot':'o\'rik', 'banana':'banan'}

# print(en_uz['apple'])

# fruits = {'apple':2, 'banana':2.5, 'pomegranade':3, 'mango':3}

# print(f"The price of mango is {fruits['mango']} euros")

# student_0 = {'name':'saidahror', 'age':24, 'year of birth':2000}
# print(f'The student who is {student_0["name"].title()} is {student_0["age"]} years old and he was born in {student_0["year of birth"]}')

# student_0['year'] = 1
# student_0['faculty'] = 'economy'

# print(student_0['faculty'])

# # we can change value of the element in the dict in following ways. First, we write NAME of dict and then write ELEMENT 
# #  inside of SQUARE BRACKET ([]) and then write EQUAL SIGN (=) and here is last step. We'll give value inside [] after =.

# student_0['name'] = ['stefano']  
# # print(f'The student who is {student_0["name"].title()} is {student_0["age"]} years old and he was born in {student_0["year of birth"]}')
# print(student_0)



# --- Creating empty dictionary for user -----

# student_1 = {}

# student_1['name'] = 'Fabio'
# student_1['age'] = 25
# student_1['year'] = 'freshman'
# print(student_1)


# # ---- Deleting item inside of dict -----
# # we have to write element's name for deleting, not value
# # {'name':'saidahror'}   ---- here are: name is element, saidahror is value


# student_0 = {'name':'saidahror', 'age':24, 'year of birth':2000}

# del student_0['name']
# print(student_0)





# # ---- Writing dictionary in several lines ------


# phones = {
#     'Saidahror':'Iphone 16',
#     'Stefano':'Iphone 15',
#     'Fabio':'Samsung S 24',
#     'Luca':'Huawei',
#     'Sardor':'Xiaomi'
#     }

# print(phones['Luca'], phones['Fabio'])

# phone = phones.get('Mario', 'This dict doesnt exist')
# print(phone)

# print(phones.get('Luca'))








# # -----   Homeworks ------

# # 1.
# father = {'name':'Shohabbos', 'age':48, 'year of birth':1976, 'job':'entrepreneur'}
# print(f"My father's name is {father['name']} and he is {father['age']} years old, he was born in {father['year of birth']}. He works like {father['job']}. He runs his own business")



# # 2. 
# favourite_meals = {
#     'father':'plov',
#     'mother':'shish kebab',
#     'little brother':'pizza',
#     'sister':'shish kebab', 
#     'mine':'samosa'
# }

# print(f"my father's favorite meal is {favourite_meals['father']}\n"
#       f"my mother's favourite meal is {favourite_meals['mother']}\n"
#       f"my sister's favourite meal is {favourite_meals['sister']}\n"
#       f"my litle brother's favourite meal is {favourite_meals['little brother']}\n"
#       f"my favourite meal is {favourite_meals['mine']}")

# for person, meal in favourite_meals.items():
#     print(f"{person}'s favorite meal is {meal}")



# # 3.

# python_dic = {
#     'string':'text',
#     'float':1.0,
#     'integer':1,
#     'lower':'changing text to small',
#     'upper':'changing text to big',
#     'append':'adding another element',
#     'get':'pulling element out from dict',
#     'print':'outcoming result in terminal',
#     'if':'decision-making',
#     'for':'loop'
# }

# user = input("Write python element:  ")

# if user in python_dic:
#     print(f"{user.lower()} - {python_dic[user]}")
# else:
#     print('There isn\'t such elemet')