# 220718
# dfs

# 재귀 함수 최대 깊이를 설정해줘야 함 (백준, 파이썬 기본 1000)
import sys
sys.setrecursionlimit(10000) 

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def dfs(y, x, m, n, board):
    board[y][x] = 0
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny <= n - 1 and 0 <= nx <= m - 1 and board[ny][nx] == 1:
            board[ny][nx] = 0
            dfs(ny, nx, m, n, board)

for _ in range(int(input())):
    answer = 0
    m, n, k = map(int, input().split())
    board = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        board[y][x] = 1
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                answer += 1
                dfs(i, j, m, n, board)
    
    print(answer)