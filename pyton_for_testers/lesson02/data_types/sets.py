#sets

nums_list =[1,2,3,3]
nums_set ={1,2,3,3}
print(nums_list)
print(nums_set)

cars = {"toyota","mazda","fiat"}
print(len(cars))
cars.remove("fiat") #raise an error while not find
print(cars)
cars.discard("fiat") #not raise an error
print(cars)
cars.pop()
print(cars)
cars.clear()
print(cars)

del cars  #delete cars

cars = {"toyota","mazda","fiat"}
print(cars)
cars_new = {"bmw","mercedes","fiat"}
print(cars_new)
cars_full = cars.union(cars_new)
print(cars_full)
print(cars.difference(cars_new))
print(cars_new.difference(cars))

