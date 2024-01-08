# 221220
import sys; input = sys.stdin.readline
from collections import deque


def bfs():
    while baby_sharks:
        i, j = baby_sharks.popleft()

        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
            ni, nj = i + di, j + dj

            if ni < 0 or ni >= N or nj < 0 or nj >= M or board[ni][nj]:
                continue

            board[ni][nj] = board[i][j] + 1
            baby_sharks.append((ni, nj))


N, M = map(int, input().split())
board = []
baby_sharks = deque()
result = 0

for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(M):
        if tmp[j] == 1:
            baby_sharks.append((i, j))
    board.append(tmp)

bfs()

for i in range(N):
    for j in range(M):
        result = max(board[i][j], result)

print(result - 1)  # 상어 1부터 시작했으므로 1 빼줌
