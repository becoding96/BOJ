# 220719
# bfs
from collections import deque

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

for _ in range(int(input())):
    m, n, k = map(int, input().split())
    board = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        board[y][x] = 1
    
    answer = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                answer += 1
                dq = deque()
                dq.append((i, j))
                board[i][j] = 0
                while len(dq) > 0:
                    l = len(dq)
                    for _ in range(l):
                        cur = dq.popleft()
                        for d in range(4):
                            ny = cur[0] + dy[d]
                            nx = cur[1] + dx[d]
                            if 0 <= ny <= n - 1 and 0 <= nx <= m - 1 and board[ny][nx] == 1:
                                board[ny][nx] = 0
                                dq.append((ny, nx))

    print(answer)