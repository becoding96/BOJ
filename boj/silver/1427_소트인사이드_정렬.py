# 220810
num = input()

for i in range(9, -1, -1):
    for j in num:
        if int(j) == i:
            print(i, end='')
