import sys
sys.stdin = open("input.txt")

for T in range(int(input())):
    N, Q = map(int, input().split())
    arr = [0] * N
    for i in range(1, Q + 1):
        L, R = map(int, input().split())
        for j in range(L - 1, R):
            arr[j] = i
    print(f'#{T + 1}', end=" ")
    print(*arr)