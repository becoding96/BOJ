# 221013
S1, S2 = input(), input()
N, M = len(S1), len(S2)

board = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

for i in range(N):
    for j in range(M):
        if S1[i] == S2[j]:
            board[i + 1][j + 1] = board[i][j] + 1
        else:
            board[i + 1][j + 1] = max(board[i + 1][j], board[i][j + 1])

result = ""

if board[N][M] != 0:
    i, j = N, M
    while i >= 1 and j >= 1:
        if board[i][j] == board[i - 1][j]:
            i -= 1
        elif board[i][j] == board[i][j - 1]:
            j -= 1
        else:
            result = S1[i - 1] + result
            i -= 1
            j -= 1
    print(board[N][M])
    print(result)
else:
    print(0)
