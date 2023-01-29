# 230129
import sys
input = sys.stdin.readline


def dfs(i, j):
    if i == M - 1 and j == N - 1:
        return 1

    # 이미 계산한 값이므로
    if dp[i][j] != -1:
        return dp[i][j]

    dp[i][j] = 0

    for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        ni, nj = i + di, j + dj

        if ni < 0 or nj < 0 or ni >= M or nj >= N:
            continue

        if board[ni][nj] < board[i][j]:
            dp[i][j] += dfs(ni, nj)

    return dp[i][j]


M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1 for _ in range(N)] for _ in range(M)]

print(dfs(0, 0))
