#for_loop

fruits = ["Banana","Melon","Water_Melon"]
for fruit in fruits:
    print("Current fruit:",fruit)
print("Good By!")


print("--------index_for-----------")
fruits2 = ["Tomato","Apple","Kiwoe"]
for index in range (len(fruits2)):
    print("Current fruit:",fruits2[index])
print("Good By!")


print("--------forX-----------")
print("Print out  numbers 0,1,2,3,4")
for x in range (5):
    print(x)


print("--------forXRange-----------")
print("Print out  numbers 3,4,5")
for x in range (3,6):
    print(x)


print("--------forXRange+2-----------")
print("Print out  numbers 3,5,7")
for x in range(3,8,2):
    print(x)


print("--------print sum list-----------")
numbers = [2,5,8,7,9,11,2,9,6]
result = 0
for number in numbers:
    result+=number
print("The sum of result is",result)

