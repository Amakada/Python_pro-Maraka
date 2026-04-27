#declaring variables in python
x = "My name is Anthony Maraka"
p = 456
print(p)
print(x)

#python variables can change type even afer they have been declared
x= 369
p = 'John'
print(x)
print(p)

#casting in python

D = str(45)

Name = str("Jones")

z = int(300)

r = float(2)
print(D)
print(Name)
print(z)
print(r)

#getting a variable data type in python

print(type(x))
print(type(p))

#Camel Case Notation

myVarName = "Christina"

birthDay = "April 4"

#pascal case notation

MyVarName = "Einstein"

Is_Comp_Wiz = False
is_scientist = True

if MyVarName == "Einstein" and (Is_Comp_Wiz==True or is_scientist==True):
    print("Einstein is a genius")
else:
    print("Invalid")


#snake case notation
_my_var = ["John", 34, ]

my_var_name = "Sir Isaac"

#many Values to Multiple variables

x, y, z = "John", "Jane", "Mitchelle"
print(x)
print(y)
print(z)

stdName, stdId, stdCourse = "Spoiler", 4567, "Machine Learning"
print(stdName)
print(stdId)
print(stdCourse)

print(type(stdName))
print(type(stdId))

#unpacking in python

people = ["John", "Peter", "Andrew", "Simon"]
print(type(people))

J, P, A, S = people

print(people)
print(J)
print(P)
print(A)
print(S)
print(P,',',J,',', A,',', S) #adding spaces

j, p, t = 'i ', 'am ', 'a programmer'
print(j+p+t)

#Assigning one value to more than one variable
n= m= k = "Peterson" #All the three variables will output the same value when we call print the output
print(n)
print(m)
print(k)

print("Hello", "World")

#perfomimg calculations inside the print function
print(45+45)

#Global variables(Variable declared outside a function)
x = "Awesome"

def myFunction():
   print("python is " + x)
myFunction()

#Local variable(Variable declared inside a function)

y = "Splendid!" #global variable

def Compliment():
    y = "Congratulations" #local variable
    print(y, " You have mastered python")
Compliment()

print(y, "I like the way you understand python conceipts")

#Creating a global variable inside a function
y = 10
def globalVarFunc():
    #global y 
    y = "This is a global variable"
    print(y, "That Can be used both inside the function and outside the function")
globalVarFunc()
print(y)

P = "Jefferson"

#print(P)

def Som1():
    global P
    P = "Alison"
    print(P)
Som1()
