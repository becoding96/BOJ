# 220827
import sys
from collections import deque

input = sys.stdin.readline
R, C = map(int, input().split())
board = [list(input().rstrip()) for _ in range(R)]
check = [0] * 26
check[ord(board[0][0]) - 65] = 1
result = 0


def dfs(i, j, cnt):
    global result
    result = cnt if cnt > result else result
    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        ni, nj = i + di, j + dj
        if 0 <= ni < R and 0 <= nj < C and check[ord(board[ni][nj]) - 65] == 0:
            check[ord(board[ni][nj]) - 65] = 1
            dfs(ni, nj, cnt + 1)
            check[ord(board[ni][nj]) - 65] = 0


dfs(0, 0, 1)
print(result)
