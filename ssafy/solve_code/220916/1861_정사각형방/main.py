import sys
sys.stdin = open("input.txt")

def dfs(i, j, double_lst):
    global cnt
    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        ni = i + di
        nj = j + dj
        if 0 <= ni < N and 0 <= nj < N and board[i][j] + 1 == board[ni][nj]:
            dfs(ni, nj, double_lst)
            cnt += 1

for T in range(int(input())):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    max_move = 0
    start = 1
    for i in range(N):
        for j in range(N):
            cnt = 1
            dfs(i, j, board)
            if cnt > max_move:
                max_move = cnt
                start = board[i][j]
            elif cnt == max_move and board[i][j] < start:
                start = board[i][j]
    print(f'#{T + 1} {start} {max_move}')