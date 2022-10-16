import sys
sys.stdin = open("input.txt")
from collections import deque


def bfs(i=0, j=0):
    global result
    visited = [[-1 for _ in range(N)] for _ in range(N)]
    visited[i][j] = 0
    q = deque([(i, j)])
    while q:
        ci, cj = q.popleft()
        for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            ni, nj = ci + di, cj + dj
            if ni < 0 or ni >= N or nj < 0 or nj >= N:
                continue
            dis = ground[ni][nj] - ground[ci][cj]
            dis = 0 if dis < 0 else dis
            compare = visited[ci][cj] + 1 + dis
            if visited[ni][nj] == -1 or compare < visited[ni][nj]:
                visited[ni][nj] = compare
                q.append((ni, nj))
    return visited[N - 1][N - 1]


for T in range(int(input())):
    N = int(input())
    ground = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{T + 1} {bfs()}')
