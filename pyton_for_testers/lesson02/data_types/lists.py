#lists

cars = ["toyota","mazda","subaru"]
cars_empty = []
print(cars)
print(cars_empty)
print(cars[1])
cars[1]="fiat"
print(cars)

num = [1,4,2,5]
print(num[0] + num[3])

print("-------- append --------")
cars.append("mazda")
print(cars)

print("-------- insert --------")
cars.insert(2,"Bugatti")
print(cars)

print("-------- index --------")
print(cars.index("Bugatti"))

print("-------- pop --------")
print(cars.pop()) #pop out the last from the list
print(cars)

print("-------- remove --------")
cars.remove("toyota")
print(cars)

print("-------- sorting --------")
cars.insert(len(cars),"mazda")
cars.insert(0,"toyota")
print(cars)
cars.sort()
print(cars)



