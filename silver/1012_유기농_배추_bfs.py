# 220719
# bfs
class Point:
    def __init__(self, y, x):
        self.y = y
        self.x = x 

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
                q = []
                q.append(Point(i, j))
                board[i][j] = 0
                while len(q) > 0:
                    lenq = len(q)
                    for _ in range(lenq):
                        cur = q.pop(0)
                        for d in range(4):
                            ny = cur.y + dy[d]
                            nx = cur.x + dx[d]
                            if 0 <= ny <= n - 1 and 0 <= nx <= m - 1 and board[ny][nx] == 1:
                                board[ny][nx] = 0
                                q.append(Point(ny, nx))

    print(answer)