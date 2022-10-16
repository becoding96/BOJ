import sys
sys.stdin = open("input.txt")


def prob(s):
    return int(s) / 100


def perm(k, r, multi=1):
    global result
    if multi <= result:
        return
    if k == r:
        result = multi
    else:
        for i in range(k, r):
            p[k], p[i] = p[i], p[k]
            perm(k + 1, r, multi * probability[k][p[k]])
            p[k], p[i] = p[i], p[k]


for T in range(int(input())):
    N = int(input())
    probability = [list(map(prob, input().split())) for _ in range(N)]
    p = [i for i in range(N)]
    result = 0
    perm(0, N)
    print(f'#{T + 1} {round(result * 100, 6):.6f}')
