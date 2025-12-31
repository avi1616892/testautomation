#String

c= "Yosi works at \"bank hapoalim\" "
print(c)

print("------------------")
greeting= "hello world"
print(greeting.lower())
print(greeting.upper())
print(len(greeting))

print("------------------")
print(greeting.replace("l","*"))
print(greeting.replace("l","*",1))

print("------------------")
print(greeting)
print(greeting[0])
print(greeting[-1])
print(greeting[2:5])
print(greeting[2:])
print(greeting*2)
print(greeting + " red ")
print(greeting[::2])

print("------------------")
name ="David"
location = "Tel-Aviv"

output="Hello my name is: " + name + " and i live in " + location
print(output)

output="Hello my name is: %s and i live in %s" %(name,location)
print(output)


print("------------------")
print("Alex ", end='')
print("Levy ", end='')
print(11)