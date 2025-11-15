from random import random

file1=open("MyPasswords.txt","w")
file1.write("-------------\n")

for i in  range(10):
    number=random()
    file1.write("Your password is:" +str((i+1)+number) + "\n")
file1.close()

file1 = open("MyPasswords.txt","a")
file1.write("\n-------------\n")
file1.write("The following users can access this file:\n")
users=["Yoni\n","Avi\n","David\n"]
# for user in users:
#     file1.write(str(user)+ "\n")
file1.writelines(users)
file1.close()
