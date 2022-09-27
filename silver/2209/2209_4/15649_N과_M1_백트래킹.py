# 220921

import sys

def nPr(i, k, r):
    if i == r:
        print(*p)
    else:
        for j in range(k):
            if used[j] == 0:
                used[j] = 1
                p[i] = a[j]
                nPr(i+1, k, r)
                used[j] = 0

N, M = map(int, sys.stdin.readline().split())
a = [i + 1 for i in range(N)]
used = [0] * N
p = [0] * M
nPr(0, N, M)