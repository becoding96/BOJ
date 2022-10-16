import sys
sys.stdin = open("input.txt")


def find_set(x):
    while x != rep[x]:
        x = rep[x]
    return x


def union(x, y):
    rep[find_set(y)] = find_set(x)


for T in range(int(input())):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    rep = [i for i in range(N + 1)]
    for i in range(M):
        union(arr[2 * i], arr[2 * i + 1])
    for i in range(1, N + 1):
        rep[i] = find_set(rep[i])
    print(f'#{T + 1} {len(set(rep[1:]))}')
