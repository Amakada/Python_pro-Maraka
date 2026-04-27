x = "Anthony" # string(str ) data type

x = 20 #int data type

x = 20.4 #float data type
print(type(x))


x = {"name":"John", "age":20, "is_Rich": True} #a dictionary (dict) data type
print(type(x))


x = {"bananas", "apples", 1000} # a set data type
print(type(x))



x = ["Blue", "green", "Red"] # a list data type
print(type(x))

print(x[1])

y = (["Blue", "green", "Red"])
print(type(y))

y = ("Yellow", "Monday", 678000)
print(type(y)) #tuple data type
print(y[1:3])

x = range(10) #range
print(type(x))
print(x)

for i in x:
    print(i)

x = ({"Bluish", "Greenish", 1000, 369})
print(type(x))

x = True #boolean
x = False
print(type(x))

x = bytearray(8)
print(type(x))

x = memoryview(bytes(10))
print(type(x))

x = None
print(type(x))