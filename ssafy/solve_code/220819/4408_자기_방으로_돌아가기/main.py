import sys
sys.stdin = open("input.txt")

for T in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnts = [0] * 200
    for cur, pur in arr:
        cur = cur // 2 if cur % 2 else (cur - 1) // 2
        pur = pur // 2 if pur % 2 else (pur - 1) // 2

        if pur < cur:
            pur, cur = cur, pur

        for i in range(cur, pur + 1):
            cnts[i] += 1

    print(f'#{T + 1} {max(cnts)}')