#Functions are reusable blocks of code that get executed when called and perfom a specific task
def my_function():
    print('this is not the first function')
my_function() #calling a function

#Single function to avoid repetition
def fah_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

celcius = fah_to_celsius(100)
print(celcius)

#pass statement for empty functions

def toUppercase():
    pass

def full_Name(first_Name):
    print("My full names are" + ' ' + first_Name + ' ' + "Maraka")

full_Name('Anthony')

def Identity(fname, lname):
    print("my names are" + ' ' + fname + ' ' + lname)
Identity('Anthony', 'Maraka')

#Default parameters
def my_Name(name="Steve"):
    print("Good morning" + ' ' + name)

my_Name('James')
my_Name()
my_Name('Anthny')

def my_function(country = "Norway"):
  print("I am from", country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#Keyword Arguments - Positions of the arguments does not matter when calling the function
def my_KidsFunction(first, second, third):
    print('My eldest daughter is called' + ' ' + first)
    print('My youngest daughter is called' + ' ' + third)

my_KidsFunction(first="Carmilla", second='Einstein', third='Cerylla')

#Positional Arguments-when the function is called the arguments must be in the right order

def myName_Function(first, second) -> None:
    print("My full names are, " + ' ' + first + ' ' + second)

myName_Function('Maraka', 'Anthony') #Changing the positions changes the results

#Combining Positional and Keyword Arguments
def Employee(name, experience, role):
    print(f"My name is {name}, and I have been a {role} for {experience} years")

Employee("Maraka", 10, role="MLOps Engineer")

#Passing different data types
def listFunction(students):
    for student in students:
        print(student)
StudentsList = ['John', 'James', 'Peter', 'Stephen'] #Passing a list item to the function
listFunction(StudentsList)
print(StudentsList)

def employeeDictionary(employee):
    for key, value in employee.items():
        print(key, value)
my_Employee = {
    'name':'John',         #passing a dictionary as an argument to a function
    'role':'Developer',
    'age': 30
}
employeeDictionary(my_Employee)

#def employeesDict(employees):
   # for x, obj in employees:
       # print(x)
        #for y in obj:
         #   print(y + ':', obj[y])
my_Employees = {                  #Passing a nested dictionary to a function
    'first': {
        'name':'Stephen',
        'age':30,
        'role': 'Data Scientist'
    },
    'second':{
        'name':'John',
        'age':29,
        'role':'Developer'
    },
    'third':{
        'name':'Einsten',
        'age': 35,
        'role':'MLOps Engineer'
    }
}

#employeesDict(my_Employees)

#Return Values
"""def calculatorFunction(num1, num2, operator):
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '/':
        result = num1 / num2
    elif operator == '*':
        result = num1 * num2    
    else:
        print("Please enter a valid operation")
    print(result)
num1 = float(input('Please enter a number: '))
num2 = float(input('Enter a second number: '))
operator = input('Enter an operator: ')
calculatorFunction(num1, num2, operator)"""

def multiplier(num1, num2):
    return num1 * num2
result = multiplier(45, 50)
print(result)

name = 'Steve'
role = 'MLOps Engineer'
def emIntro():
    return f'my name is {name} and I am a {role}'
print(emIntro())

#Returning different data types
def fruitsFunction():
    return ['banana', 'orange', 'mango', 'guava'] #returning a list
fruitsList = fruitsFunction()
print(fruitsList)
print(fruitsList[2])
print(fruitsList[0])

def teamsFunction():
    return ('Arsenal', 'Man United', 'Chelsea', 'Bayern Munchen') #tuple
myTeams = teamsFunction()
print(myTeams)
print(myTeams[2])

def my_function():
  return (10, 20)

x, y = my_function()  #unpacking a tuple using the function
print("x:", x)
print("y:", y)

def resultData():
    return (90, 80, 70, 60)
John, James, Peter, Andrew = resultData()
print('John:', John)
print('Andrew:', Andrew)
print('Peter:', Peter)


#Positional-only Arguments

def myFunction(name, age, /):
    print('My name is ', name)

myFunction('James', 20)

def introFunc(name, /):
    print('My name is', name)

introFunc("Teacher Waajiku")

#Keyword-only arguments

def studentInfo(*, name, course):
    print('My name is', name, 'iam learning', course)

studentInfo(name='John', course='Python')

#Combininng keyword only and positional only arguments
def argsCombo(name, course, /, *,  profession):
    print('I am ', name, 'I study', course, 'and I am also a', profession)

argsCombo('Anthony', 'Data Science', profession = 'Developer')

#*args and **kwargs - allows a function to receive an unknown number of arguments
def my_Function(*fruits):
    for fruit in fruits:
        print(fruit)

my_Function('banana', 'orange', 'mango', 'guava')

#Using the *args keyword
def Students(*args):
    print(args)
    print('1st student:', args[0])
    print('2nd student:', args[1])
    print('3rd student:', args[2])

Students("Harry", "Song", "Steve", 'John', 'Peter')

#Combining Regular Parameters with *args
def greetFunction(greeting, *names):
    for name in names:
        print(greeting, name)

greetFunction('Good morning', 'John', 'Peter', 'Stephen')

#Practical examples with args
#Function that calculates the sum of any number values
def sumFuntion(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total
print(sumFuntion(90, 80, 70))
print(sumFuntion(9, 8, 7))

#Finding the maximum value
def findMaxNumber(*numbers):
    if not numbers:
        return None
    max_number = numbers[0]
    for num in numbers:
        if num > max_number:
            max_number = num
    return max_number
print(findMaxNumber(56, 78, 90, 220))

#Arbitrary Keyword arguments (**kwargs)
def keywordArgsFunction(**students):
    for student in students.items():
        print(student)
keywordArgsFunction(name='John', course="Data Science", graduated=True)


def employeeFunction(**Employees):
    for employee in Employees.items():
        print(employee)
employeeFunction(name='John', age=30, role='Developer')