# 221205
from collections import deque, defaultdict


def bfs(A, B):
    visited = defaultdict(int)
    q = deque([A])
    while q:
        v = q.popleft()
        for nv in [v * 2, int(str(v) + '1')]:
            if nv <= B and (not visited[nv] or visited[v] + 1 < visited[nv]):
                visited[nv] = visited[v] + 1
                q.append(nv)
    if not visited[B]:
        visited[B] = -2
    return visited[B] + 1


A, B = map(int, input().split())
print(bfs(A, B))
