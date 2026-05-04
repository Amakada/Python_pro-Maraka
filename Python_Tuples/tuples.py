fruit_Tup = ('apple', 'banana', 'orange')
print(fruit_Tup) # ('apple', 'banana', 'orange')

print(type(fruit_Tup)) # <class 'tuple'>
#Tuples allow duplicate values
my_tuple = ('steve jobs', 56, True, 3.14, 'alan watts', 56)
print(len(my_tuple)) # print the length of the tuple

#Single value tuple
bool_Tup = (True,)

#Tuple() constructor
my_tuple = tuple(('apple', 'banana', 'cherry'))

#Access tuple items

print(my_tuple[0]) # 'apple'
print(my_tuple[1]) # 'banana'   
print(my_tuple[2]) # 'cherry'

#Negative Indexing
print(my_tuple[-1]) # 'cherry'
print(my_tuple[-2]) # 'banana'
print(my_tuple[-3]) # 'apple'

#Range of indexes
this_tuple = ('apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango')
print(this_tuple[1:4]) # ('banana', 'cherry', 'orange')
print(this_tuple[:4]) # ('apple', 'banana', 'cherry', 'orange')

#Range of Negative Indexes
print(this_tuple[-5:-1])



#k = [m for m in this_tuple if "o" in m]
#print(k)

#for i in this_tuple:
  #  if "banana" in this_tuple:
      #  print("Yes, 'banana' is in the tuple.")
   # else:
      #  print("No, 'banana' is not in the tuple.")


#Check if item exists in a tuple
if 'orange' in this_tuple:
    print(bool(this_tuple))
else:   
    print(bool(this_tuple))



#Change tuple values and add values by converting to a list and vice versa


tuple_example = ('Lamborghini', 'Ferrari', 'Porsche', 'Bugatti', 'McLaren')

#Convert the tuple to a list

cars_List = list(tuple_example)

cars_List[0] = 'Lamborghini Aventador'
cars_List[1] = 'Ferrari F8 Tributo'

cars_List.append(['Landcruiser', 'Range Rover', 'G-Wagon'])

cars_List.insert(2, 'Porsche 911')

cars_List = tuple(cars_List)

print(cars_List)

cars_tuple = ('Bugatti', 'Jeep')

cars_List += cars_tuple

print(len(cars_List))

del cars_tuple

print(cars_List)
print(len(cars_List))



#Unpacking tuples

colors = ('Green', 'Blue', 'Yellow', 'Red')

(Green, Blue, Yellow, Red) = colors

print(Green)
print(colors)

#Using Asterisk * for unpacking fewer values

Plays = ('Soccer', 'basketball', 'Volleybal', 'Drama', 'Hockey')

(Red, Blue, *Green) = Plays

print(Plays)

print(Green)

print(Red)

games = ('Soccer', 'basketball', 'Volleybal', 'Drama', 'Hockey', 'Baseball', 'Football', 'Tennis')

(Stephen, *Michael, John, James) = games

print(Stephen)
print(Michael)  
print(John)
print(James)    

print(games)

#Looping through a tuple
for x in games:
    print(x)

#While loop through a tuple
x = 0
while x < len(games):
    print(games[x])
    x += 1

#Looping through the index numbers
for x in range(len(games)):
    print(games[x])

#Join Tuples

tuple1 = ('John', 'Jane', 'Mitchelle')
tuple2 = ('Smith', 'Doe', 'Johnson')

tuple1 += tuple2
print(tuple1)

#Multiply Tuples
tuple3 = ('Hello',) * 3

print(tuple3)

#Tuple Methods
my_tuple = ('apple', 'banana', 'cherry', 'apple', 'banana')

print(my_tuple.index('banana')) # 1
print(my_tuple.count('apple')) # 2