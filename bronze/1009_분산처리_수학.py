# 220721
for _ in range(int(input())):
    a, b = map(int, input().split())
    if a % 10 == 0:
        print(10)
        continue
    a %= 10
    l = []
    tmp = a
    while True:
        one = int(str(tmp)[-1])
        if one in l:
            break
        l.append(one)
        tmp *= a

    print(l[b % len(l) - 1])