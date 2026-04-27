print(10 < 5) # False

print(10 > 5) # True

x = 10
y = 5

if x > y:
    print("x is greater than y")
else:
    print("x is not greater than y")

print(bool(x))

#The following values will evaluate to True when converted to a boolean:
print(bool(True))
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

#The following values will evaluate to False when converted to a boolean:
print(bool(False))
print(bool(None))
print(bool(0))#Zero of any numeric type is False
print(bool(0.0))#Zero of any numeric type is False
print(bool("")) #Empty string is False
print(bool(())) #Empty tuple is False
print(bool([]))#Empty list is False
print(bool({}))#Empty dictionary is False

class Person():
    def __len__(self):
        return 0
    
myobj = Person()
print(bool(myobj)) #False, because __len__ returns 0

class Person():
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
object = Person("John", 30, "New York")
object2 = Person("Jane", 25, "Los Angeles")
print(bool(object)) #True, because __len__ is not defined, so it defaults to True
print(bool(object2)) #True, because __len__ is not defined, so it defaults to  true

#Functions Can Return a Boolean

def myFunction():
    return True
print(myFunction()) #True

def myFunc():
    return False
if myFunc():
    print("Yes")
else:
    print("No") #No

#If an object is of  certain data type
x = 200
print(isinstance(x, int)) #True, because x is an integer