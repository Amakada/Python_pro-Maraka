my_set = {'banana', 'cherry', 'apple'}
print(type(my_set)) # <class 'set'>

#Sets do not allow duplicate values
#0 and False are considered the same value in a set, as are 1 and True
my_set = {'banana', 'apple', 'banana', 0, False, 1, True}

print(my_set) # {'banana', 'cherry', 'apple', 0, 1}

print(len(my_set)) # get the length of my set

#Set() constructor can be used to create a set from an iterable (like a list, tuple, or string)
new_set = set(('purple', 'blue', 'green'))
new_set2 = set(('Hello', ))
print(new_set2)
print(len(new_set2 ))

#Accessing items in a set
for color in new_set:
    print(color)

#Check if item exists in a set
for x in my_set:
  if 'cherry' in my_set:
    print("Yes, 'cherry' is in the set.")
else:
   print("No, 'cherry' is not in the set.")

set_elements = {'green', 'yellow', 'red', 'blue'}
if 'blue' not in set_elements:
    print("No, 'blue' is not in the set.")
else:
    print("Yes, 'blue' is in the set.")

print('cherry' not in my_set) # False

print('blue' not in set_elements) # True


#Adding set items
set_elements.add('orange')
print(set_elements) # {'green', 'yellow', 'red', 'blue', 'orange'}

set_elements.add('amber')

set_elements.add('cyan')

print(set_elements) # {'green', 'yellow', 'red', 'blue', 'orange', 'amber', 'cyan'}


#Add sets using update() method

first_set = {'mma', 'tkd', 'boxing'}
second_set = {'karate', 'judo', 'taekwondo'}

first_set.update(second_set)
print(first_set)

second_set.add(20) #Add a single item
second_set.update([30, 40, 50]) #Add a list
second_set.update({'Shuckle', 'Bulbasaur'}) #add another set

print(second_set) # {'karate', 'judo', 'taekwondo', 20, 30, 40, 50, 'Shuckle', 'Bulbasaur'} 

#Remove items in a set using remove() and discard() methods

second_set.remove(20) # removes 20 from the set
print(second_set)   

second_set.discard('Bulbasaur') # removes 'Bulbasaur' from the set
print(second_set)

#Clear the set with the clear() method
first_set.clear()
print(first_set) # set()

unwanted_set = {'apple', 'banana', 'cherry'}
unwanted_set.clear()
print(unwanted_set) # set()

#Deleting the set using the del keyword

pupils = {'Alice', 'Bob', 'Charlie'}
del pupils
#print(pupils) # NameError: name 'pupils' is not defined

#Looping through a set

lup_set = {'lion', 'tiger', 'leopard'}

for animal in lup_set:  #for loop
   print(animal)



another_set = {'teachers', 'soldiers', 'doctors', 'engineers'}
for e in another_set:
   print(e)



a = 0

while a < len(lup_set):
    print(list(lup_set)[a]) #while loop
    a += 1

#Joining sets
# 1. union() and update() methods
set1 = {'apple', 'banana', 'cherry'}
set2 = {'orange', 'kiwi', 'melon'}

set3 = set1.union(set2) # creates a new set that is the union of set1 and set2
print(set3) # {'apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon'}
set3 = set1| set2 # another way to get the union of set1 and set2
print(set3) # {'apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon'}

set4 = set1.copy() # creates a copy of set1
set4.update(set2) # updates set4 with the union of set4 and set2

set5 = {'grape', 'peach', 'plum'}

set6 = set1.union(set2, set4, set5)
print(set6) # {'apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'grape', 'peach', 'plum'}    

#Join a set and a tuple
nums = {1, 2, 3}
more_nums = (4, 5, 6)
nums = nums.union(more_nums)
print(nums) # {1, 2, 3, 4, 5, 6}

nums.update(more_nums)
print(nums) # {1, 2, 3, 4, 5, 6}

x = {1, 2, 3}

y = {'ball', 'cat', 'dog'} 

