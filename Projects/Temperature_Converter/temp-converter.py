# Uses number types, conversion formulas, conditionals, formatted output
temp = float(input("Enter temperature: "))
choice = input("Convert to F or C? (Enter F or C): ")

if choice.upper() == "F":
    result = (temp * 9/5) + 32
    print(f"{temp}°C = {result:.2f}°F")
else:
    result = (temp - 32) * 5/9
    print(f"{temp}°F = {result:.2f}°C")


temp = float(input("Enter the temperature:"))
choice = input("Convert to Celcius or Fahrenheit? (Enter F or C):")

if choice.upper() == "F":
    result = (temp * 9/5) + 32
    print(f"{temp}C = {result:.2f}F")
else:
    result = (temp - 32) * 5/9
    print(f"{temp}F = {result:2f}C")