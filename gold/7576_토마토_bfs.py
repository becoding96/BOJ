# 220721
# deque 사용 필수!
import sys
from collections import deque

dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]

m, n = map(int, input().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

if all(0 not in l for l in board):
    print(0)
    exit()

q = deque()
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            q.append((i, j))
level = 0
while True:
    len_q = len(q)
    for i in range(len_q):
        cur = q.popleft()
        for j in range(4):
            nrow = cur[0] + dy[j]
            ncol = cur[1] + dx[j]
            if 0 <= nrow <= n - 1 and 0 <= ncol <= m - 1 and board[nrow][ncol] == 0:
                board[nrow][ncol] = 1
                q.append((nrow, ncol))
    if len(q) == 0: # while 조건에 넣으면 level 올리고 끝남
        break
    level += 1

for i in range(n):
    if 0 in board[i]:
        print(-1)
        break
else:
    print(level)