x.update(y)# update() method does not return a new set, it updates the original set and returns None
print(x)

#Join Multiple sets
first_set = {'mma', 'tkd', 'boxing'}
second_set = {'karate', 'judo', 'taekwondo'}
third_set = {'baseball', 'football', 'hockey'}

joined_sets = first_set.union(second_set, third_set)
print(joined_sets)
print(len(joined_sets))

fourth_set = first_set|second_set|third_set
print(fourth_set)

set1 = {'apple', 'banana', 'cherry'}
set2 = {'google', 'microsoft', 'apple'}
set1.update(set2)
print(set1) # {'apple', 'banana', 'cherry', 'google', 'microsoft'}

#Both Update() and union() methods can be used to join sets, but the update() method modifies the original set, while the union() method creates a new set without modifying the original sets.
#They both exclude duplicate items and can be used to join multiple sets at once. The choice between them depends on whether you want to modify the original set or create a new one.


# 2. intersection() method - keps only the duplicates
setA = {'apple', 'banana', 'cherry'}
setB = {'google', 'microsoft', 'apple'}
setc = setA.intersection(setB) #creates a new setc and store the intersection of the other two sets in it

print(setc) # {'apple'}

games = {'soccer', 'basketball', 'tennis'}
sports = {'soccer', 'baseball', 'hockey'}
common_game = games & sports # another way to get the intersection of games and sports
print(common_game) # {'soccer'}

games.intersection_update(sports) # updates games with the intersection of games and sports without creating a new set
print(games) # {'soccer'}

# 3. difference() method - Keeps the values that are not found in the other set

cars = {'BMW', 'Volvo', 'Ford', 'Lamborghini'}
cars2 = {'BMW', 'Volvo', 'Ford', 'Ferrari', 'Porsche'}

difference_cars = cars.difference(cars2)
print(difference_cars)

diff_cars = cars2.difference(cars)
print(diff_cars)

fruits = {'apple', 'banana', 'cherry', 'orange'}
citrus_fruits = {'lemon', 'lime', 'orange'}
non_cit = fruits - citrus_fruits
print(non_cit) # {'apple', 'banana', 'cherry'}

fruits.difference_update(citrus_fruits) # updates fruits with the difference of fruits and citrus_fruits
print(fruits) # {'apple', 'banana', 'cherry'}

nono = citrus_fruits - fruits
print(nono)

# 4.symmetric_difference() method - Returns values that are in one set and not in another and joins them into a single set

colors = {'red', 'green', 'blue', 'white'}
colors2 = {'red', 'yellow', 'blue', 'black'}
colors3 = colors.symmetric_difference(colors2) # returns a new set with the symmetric difference of colors and colors2
print(colors3) # {'green', 'white', 'yellow', 'black'}

colors3 = colors ^ colors2 # another way to get the symmetric difference of colors and colors2
print(colors3) # {'green', 'white', 'yellow', 'black'}

colors.symmetric_difference_update(colors2) # updates colors with the symmetric difference of colors and colors2
print(colors) # {'green', 'white', 'yellow', 'black'}


#Frozenset - immutable set that cannot be changed after it is created
frozen_set = frozenset({'banana', 'cherry', 'apple', 'Jeep'})
frozen_set2 = frozenset({'Toyota','Lexus', 'Jeep', 'apple'})
print(frozen_set) # frozenset({'banana', 'cherry', 'apple'})
print(type(frozen_set)) # <class 'frozenset'>


frozen_set1 = frozen_set.intersection(frozen_set2)
print(frozen_set1)
frozen_set1 = frozen_set & frozen_set2
print(frozen_set1)

frozen_set3 = frozen_set.difference(frozen_set2)
print(frozen_set3)
frozen_set3 = frozen_set - frozen_set2
print(frozen_set3)

frozen_set4 = frozen_set.symmetric_difference(frozen_set2)
print(frozen_set4)
frozen_set4 = frozen_set ^ frozen_set2
print(frozen_set4)