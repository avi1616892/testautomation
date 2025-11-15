#match_case

my_name = input("What is your name? ")
match my_name:
    case "Avi":
        print("Hello " +my_name)
    case "David":
        print("Hello " + my_name)
    case "Roei":
        print("Hello " + my_name)
    case "Misael":
        print("Hello " + my_name)
    case _:
        print("Wrong name")
