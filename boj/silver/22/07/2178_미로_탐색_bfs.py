# 220711
from collections import deque

n, m =  map(int, input().split())

maze = [[] for _ in range(n)]
for i in range(n):
    tmp = input()
    for j in range(m):
        maze[i].append(int(tmp[j]))

cumul = [[0 for _ in range(m)] for _ in range(n)]
cumul[0][0] = 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

dq = deque()
dq.append((0, 0))
maze[0][0] = 0

while len(dq) > 0:
    cp = dq.popleft()
    for i in range(4):
        nx = cp[0] + dx[i]
        ny = cp[1] + dy[i]
        if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1:
            maze[nx][ny] = 0
            dq.append((nx, ny))
            cumul[nx][ny] = cumul[cp[0]][cp[1]] + 1

print(cumul[n - 1][m - 1])