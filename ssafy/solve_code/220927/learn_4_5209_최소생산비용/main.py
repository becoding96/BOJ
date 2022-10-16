import sys
sys.stdin = open("sample_input.txt")


def perm(k, r, sum=0):
    global result
    if sum >= result:  # 프루닝(가지치기)
        return
    if k == r:
        result = sum
    else:
        for i in range(k, r):
            p[k], p[i] = p[i], p[k]
            perm(k + 1, r, sum + costs[k][p[k]])
            p[k], p[i] = p[i], p[k]


for T in range(int(input())):
    N = int(input())
    costs = [list(map(int, input().split())) for _ in range(N)]
    p = [i for i in range(N)]
    result = 15 * 99
    perm(0, N)
    print(f'#{T + 1} {result}')
