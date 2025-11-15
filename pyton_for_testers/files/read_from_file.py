file1=open("MyPasswords.txt","r")

#way1
print("The content of the file is: \n"+str(file1.read()))


#way2
# print(file1.readline()) #first line
# print(file1.readline())  #second line
# print(file1.readline())  #third line


#way3
# lines=file1.readlines()
# print(lines[4])
# print(lines[10])

file1.close()