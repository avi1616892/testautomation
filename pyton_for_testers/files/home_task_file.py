file = 'abc.txt'

def write_file(file_name):
    my_file = open(file_name, "w")
    my_file.write("Python Exercises\n")
    my_file.write("Java Exercises")
    my_file.close()


write_file(file)


def file_read(file_name):
    with open(file_name, "r") as my_file:
        data = my_file.read()
        print(data)


file_read(file)
