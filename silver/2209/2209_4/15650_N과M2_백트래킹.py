import sys

def combination(arr, r):
    result = []

    if r == 1:
        for i in arr:
            result.append([i])

    elif r > 1:
        for i in range(len(arr) - r + 1):
            for j in combination(arr[i + 1:], r - 1):
                result.append([arr[i]] + j)

    return result

N, M = map(int, sys.stdin.readline().split())
for c in combination([i + 1 for i in range(N)], M):
    print(*c)