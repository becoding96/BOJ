import sys
sys.stdin = open("input.txt")

def bfs(root):
    visited = [[0 for _ in range(16)] for _ in range(16)]
    visited[root[0]][root[1]] = 1
    q = []
    q.append(root)
    while q:
        cur = q.pop(0)
        for di, dj in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            ni, nj = cur[0] + di, cur[1] + dj
            if 0 <= ni < 16 and 0 <= nj < 16 and visited[ni][nj] == 0:
                if maze[ni][nj] == 0:
                    visited[ni][nj] = 1
                    q.append((ni, nj))
                elif maze[ni][nj] == 3:
                    return 1
    return 0

for _ in range(10):
    T = int(input())
    maze = [list(map(int, input())) for _ in range(16)]

    sti, stj = -1, -1
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                sti, stj = i, j

    print(f'#{T} {bfs((sti, stj))}')
