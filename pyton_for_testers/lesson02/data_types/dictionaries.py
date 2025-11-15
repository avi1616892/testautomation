#dictionaries

salary = {"Administration" : 8000,"It" : 10000,"Support":11000,"Qa" : 14000,"Automation":18000}
print(type(salary))
print(salary["Qa"])
print(salary.get("Qa")) #another way to fetch data

print("-----list inside dictionary-----")
salary_with_list = {"Support":11000,"Qa" : [14000,10000,12000,8000],"Automation":18000}
print(salary_with_list["Qa"])
print(salary_with_list["Qa"][3])
print(salary_with_list.get("Qa")[3])
print(salary_with_list["Qa"].index(10000))

print("-----dictionary inside dictionary-----")
emp = {"CEO" : "Moshe", "VPRND" : "David", "RND" :{"QA" : "Yoni","DEV": "Chaim"}, "DBS" : "Shlomo" }
print(emp.get("RND").get("QA"))

print("-----add elemnet to dictionary-----")
print(emp)
emp ["Team Leder"] = "Yeal"
print(emp)

print("-----update elemnet in dictionary-----")
print(emp)
emp ["Team Leder"] = "Roni"
print(emp)

print("-----remove elemnet from dictionary-----")
print(emp)
emp.pop("Team Leder")
print(emp)

del emp["VPRND"]
print(emp)