#try_except

try:
    year =int(input("Enter your birth year: "))
    income= int(input("Enter your yearly income: "))
    print("Your age is: ",2025-year)
    print("Your income is: ",(year/income)*100)
except ValueError:
    print("You entered invalid value")
except ZeroDivisionError:
    print("income can't be zero!")