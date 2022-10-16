import sys
sys.stdin = open("input.txt")

# 237ms
for T in range(int(input())):
    N = int(input())
    route = []
    for _ in range(N):
        route.append(tuple(map(int, input().split())))
    P = int(input())
    station = [int(input()) for _ in range(P)]
    result = [0 for _ in range(P)]
    for r in route:
        for i in range(P):
            if r[0] <= station[i] <= r[1]:
                result[i] += 1

    print(f'#{T + 1}', end=" ")
    print(*result)

