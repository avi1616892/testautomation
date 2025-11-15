#home_task_functions

print("------------------------1-------------------------")
def revers(string):
    revers_string =string[::-1]
    print(revers_string)

revers("1234abcd")


print("---------------------2----------------------------")
def numbers(number1, number2, number3):
    max_num = number1
    if number2 > max_num:
        max_num = number2
    if number3 > max_num:
        max_num = number3
    return max_num

result= numbers(1,3,2)
print("The max number is:",result)


print("-----------------------3--------------------------")
def distinc(*args):
    result2 = []
    for num in args:
        if num not in result2:
            result2.append(num)
    return result2

print(distinc(1, 1, 2, 2, 3, 3, 4, 4))


print("-----------------------4--------------------------")
def number_assembly(num):
    if not isinstance(num, int):  # בודק אם num הוא לא int
        print("Please enter an integer number only")
        return None

    if num < 0:
        print("Number is negative, enter a positive number")
        return None

    sum_of_numbers = 1
    while num > 1:
        sum_of_numbers *= num
        num -= 1
    return sum_of_numbers


result4 = number_assembly(5)
print(result4)

