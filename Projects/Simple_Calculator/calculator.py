# Simple Calculator in Python
#Combines Variables, type casting, User input, conditionals and basic operators
firstNum = float(input("Enter the first number:"))

secondNum = float(input("Enter the second number:"))

operation = input("Choose the desired Operator: +, -, *, /, %: ")

if operation == "+":
    result = firstNum + secondNum
elif operation == "-":
    result = firstNum - secondNum
elif operation == "*":
    result = firstNum * secondNum
elif operation == "/":
    result = firstNum / secondNum
elif operation == "%":
    result = firstNum % secondNum
else:
    print("Enter a valid operation")
print("Result:", result)