# 221221
import sys, pprint; input = sys.stdin.readline
from collections import deque


def bfs():
    while viruses:
        virus, i, j = viruses.popleft()

        if board[i][j][1] == S:  # S초 이후로는 볼 필요없음
            break

        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = i + di, j + dj

            if ni < 0 or ni == N or nj < 0 or nj == N:
                continue
            
            if board[ni][nj][0] == 0:  # 아직 바이러스가 퍼지지 않은 곳이라면
                board[ni][nj] = (board[i][j][0], board[i][j][1] + 1)
                viruses.append((virus, ni, nj))


N, K = map(int, input().split())
board = []
viruses = []

for i in range(N):
    tmp = list(map(lambda x: (int(x), 0), input().split()))  # (바이러스 번호, 시간)
    for j in range(N):
        if tmp[j][0] != 0:
            viruses.append((tmp[j][0], i, j))
    board.append(tmp)

viruses = deque(sorted(viruses))

S, X, Y = map(int, input().split())

bfs()

print(board[X - 1][Y - 1][0])
