import sys
sys.stdin = open("input.txt")

di, dj = [1, 1, -1, -1], [1, -1, -1, 1]


def dfs(i, j, d=0, n_history=[]):
    global start_i, start_j, result
    if d == 3 and i == start_i and j == start_j:
        result = max(len(n_history), result)
    else:
        ni, nj = i + di[d], j + dj[d]
        if ni < 0 or ni >= N or nj < 0 or nj >= N or board[ni][nj] in n_history:
            return
        dfs(ni, nj, d, n_history + [board[ni][nj]])
        if d < 3:
            dfs(ni, nj, d + 1, n_history + [board[ni][nj]])


for T in range(int(input())):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    result = -1
    for i in range(N):
        for j in range(N):
            if i in (0, N - 1) and j in (0, N - 1):
                continue
            start_i, start_j = i, j
            dfs(i, j)
    print(f'#{T + 1} {result}')
