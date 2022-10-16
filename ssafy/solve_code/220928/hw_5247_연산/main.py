import sys
sys.stdin = open("input.txt")
from collections import deque


def bfs(n, m):
    visited = [-1] * (1000001)
    visited[n] = 0
    q = deque([n])
    while q:
        cur = q.popleft()
        if cur + 1 == m or cur -1 == m or cur * 2 == m or cur - 10 == m:
            return visited[cur] + 1
        if cur + 1 <= 1000000 and visited[cur + 1] == -1:
            visited[cur + 1] = visited[cur] + 1
            q.append(cur + 1)
        if cur - 1 >= 0 and visited[cur - 1] == -1:
            visited[cur - 1] = visited[cur] + 1
            q.append(cur - 1)
        if cur * 2 <= 1000000 and visited[cur * 2] == -1:
            visited[cur * 2] = visited[cur] + 1
            q.append(cur * 2)
        if cur - 10 >= 0 and visited[cur - 10] == -1:
            visited[cur - 10] = visited[cur] + 1
            q.append(cur - 10)


for T in range(int(input())):
    N, M = map(int, input().split())
    print(f'#{T + 1} {bfs(N, M)}')
