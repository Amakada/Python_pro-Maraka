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
print(this_tuple[-1:-5])