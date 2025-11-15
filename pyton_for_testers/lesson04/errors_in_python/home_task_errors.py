#home_task_errors

print("-------------------------1---------------------")
def print_message(value):
    try:
        print(2000+value)
    except TypeError:
        print("unsupported operand type(s) for +: 'int' and 'str'")
        print(str(2000) + " " + value)



print_message("OK")

print("-------------------------2---------------------")
try:
    my_list = [1, 2, 0]
    my_list[6] = my_list[0] / my_list[1]
    print(my_list)
except IndexError:
    print("You list's index is out of bound")
except ZeroDivisionError:
    print("You can't divide number by zero")