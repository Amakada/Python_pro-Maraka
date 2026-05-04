my_list = ['banana', 'cherry', 'apple']
print(my_list) # ['banana', 'cherry', 'apple']
print(type(my_list)) # <class 'list'>

print(my_list[0]) # 'banana'
print(my_list[1]) # 'cherry'    

print(len(my_list)) # 3

list1 = ["abc", 34, True, 40, "male"]
print(type(list1)) # <class 'list'>


#list() constructor can be used to create a list from an iterable (like a string, tuple, or another list)
my_list = list(("apple", "banana", "cherry"))
print(my_list) # ['apple', 'banana', 'cherry']

#Access List Items
my_list = ["apple", "banana", "cherry"]
print(my_list[0]) # 'apple'
print(my_list[1]) # 'banana'
print(my_list[2]) # 'cherry'

#Negative indexing allows you to access list items from the end of the list
print(my_list[-1]) # 'cherry'
print(my_list[-2]) # 'banana'
print(my_list[-3]) # 'apple'

#Range of Indexes

this_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(this_list[2:5]) # ['cherry', 'orange', 'kiwi
print(this_list[:4]) # ['apple', 'banana', 'cherry', 'orange']
print(this_list[3:]) # ['orange', 'kiwi', 'melon', 'mango']

#The range of Negative indexes
print(this_list[-4:-1]) # ['orange', 'kiwi', 'melon']

#Check if Items exists in a list

cars_List = ["BMW", "Volvo", "Ford"]

if "Lamborghini" in cars_List:
    print("Yes, Lamborghini is in the list of cars.")
else:
    print("No, Lamborghini is not in the list of cars.")


sport_List = ["Soccer", "Basketball", "Tennis"]
if "Soccer" in sport_List:
    print("Yes, Soccer is in the list of sports.")
else:
    print("No, Soccer is not in the list of sports.")  


#Change List Item Value
sports = ['MMA', 'Boxing', 'Soccer', 'Basketball', 'Tennis']
sports[2] = 'Taekwondo'
sports[3] = 'Karate'

print(sports) # ['MMA', 'Boxing', 'Taekwondo', 'Karate', 'Tennis']
sports[4] = 'Judo'
print(sports) # ['MMA', 'Boxing', 'Taekwondo', 'Karate', 'Judo']

#Changina a range of values in a list

sports[0:4] = ['Baseball', 'Football', 'Hockey', 'Golf']
print(sports) # ['Baseball', 'Football', 'Hockey', 'Golf', 'Judo']

sports[0:10] = ['Rugby', 'Cricket', 'Swimming', 'Volleyball', 'Badminton', 'Table Tennis', 'Skiing', 'Snowboarding', 'Skateboarding', 'Surfing']
print(sports) # ['Rugby', 'Cricket', 'Swimming', 'Volleyball', 'Badminton', 'Table Tennis', 'Skiing', 'Snowboarding', 'Skateboarding', 'Surfing']
print(len(sports)) # 10

#insert an item to a list
sports.insert(0, 'MMA')
print(sports) # ['MMA', 'Rugby', 'Cricket', 'Swimming', 'Volleyball', 'Badminton', 'Table Tennis', 'Skiing', 'Snowboarding', 'Skateboarding', 'Surfing']

exercises = ['Push-ups', 'Sit-ups', 'Squats']
exercises.insert(2, 'Lunges')
print(exercises) # ['Push-ups', 'Sit-ups', 'Lunges', '


#Add an item to the list using append()

fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')
print(fruits) # ['apple', 'banana', 'cherry', 'orange']

students = ['Alice', 'Bob', 'Charlie']
students.append('David')
students.insert(0, 'Eve')
print(students) # ['Eve', 'Alice', 'Bob', 'Charlie', 'David']

#Append the elements of a list to another list using extend()

players = ['Andrew', 'Michael', 'Sarah']
players.extend([10, 20, 30])

players.extend(['Jessica', 'David'])
print(players) # ['Andrew', 'Michael', 'Sarah', 'Jessica', 'David'] 

players.extend(students)
print(players) # ['Andrew', 'Michael', 'Sarah', 'Jessica', 'David',

students.extend(players)
print(students) # ['Eve', 'Alice', 'Bob', 'Charlie', 'David', 'Andrew', 'Michael', 'Sarah', 'Jessica', 'David'] 

#Adding the items of a tuple to a list using extend()

Drinks = ['Water', 'Juice', 'Soda'] #list item

alco_drinks = ('Wine', 'Beer', 'Vodka') #Tuple item

Drinks.extend(alco_drinks)

print(Drinks) # ['Water', 'Juice', 'Soda', 'Wine', 'Beer', 'Vodka']

beverages = ['Tea', 'Coffee', 'Milk'] #list item

hot_drinks = {'Hot Chocolate', 'Espresso', 'Latte'} #set item

beverages.extend(hot_drinks)

print(beverages) # ['Tea', 'Coffee', 'Milk', 'Hot Chocolate', 'Espresso', 'Latte']  

