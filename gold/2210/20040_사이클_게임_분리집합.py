# 221016
import sys; input = sys.stdin.readline


def find(a):
    while a != rep[a]:
        a = rep[a]
    return a


def union(a, b):
    ar = find(a)
    br = find(b)

    if rank[ar] > rank[br]:
        rep[br] = ar
    elif rank[br] > rank[ar]:
        rep[ar] = br
    else:
        rep[br] = ar
        rank[ar] += 1


N, M = map(int, input().split())
rep = list(range(N))
rank = [0] * N
for i in range(M):
    a, b = map(int, input().split())
    if find(a) == find(b):
        print(i + 1)
        break
    union(a, b)
else:
    print(0)
