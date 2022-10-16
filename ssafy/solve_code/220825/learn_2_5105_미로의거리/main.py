import sys
sys.stdin = open("input.txt")

def bfs(root):
    visited = [[0 for _ in range(N)] for _ in range(N)]
    queue = []
    visited[root[0]][root[1]] = 0
    queue.append(root)
    while queue:
        cur = queue.pop(0)
        for di, dj in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            ni, nj = cur[0] + di, cur[1] + dj
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
                if board[ni][nj] == 0:
                    queue.append((ni, nj))
                    visited[ni][nj] = visited[cur[0]][cur[1]] + 1
                elif board[ni][nj] == 3:
                    return visited[cur[0]][cur[1]]

    return 0


for T in range(int(input())):
    N = int(input())
    board = [list(map(int, input())) for _ in range(N)]

    sti, stj = -1, -1
    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                sti, stj = i, j
                break

    print(f'#{T + 1} {bfs((sti, stj))}')

