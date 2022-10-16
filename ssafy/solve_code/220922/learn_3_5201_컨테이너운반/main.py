import sys
sys.stdin = open("input.txt")


for T in range(int(input())):
    N, M = map(int, input().split())
    container = sorted(list(map(int, input().split())), reverse=True)
    used = [0] * N
    truck = list(map(int, input().split()))
    result = 0
    for t in truck:
        for i, w in enumerate(container):
            if t >= w and used[i] == 0:
                result += w
                used[i] = 1
                break
    print(f'#{T + 1} {result}')
