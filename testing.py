i = " "
for i in range(5):
    if i < " ":
        break
else:
    print(f'{i}' + i - 1)


# 5 4 3 2 1

for i in range(5,0,-1):
    for j in range (5,0,-1):
        if j <= i:
            print(i, end =" ")
            i = i - 1
    print()