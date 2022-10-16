import sys
from collections import deque
sys.stdin = open("input.txt")

tunnel = [[], [(-1, 0), (1, 0), (0, -1), (0, 1)],
        [(-1, 0), (1, 0)], [(0, -1), (0, 1)],
        [(-1, 0), (0, 1)], [(1, 0), (0, 1)],
        [(1, 0), (0, -1)], [(-1, 0), (0, -1)]]

def bfs(r, c):
    cnt = 1
    visited = [[0 for _ in range(M)] for _ in range(N)]
    q = deque([(r, c)])
    visited[r][c] = 1
    while q:
        cur = q.popleft()
        for di, dj in tunnel[board[cur[0]][cur[1]]]:
            ni, nj = cur[0] + di, cur[1] + dj
            if (0 <= ni < N and 0 <= nj < M and board[ni][nj] and
                visited[ni][nj] == 0 and (-di, -dj) in tunnel[board[ni][nj]]):
                q.append((ni, nj))
                visited[ni][nj] = visited[cur[0]][cur[1]] + 1
                if visited[ni][nj] <= L:
                    cnt += 1
    return cnt

for T in range(int(input())):
    N, M, R, C, L = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{T + 1} {bfs(R, C)}')
