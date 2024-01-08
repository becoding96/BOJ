# 220927
import sys
from collections import deque


def bfs(v):
    visited = [100] * (N + 1)
    q = deque([v])
    visited[v] = 0
    while q:
        cur = q.popleft()
        for nv in linked[cur]:
            if visited[nv] == 100:
                visited[nv] = min(visited[cur] + 1, visited[nv])
                q.append(nv)
    return sum(visited) - 100


input = sys.stdin.readline
N, M = map(int, input().split())
linked = {i + 1: [] for i in range(N)}
cnt = [0] * (N + 1) 
for _ in range(M):
    A, B = map(int, input().split())
    linked[A].append(B)
    linked[B].append(A)
min_bacon = 100
result = 0

for i in range(N, 0, -1):
    bacon = bfs(i)
    if bacon <= min_bacon:
        min_bacon = bacon
        result = i

print(result)
