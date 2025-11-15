#continue

var = 5
while var>0:
    var-=1
    if var==3:
        continue
    print("current variable value:", var)


print("----------continue_for--------")
for val in "avrham":
    if val == "h":
        continue
    print(val)
print("finished !!!")