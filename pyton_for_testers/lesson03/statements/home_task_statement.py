#home_task_statement

print("-----------exercise_1----------")
x = float(input("Enter a number: "))
y = float(input("Enter a number: "))

if x>y:
    print(x)
elif y>x:
    print(y)
else:
    print(x+y)


print("-----------exercise_2----------")
list_numbers = [2,5,9]
if list_numbers[0]>list_numbers[1]:
    print("First One is Bigger")
elif list_numbers[0]<list_numbers[1]:
    print("Second One is Bigger")
else:
    print("Both are Equal")


print("-----------exercise_3.1----------")
for num in range (1,11):
    print(num, end=' ')
print()


print("-----------exercise_3.2----------")
count = 1
while count<=10:
    print(count, end=' ')
    count+=1
print()


print("-----------exercise_3.3----------")
for num in range (30,51):
    if num % 2==0:
       print(num, end=' ')
print()


print("-----------exercise_3.4----------")
for num in range (20,41):
    if num % 2!=0:
       print(num, end=' ')
print()


print("-----------exercise_4.1----------")
countries = ["Austria", "Germany", "Canada", "Peru", "Israel"]
for country in countries:
    print(country, end=' ')
print()


print("-----------exercise_4.2----------")
countries = ["Austria", "Germany", "Canada", "Peru", "Israel"]
for country in countries:
    if country=="Israel":
        print(country)
print()


print("-----------exercise_4.3----------")
countries = ["Austria", "Germany", "Canada", "Peru", "Israel"]
if countries[2]=="China":
    print("Yes, it is there")
else:
    print("No, Sorry…")


print("-----------exercise_4.4----------")
countries = ["Austria", "Germany", "Canada", "Peru", "Israel"]
print(len(countries[0]))


print("-----------exercise_5----------")
num = int(input("Enter a number: "))

match num:
    case num if 0 <= num <= 6:
        print("Go to Kindergarten")
    case num if 7 <= num <= 18:
        print("Go to School")
    case num if 19 <= num <= 67:
        print("Go to Work")
    case num if 68 <= num <= 120:
        print("Collecting Pension")
    case _:
        print("Wrong number")

print("-----------exercise_6----------")
job = input("Enter a job: ").lower()

if job == "teacher":
    print("Salary job:", 5000)
elif job == "bank teller":
    print("Salary job:", 10000)
elif job == "qa":
    print("Salary job:", 15000)
elif job == "average salary":
    print("Salary job:", 9100)
else:
    print("You entered wrong job from list")


print("-----------exercise_7----------")
names = {12345: 'Yoni', 45678: 'Moshe', 54321: 'David'}

#way_1
for name in names.keys():
    print("ID:", name)
for name in names.values():
    print("Name:", name)

#way_2
for id, name in names.items():
    print("ID:", id, "| Name:", name)


print("-----------exercise_8----------")
numbers = [3,5,15,18,20,30]
for number in numbers:
    if number%3==0 and number%5==0:
        print(number)
print()


print("-----------exercise_9----------")
word = ['o', 'l', 'l', 'e', 'h']
while len(word) > 0:
    print(word.pop(), end='')
print()


print("-----------exercise_10.1----------")
numbers = [15, 2, 36, 20, 7]
if numbers[0] > numbers[1]:
    if numbers[0] > numbers[2]:
        print(numbers[0])
    else:
        print(numbers[2])
else:
    if numbers[1] > numbers[2]:
        print(numbers[1])
    else:
        print(numbers[2])


print("-----------exercise_10.2----------")
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print("The maximum value of the list:", max)


print("-----------exercise_10.3----------")
sum = 0
for number in numbers:
    sum += number
print("The sum of elements in the list:", sum)


print("-----------exercise_11----------")
num = int(input("Enter a number: "))
is_prime = True
for i in range(2, int(num/2)+1):
    if num % i == 0:
        is_prime = False
        break
if is_prime:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")


