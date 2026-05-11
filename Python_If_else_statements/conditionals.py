#if statement
a = 20
b = 30
if a > b:
    print('a is greater than b')
else:
    print('b is greater than a')

#check if number is -ve
a = 1
if a < 0:
    print("a is a negative number")
else:
    print(' a is positive number')

#elif statement
a = 1
b = 1
if a > b:
    print('a  is greater than b')
elif a == b:
    print('a is equal to b')

#multiple elif stements
score = 59

if score >= 90:
    print("Grade is A")
elif score >=80:     #stops when it executes the first statement that evaluates to true
    print("Grade is A-")
elif score >= 70:
    print("Grade is B+")
elif score >= 60:
    print("Grade is B")
elif score >= 50:
    print("Grade is B-")
elif score >= 40:
    print("Grade is C+")
elif score >= 30:
    print('grade is C')
else:
    print("Grade is D")

#check if odd or even number

number = 5
if number % 2 ==0:
    print('number is even')
else:
    print('This is an odd number')

name = 'Jonas'
if len(name) == 0:
    print("Name cannot be empty")
else:
    print(f"Welcome, {name} to our meeting")

#Shorthand if statements
a = 10
b = 6
if a > b: print('a is greater than b')

#Shorthand if...else statement
print('a is greater b') if a>b else print('Not greater')

#Assign a value to a variable

p = 200
v = 300
bigger = v if v>p else p
print('the bigger number is', bigger) #this syntax is summarized below:
# variable = value_if_true if condition else value_if_false

#Multiple conditions on one line
a = 400
b = 500
print('A') if a>b else print('B') if b>a else print('none')

#finding the maximum of two numbers

x = 30
y = 40
max_value = x if x>y else y
print("The maximum value is", max_value)

#setting a default value
username = ''
display_name = username if username else "Montana"
print('Welcome', display_name)

#python logical operators
a = 3
b = 4
c = 5
if b > a and a > c: #and operator
    print('both conditions are true')
elif c > b:
    print('c is greater than b')
else:
    print('b is greater than a')

if a > b or c > b:
    print('one condition is true')

if a > b and 