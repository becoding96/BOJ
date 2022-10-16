import sys
sys.stdin = open("input.txt")

for T in range(int(input())):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    M %= N
    cnt = 0
    while cnt < M:
        cnt += 1
        arr.append(arr.pop(0))
    print(f'#{T + 1} {arr[0]}')
