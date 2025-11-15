#casting_types
from datetime import datetime

a = 2
b = 3
print(a+b)
print("The result is: " + str(a+b))


year = input("Enter your birth year: ")
current_year = datetime.now().year
age = current_year - int(year)
print("Your age is:", age)
