# 220711
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

n, m =  map(int, input().split())

maze = [[] for _ in range(n)]

for i in range(n):
    tmp = input()
    for j in range(m):
        maze[i].append(int(tmp[j]))

cd = [[0 for _ in range(m)] for _ in range(n)]
cd[0][0] = 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

q = []
q.append(Point(0, 0))
maze[0][0] = 0

while len(q) > 0:
    cp = q.pop(0)
    for i in range(4):
        nx = cp.x + dx[i]
        ny = cp.y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1:
            maze[nx][ny] = 0
            q.append(Point(nx, ny))
            cd[nx][ny] = cd[cp.x][cp.y] + 1

print(cd[n - 1][m - 1])