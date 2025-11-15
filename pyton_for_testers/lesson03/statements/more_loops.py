#more_loop

count = 0
while count<5:
    print(count,"is less than 5")
    count+=1
else:
    print(count,"is  not less than 5")

print("-----------------for else-------------------")
for i in  range (0,5):
    print(i)
else:
    print("finished")


print("-----------------prime numbers-------------------")
number = int(input("Enter a number:"))
for i in range(2,number):
    if number % i == 0:
        print(number,"is not prime number")
        break
else:
    print(number,"is prime number")


