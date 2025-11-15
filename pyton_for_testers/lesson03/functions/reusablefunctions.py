#reusablefunctions

numbers = [1,2,3,4,5,6,7,8,9]
print("---Print the only pair numbers without a function---")
for num in numbers:
    if num%2==0:
        print(num)


print("---Print the only NOT pair numbers without a function---")
for num in numbers:
    if num%2!=0:
        print(num)


print("---Print with a function pair and not pair numbers---")
def print_number(is_pair):
    if is_pair:
        for number in  numbers:
            if number%2==0:
                print(number)
    else:
        for number in numbers:
            if number % 2 != 0:
                print(number)


print_number(True)
print("-------------")
print_number(False)