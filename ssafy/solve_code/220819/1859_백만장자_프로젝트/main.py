import sys
sys.stdin = open("input.txt")

# 1118ms
for T in range(int(input())):
    N = int(input())
    price = list(map(int, input().split()))
    result = 0
    maxv = 0
    for i in range(N - 1, -1, -1):
        maxv = price[i] if price[i] > maxv else maxv
        if price[i] < maxv:
            result += maxv - price[i]
    print(f'#{T + 1} {result}')
