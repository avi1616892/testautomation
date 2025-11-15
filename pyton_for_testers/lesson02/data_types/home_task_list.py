#home_task_list

countries = ["Israel","Usa","Russian","Romania","Argentina","Spain"]

print("----1.1----")
print(countries[:3])


print("----1.2----")
country = countries[0]
countries[0] = countries[1]
countries[1] = country
print(countries)

print("----1.3----")
print(countries[::-1])


print("----1.4----")
countries.sort()
print(countries)


print("----1.5----")
countries.pop()
print(countries)
countries.remove(countries[-1])
print(countries)


print("----1.6----")
middle_index = len(countries) // 2
countries.insert(middle_index,"Brazil")
print(countries)



