import sys
sys.stdin = open("input.txt")

for T in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    l = len(arr)
    for i in range(l - 1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(f'#{T + 1}', end=" ")
    print(*arr)