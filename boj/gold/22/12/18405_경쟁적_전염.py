# 221221
import sys; input = sys.stdin.readline
from collections import deque


def bfs():
    while viruses:
        i, j = viruses.popleft()

        if board[i][j][1] == S:  # S초 이후로는 볼 필요없음
            continue

        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = i + di, j + dj

            if ni < 0 or ni >= N or nj < 0 or nj >= N:
                continue
            
            if board[ni][nj][0] == 0:  # 아직 바이러스가 퍼지지 않은 곳이라면
                board[ni][nj] = (board[i][j][0], board[i][j][1] + 1)
                viruses.append((ni, nj))
            # 같은 시간대라면, 번호 낮은 바이러스 우선
            elif board[i][j][1] + 1 == board[ni][nj][1] and board[i][j][0] < board[ni][nj][0]:
                board[ni][nj] = (board[i][j][0], board[i][j][1] + 1)
                viruses.append((ni, nj))


N, K = map(int, input().split())
board = []
viruses = deque()

for i in range(N):
    tmp = list(map(lambda x: (int(x), 0), input().split()))  # (바이러스 번호, 시간)
    for j in range(N):
        if tmp[j][0] != 0:
            viruses.append((i, j))
    board.append(tmp)

S, X, Y = map(int, input().split())

bfs()

print(board[X - 1][Y - 1][0])