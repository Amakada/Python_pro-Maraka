print("Hello Strings")

#Multiline strings

a = """Lorem ipsum  dolor sit aamet,
 consecteur adipising elit,
sed do euismd tempor incididunt
ut labore et dolore magna aliqua."""


print(a)
print(len(a))  #get the length of a string 

print("tempor" in a) # Checking for a specific phrase in the string

if "dolore" in a:
     print('yes, "dolore" is present in a') # Checking for a specific phrase in the string

print(a[4])    #getting the character at position 4

y = "Anthony"
for i in y:    #looping through a string
    print(i)

#Checking if a certain phrase or character is not present

greet = "Good Morning Sir Anthony"
if "Anthony" not in greet:   
     print("No such character")
else:
     print("Name present")
print("Maraka" not in greet)
print("Anthony" not in greet)

#Slicing Srtrings

p = "I am an encrypted panda"
print(p[18:23]) # Get characters from position 18 to position 23

#Slice from the begining to position 23
print(p[:23])   #Get characters from the start to position 23 

#Get from the first position
print(p[0])    #get the element at the first position

#slice to the end
print(p[0:])  #getthe elements from position 0 to the end

#Negative Indexing

p = "I am an encrypted bee"

print(p[-4:-1])

#Modify Strings

h = "Hello World"
print(h.upper()) #Return a string in uppercase letters

i = "I BELIEVE IN GOD THE FATHER ALMIGHTY"

print(i.lower()) #Prints a string in lowercase letters

k = "        There is no whitespace in this sentence     "
print(k.strip()) #Remove whitespace from a string


#Replacing a string 

x = 'Hello, Python'

x = x.replace('Hello', 'Good Morning') #changes the string Hello to goodmorning
print(x)

g = "God created the universe"

g = g.replace("universe", "Heaven and earth") #Changes the string 'universe' to heaven and earth

print(g)

#Spliting a string

a = "blue,green,yellow"

a = a.split(',') #Splits the string into a list

print(a)

#String Concatenation

a = "Mr. "
b = "encrypted bee"
c = a + b   # Combines a and b to form a sentence
print(c)

#String Formating
age = 28

Intro = f"My name is Anthony Maraka, I am {age} years old" #using f-string

print(Intro)

print(f"I will try it even {1000000} times until success kneels for me")


#Placeholders and Modifiers

"""Placeholders can contain variables, functions, 
operations and modifiers to fomart the string"""

MonthlyPay = 2000

txt = f"My freelancing salary for Data Science is {MonthlyPay} dollars"

print(txt)

allowDaily = 80
txt = f"Daily Allowance is {allowDaily:.2f}"  #display number with 2 decimals
print(txt)

price_Statement = f"The total price is {20 * 1000}"
print(price_Statement)


#Escape characters

Declaration = "Since I love \"Coding\" I will code the whole of my life " 
print(Declaration)

#escape to a new line
quote = "Your Perception of reality is more real than the reality itself \ngiven this fact, is reality really real?"
print(quote)

Declaration = "Since I love \"Coding\" I will code the whole of my life " 
print(Declaration)

#String Methods
txt = "i am an encrypted bee"
print(txt.capitalize()) #Capitalizes the first letter of the string

print(txt.casefold()) #Converts first string to lower case

x = txt.upper()
print(x)
print(x.casefold())

print(x.center(2)) #Returns a centered strig

print(x.count('A')) #Returns the number of times a particular value occurs in a string

print(x.encode()) #Returns an encoded version of the string

print(x.endswith('E')) #Returns true of string ends with the value specified

print(x.expandtabs()) #Expands tab size of the string

print(x.find("A")) #Searches a particular value and returns its position if found 

print(x.format("BEE")) # Formats specified values in a string

print(x.format_map("BEE")) # Formats specified values in a string

print(x.index("C")) #Searches a particular value and returns its position if found 
