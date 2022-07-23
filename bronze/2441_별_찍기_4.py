n = int(input())

for i in range(n, 0, -1):
    star = '*' * i
    print(f'{star:>{n}}')