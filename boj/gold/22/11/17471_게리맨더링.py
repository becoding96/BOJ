# 221102
import sys; input = sys.stdin.readline
from collections import deque


def islinked(lst):
    visited = [0] * (N + 1)
    visited[list(lst)[0]] = 1
    q = deque([list(lst)[0]])
    while q:
        v = q.popleft()
        for nv in graph[v]:
            if not visited[nv] and nv in lst:
                visited[nv] = 1
                q.append(nv)
    for e in lst:
        if not visited[e]:
            return False
    else:
        return True


def comb(n, r):
    global result
    if r == 0:
        if islinked(c) and islinked(set(areas) - set(c)):
            comb_sum = 0
            for i in c:
                comb_sum += population[i - 1]
            diff = abs(comb_sum - (population_sum - comb_sum))
            result = min(diff, result)
    elif n < r:
        return
    else:
        c[r - 1] = areas[n - 1]
        comb(n - 1, r - 1)
        comb(n - 1, r)


N = int(input().rstrip())
population = list(map(int, input().split()))
graph = {i:[] for i in range(N + 1)}
for i in range(1, N + 1):
    near_len, *nears = map(int, input().split())
    graph[i] = nears

areas = list(range(1, N + 1))
population_sum = sum(population)
result = population_sum
for r in range(1, N // 2 + 1):
    c = [0] * r
    comb(N, r)

if result == population_sum:
    result = -1

print(result)
