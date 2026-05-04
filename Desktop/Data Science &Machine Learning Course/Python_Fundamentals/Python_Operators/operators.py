print(10 + 5) # Addition, output: 15
print(10 - 5) # Subtraction, output: 5

sum1 = 100 + 50      # 150 (100 + 50)
sum2 = sum1 + 250    # 400 (150 + 250)
sum3 = sum2 + sum2   # 800 (400 + 400)

print(sum1) # 150
print(sum2) # 400
print(sum3) # 800

##Arithmetic Operators
print(10 * 5) # Multiplication, output: 50
print(10 / 5) # Division, output: 2.0
print(11 // 5) # Floor Division, output: 2(rounds down to the nearest whole number)
print(10 % 5) # Modulus, output: 0
print(10 ** 5) # Exponentiation, output: 100000

##Assignment Operators
x = 10
x += 5 # x = x + 5, output: 15
x -= 3 # x = x - 3, output: 12
x *= 2 # x = x * 2, output: 24
x /= 4 # x = x / 4, output: 6.0

##Comparison Opeators
print(10 == 5) # Equal to, output: False
print(10 != 5) # Not equal to, output: True
print(10 > 5) # Greater than, output: True  
print(10 < 5) # Less than, output: False
print(10 >= 5) # Greater than or equal to, output: True
print(10 <= 5) # Less than or equal to, output: False
#Chaning Comparison Operators
print(10 > 5 > 3) # True, because 10 is greater than 5 and 5 is greater than 3
print(10 > 5 < 3) # False, because 10 is greater than 5 but 5 is not less than 3


##Logical Operators

print(10 > 5 and 5 > 3) # Logical AND, output: True
print(10 > 5 or 5 < 3) # Logical OR, output: True
print(not(10 > 5)) # Logical NOT, output: False

##Identity Operators
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have the same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

#Membership Operators
x = ["apple", "banana"]
print("banana" in x) # returns True because "banana" is present in the list
print("orange" in x) # returns False because "orange" is not present in the list