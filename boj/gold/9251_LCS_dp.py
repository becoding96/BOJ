# 220813
# 입력 개수가 작아도 readline이 조금 더 빠름
import sys; input = sys.stdin.readline

A = input().rstrip()
B = input().rstrip()
board = [[0 for _ in range(len(A) + 1)] for _ in range(len(B) + 1)]
maxV = 0

for i in range(1, len(B) + 1):
    for j in range(1, len(A) + 1):
        if A[j - 1] == B[i - 1]:
            board[i][j] = board[i - 1][j - 1] + 1
            maxV = board[i][j] if maxV < board[i][j] else maxV
        else:
            board[i][j] = max(board[i - 1][j], board[i][j - 1])

print(maxV)
