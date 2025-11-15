#if_else

name =input("What is your name?")
if name=="Avi":
    print("Your password" ,len(name) + len(name)**10)
else:
    print("Your password :123456")
print("Welcome")

print("--------verify number-------")
num = float(input("Enter a number:"))
if num>=0:
    if num==0:
        print("zero")
    else:
        print("positive")
else:
    print("negative")