pro_Langs = ['python', 'javascript', 'java'] #list item
other_Langs = {'C++', 'Ruby', 'Go'} #set item

pro_Langs.extend(other_Langs)
print(pro_Langs) # ['python', 'javascript', 'java', 'C++', 'Ruby', 'Go']

#Remove an item from a list using remove()

cars = ['BMW', 'Volvo', 'Ford', 'Toyota']
cars.remove('Ford')

print(cars)

#Remove the specified index using pop()

cars.pop(1) # removes 'Volvo' at index 1
print(cars) # ['BMW', 'Toyota']

#Remove an item using the del keyword

del cars[0] # removes 'BMW' at index 0
print(cars) # ['Toyota']  

#Clear the list using clear()

rooms = ['Living Room', 'Kitchen', 'Bedroom', 'Bathroom']
rooms.clear()
print(rooms) # []

#Loop though Lists
colors = ['Red', 'Green', 'Blue']

for c in colors:
    print(c) # Red, Green, Blue

#Loop through the list items by referring to their index number
colors = ['Red', 'Green', 'Blue']
for i in range(len(colors)):
    print(colors[i]) # Red, Green, Blue

animals = ['cows', 'goats', 'sheep', 'donkeys']
for a in range(len(animals)):
    print(animals[a])


#Using a while loop

play_Names = ['codewiz', 'serenade', 'montana', 'ariif', 'amakada']
i = 0
while i < len(play_Names):
    print(play_Names[i])
    i += 1

Tech_Res = ['Hacker', 'Data Scientist', 'Web Developer', 'IT Consultancy']

t = 0
while t < len(Tech_Res):
    print(Tech_Res[t])
    t += 1

#Loop Using list Compression
this_list = ['jay', 'blue', 'green', 'toy', 'tiger']
new_list = []

[print(x.upper()) for x in this_list]


for x in this_list:
    if 'e' in x:
        new_list.append(x)
print(new_list) # ['green', 'tiger']

flies = ['tsetse fly', 'house fly', 'fruit fly', 'blow fly']

new_flies = [f for f in flies if 'b' in f]
print(new_flies)

countries = ['Germany', 'Russia', 'Kenya', 'Uganda']
new_cou = [c for c in countries if 's' in c]
print(new_cou)


poultry = ['Chicken', 'duck', 'goose']
new_Polt = [c for c in poultry if 'g' in c]
print(new_Polt) # ['goose']

New_polt = [t for t in poultry if 'k' in t]
print(New_polt)

new_Polt = [x for x in poultry]
print(new_Polt)

phone_Models = ['iPhone', 'Samsung', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'OnePlus', 'Google Pixel', 'Sony Xperia', 'Nokia']
new_Models = [m for m in phone_Models if 'a' in m]
print(new_Models)

new_Models2 = [m for m in phone_Models if m.startswith('S')]
print(new_Models2)

new_Models3 = [m for m in phone_Models if m != 'Samsung']
print(new_Models3)


#Create an iterable 
iterable = [i for i in range(5)]
print(iterable)

#Sort lists
my_List = ['kales,', 'spinach', 'cabbage', 'lettuce']
my_List.sort()

print(my_List) # ['cabbage', 'kales,', 'lettuce', 'spinach']

my_Numerals = [5, 2, 9, 1, 3]
my_Numerals.sort()
print(my_Numerals) # [1, 2, 3, 5, 9]

#Sort in descending order using reverse=true
my_List = ['kales,', 'spinach', 'cabbage', 'lettuce']
my_List.sort(reverse=True)
print(my_List) # ['spinach', 'lettuce', 'kales,', '


my_Numerals = [5, 2, 9, 1, 3]
my_Numerals.sort(reverse=True)
print(my_Numerals) # [9, 5, 3, 2, 1]

#sort using a function as key

nums = [100, 50, 200, 25, 75, 80, 150, 300, 10, 60]
def my_function(i):
    return abs(i - 60) #Sort numbers according to how close it is to 60
nums.sort(key=my_function)
print(nums)


marks = [50, 60, 70, 80, 99, 77, 45, 59]
def function(n):
    return abs(n-50)
marks.sort(key=function) #Sort according to closeness to 50
print(marks)

Names = ['John', 'Peter', 'John', 'Andrew', 'Samson', 'christine', 'abigael']
Names.sort(key=str.lower) #Remove case sensitivity when sorting
print(Names)

Names.reverse() #Reverse the order of a lst
print(Names)

names = Names.copy() #Copy a list
print(names)

names2 = list(names) #Another way to copy a list
print(names2)

names3 = names[:] #Another way to copy a list
print(names3)

names4 = names3[:] #Another way to copy a list
print(names4)

#Joining Lists

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3) # ['a', 'b', 'c', 1, 2, 3] #Using the + operator to join lists 


list4 = list1.extend(list2) #Using the extend() method to join lists
print(list3) # ['a', 'b', 'c', 1, 2

for x in list2:
    list1.append(x)
    print(list1) # ['a', 'b', 'c', 1, 2, 3] #Using a for loop to append each item of list2 to list1 
    
