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

employees.update({})