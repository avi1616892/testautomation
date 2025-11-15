#while_loop

count = 0
while count<10:
    print("The count is:",count)
    count+=1


print("=======number aggregation------")
num = input("Enter a number:")
result = 0
i =1

while i <= int(num):
    result += i
    i += 1

print("The sum is:",result)