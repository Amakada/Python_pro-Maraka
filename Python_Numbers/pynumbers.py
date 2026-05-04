x = 1 #Integer
print(type(x))

x= 1.5 #floating point number
print(type(x))
y = 12E4
print(y)
print(type(y))

x = 1j #complex number
print(type(x))

x = 3 + 6j
print(x)
print(type(x))

#Converting Data types from one data type to another

a = 56

a = float(a) # converting to a float
print(a)

a = str(a) # converting to a string
print(a)

a = complex(a)
print(a)

#Random Numbers in python

import random
print(random.randrange(1, 10))
