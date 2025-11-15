#home_task_dictionary

family={"First_name" : ["Ziv","Etamar","Loren"], "Number" : [100, 101, 102]}

print("----1.1----")
print(family)

print("----1.2----")
print(len(family))

print("----1.3----")
family["First_name"].append("Noa")
family["Number"].append(103)
print(family)

family["First_name"].insert(-1,"Rona")
family["Number"].insert(-1,104)
print(family)


print("---------Answer_Yoni------")
family = {'Yoni': '054-1234567', 'Moshe': '050-2222222', 'David': '052-7654321', 'Yael': '058-9988776'}

# solution 01
print(family)

# solution 02
print(len(family))

# solution 03
family['Chaim'] = '050-3374643'
print(family)

family.update({'Shalom': '055-5294754'})
print(family)

