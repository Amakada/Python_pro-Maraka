# while loops 
i = 0
while i < 6:
    print(i)
    i +=1

obj = 0
my_list = ['grey', 'green', 23, 56, True]
while obj <  len(my_list):
    print(my_list[obj])
    obj +=1

for e in my_list:
    print(e) #for loop


g = 0
while g < 9:
    print(g)
    if g == 6:
        break #breaks the loop at 6
    g +=1
    
t = 0
while t < 0:
    print(t)
    if t == 4:
        continue
    t += 1

#looping through a list
places = ['kakuma', 'lodwar', 'lokichogio', 'nadapal']
RandNums = [34, 56, 78, 34, 45]
mix = [34, 'green', True, 4.50, 'violet']

#For Loops

for p in places:
    print(p)

for r in RandNums:
    print(r)
for x in mix:
    print(x)

#While Loops
p = 0
while p < len(places):
    print(places[p])
    p += 1

r = 0
while r < len(RandNums):
    print(RandNums[r])
    r += 1

x = 0
while x < len(mix):
    print(mix[x])
    x += 1


#looping through a dictionary and nested dictionary
#single dictionary
MyKids = {
    'name': 'Einstein',
    'age': 4,
    'gender': 'male',
    'studying': True
}
   #for loop
for k in MyKids:
    print(MyKids[k]) #prints only value
for k in MyKids:
    print(k) # prints only keys
for j, n in MyKids.items():
    print(j, n)

#nested dictionaries
leaders = {
    'leader1': {
        'name': 'Eliud',
        'position': 'MCA',
        'in_power': True,
        'term_limit': 1
    },
    'leader2': {
        'name':"Napotikan",
        'position': "gov",
        'in_power': True,
        'term_limit': 1
    },
    'leader3': {
        'name': 'Benjamin',
        'position': 'MP',
        'in_power': False,
        'term_limit': 2
    }
}
for i in leaders.items():
    print(i)
print(leaders['leader1']['name'])

for i, obj in leaders.items():
    print(i)
    for y in obj:
        print(y + ':', obj[y])

#create three dictionaries and then nest them in a biger one
std1 = {
    'name': 'James',
    'course': 'Data Science',
    '_Id_': 236477,
    'graduated': False
}
std2 = {
    'name': 'John',
    'course': 'Fullstack',
    '_id_': 376478,
    'graduated': True
}
std3 = {
    'name': 'steve',
    'course': 'Data annotation',
    '_id_': 968695,
    'graduated': True
}

Students = {
    'std1': std1,
    'std2': std2,
    'std3': std3
}
print(Students)
for s in Students.items():
    print(Students['std1']['name'])

for i, obj in Students.items():
    print(i)
    for y in obj:
        print(y + ':', obj[y])
#looping through a set 
my_set = {'blue', 'green', 32, True, 3.5}
for i in my_set:
    print(i)

i = 0
while i < len(my_list):
    print(list(my_set))
    i += 1
    break

#looping through a tuple
my_tuple = ('rat', 'cat', 67, True, 9.7)
for m in my_tuple:
    print(m)

t = 0
while t < len(my_tuple):
    print(my_tuple)
    t += 1
    break

poultry = ['goose', 'chicken', 'ducks', 'quail', 'turkey']
for p in poultry:
    if p == 'ducks':
        break         #exit the loop when p is 'ducks'
        continue
    print(p)


poultry = ['goose', 'chicken', 'ducks', 'quail', 'turkey']
for p in poultry:
    if p == 'quail':
        break
    print(p)


#range()
for i in range(10):
    print(i)

for r in range(3, 12):
    print(r) #start the range from 3 11

for l in range(10, 100, 20):
    print(l)  #range of 100 start at 10 and increment by 20

#else in for loops
for o in range(5, 30, 5):
    if o == 20:
        break
    print(o)
else:
    print('done')

#Nested loops
adj = ['red', 'big', 'tasty']
fruits = ['apple', 'banana', 'cherry']
for x in adj:
    for y in fruits:
        print(x, y)

for i in range(1, 354):
    pass