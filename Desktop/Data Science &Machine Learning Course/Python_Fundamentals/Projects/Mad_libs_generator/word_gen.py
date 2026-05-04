#Combine string operations, f-strings, user input, string formating and casting

#get user input and cast it to a string
Name = str(input("Enter a name:"))
Adjective = str(input("Enter an adjective:"))
Noun = str(input("Enter a noun:"))

#Use string formating with the f-string

Story = f"{Name} walked into a {Adjective} {Noun} last Tuesday."
print(Story)