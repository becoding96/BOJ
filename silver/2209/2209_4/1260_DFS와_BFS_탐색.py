# 220922

import sys
from collections import deque

def dfs(v):
    print(v, end=" ")
    for nv in graph[v]:
        if dfs_visited[nv] == 0:
            dfs_visited[nv] = 1
            dfs(nv)

def bfs(v):
    print(v, end=" ")
    bfs_visited = [0] * (N + 1)
    bfs_visited[v] = 1
    q = deque([v])
    while q:
        cur = q.popleft()
        for nv in graph[cur]:
            if bfs_visited[nv] == 0:
                print(nv, end=" ")
                q.append(nv)
                bfs_visited[nv] = 1

input = sys.stdin.readline
N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[a].sort()
    graph[b].append(a)
    graph[b].sort()

dfs_visited = [0] * (N + 1)
dfs_visited[V] = 1
dfs(V)
print()

bfs(V)