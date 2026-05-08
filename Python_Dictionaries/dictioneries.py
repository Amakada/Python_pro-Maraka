my_dict = {
    "name": "Ngong Kuot",
    "nationality": "South Sudanese",
    "year of birth": 1999,
    "skin_color": "dark",
    "Sofware-engineer": True,
    "programming languages": ["python", "java", "Javascript"]
}
print(my_dict)
my_dict["name"] = "Maraka"
my_dict["year of birth"] = 1998
my_dict['nationality'] = "Kenyan"
print(my_dict)

print(my_dict['name'])
print(len(my_dict))
print(type(my_dict))

#Creating a dictionery using the dict() constructor

student_dict = dict(name='john', age=30, courses=['Full stack development', 'Data science'])
print(student_dict) 

print(student_dict["courses"])

#Accessing the dictionery items

d = student_dict["name"]
print(d)
print(student_dict["age"])

print(student_dict.get("name")) #Using get() method to access the value of a key, it returns None if the key does not exist instead of raising an error 
print(student_dict.get("country")) # None, since the key "country" does not exist in the dictionary
print(student_dict.get("age"))
print(student_dict.get(True))

print(student_dict.keys()) # get all the keys in the dictionary

print(student_dict.values()) # get all the values in the dictionary

print(student_dict.items()) # get all the key-value pairs in the dictionary as a list of tuples 

# Adding items to the dictionary

student_details = {
    "name": "Alice",
    "age": 25,
    "city": "New York"  
}

student_details['email'] = 'alice@gmail.com'
student_details['phone'] = '123-456-7890'
student_details['location'] = 'New York'
print(student_details)

print(student_details['email'])

print(student_details.items()) #returned as a list of tuples, where each tuple contains a key-value pair from the dictionary.

#Check if a key exists
student_details = {
    "name": "Alice",
    "age": 25,
    "city": "New York"  
}

student_details['email'] = 'alice@gmail.com'
student_details['phone'] = '123-456-7890'
student_details['course'] = 'Data Science'
student_details['finished'] = False
if 'city' in student_details:
    print('city exists')

print('name' in student_details) # True
print('country' in student_details) # False
print(student_details)

#Change Dictionery items
student_details['finished'] = True
student_details['course'] = 'Full Stack Development'
print(student_details)

#Update() method to change the value of a key
student_details.update({'age': 26, 'course': 'Data Science'})
print(student_details)
student_details.update({'city': 'San Francisco '})
print(student_details)

employees = {
    'name': 'John',
    'role': 'Data scientist',
    'monthly_salary': (500*30*130),
    'is_married': True
}

employees.update({'age':28, 'city':'Chicago ilinois'})

print(employees)

if 'city' in employees:
    print(True)
else:
    print(False)
employees['name'] = 'Anthony Maraka'

print(employees)

#add dictionary items
dict = {
    'type': 'car',
    'model': 'Jeep',
    'year': 2027
}

dict['price'] = 10000000
dict['registered'] = True
dict['owner'] = 'Anthony Maraka'

print(dict)

dict.update({'color':'red', 'interior':'leather biege'}) #update() method
print(dict)

#Removing items from the dictionary

dict.pop('price')
dict.pop('color') #removing using the pop() method
print(dict)

dict.popitem()
print(dict)   # removes the last added item

del dict['type']
print(dict) #del removes the specified key name

del dict # removes the dictionary compleletely

my_dict = {
    'item': 'Jeans',
    'color': 'blue',
    'manufacturer': 'denim',
    'price': '2000'
}

my_dict.clear() #empties the dictionary completely
print(my_dict)

#Loop dictionaries

employees_dict = {
    'name': "Anthony",
    'role': 'Data Analyst',
    'city': 'nairobi',
    'age': 28
}
for k in employees_dict:
    print(k) #prints only the keys of the dictionary

for v in employees_dict:
    print(employees_dict[v]) #prints only the values

places = {
    'name':'Nairobi',
    'country': 'kenya',
    'residents': 'multi-national',
    'safe': True
}
for p in places.keys():
    print(p) #prints the dictionary keys
for p in places.values():
    print(p)  #prints the dictionary values

for k, v in employees_dict.items():
    print(k, v) #prints both keys and values of the dictionary

new_dict = employees_dict.copy()
print(new_dict)
new_dict.update({'employer': 'microsoft', 'is_expert': True})
print(new_dict)
new_dict1 = dict(new_dict) #another way to copy a dictionary
print(new_dict1)

#Nested Dictionaries
my_Employees = {
    'employee1':{
        'name': 'Steve Korocho',
        'age' : 23,
        'role': 'web developer',
        'city': 'chicago illinois',
        'still_employed': True
    },
    'employee2':{
        'name': 'Ahmed Punda',
        'age': 30,
        'role': 'driver',
        'city': 'nairobi',
        'still_employed': True
    },
    'employee3':{
        'name':'James mbane',
        'age':35,
        'role': 'machine learning engineer',
        'city': 'milan',
        'still_employed': True
    }
}

#create dictionaries then nest them in one bigger dictionary

child1 = {
    'name':'ken',
    'age': 11,
    'studying': True
}

child2 = {
    'name':'jane',
    'age':9,
    'studying': True
}
child3={
    'name':'Progenstein',
    'age': 2,
    'studying': False
}

my_Kids = {
    'child1':child1,
    'child2': child2,
    'child3' : child3
}

print(my_Kids)
#access items in nested dictionaries
print(my_Kids['child2']['name'])
print(my_Kids['child3']['studying'])

#loop through a nested dictionary
for x, obj in my_Kids.items():
    print(x)

    for y in obj:
        print(y + ':', obj[y])


for x, obj in my_Employees.items():
    print(x)
    for y in obj:
        print(y + ':', obj[y])


leader1 = {
    'name':'raphael kerio',
    'positon':'member of parliament',
    'term': 2,
    'educated': True
}

leader2 = {
    'name': 'eliud',
    'position': 'member of county assemly',
    'term': 1,
    'educated': True
}

leader3 = {
    'name' : 'Napotikan',
    'position':'governor',
    'term' : 1,
    'educated' : False
}

leaders = {
    'leader1':leader1,
    'leader2':leader2,
    'leader3':leader3,
}
print(leaders)

aspirants_mca = {
    'asp1' : {
        'name': 'eliud emoni',
        'is_in_power': True,
        'projected_terms': 1
    },
    'asp2' : {
        'name':'yemen guy',
        'is_in_power': False,
        'projected_terms': 2
    },
    'asp3' : {
        'name': 'boiz flani',
        'is_in_power': False,
        'projected_terms': None
    }
}

print(aspirants_mca)
for a, objects in aspirants_mca.items():
    print(print(a))
    for b in objects:
        print(b + ':', objects[b])