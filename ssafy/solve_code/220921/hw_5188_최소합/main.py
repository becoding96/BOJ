import sys
sys.stdin = open("sample_input.txt")


def move(i, j, s):
    global result
    if i == N - 1 and j == N - 1:
        result = s if s < result else result
    else:
        if i < N - 1:
            move(i + 1, j, s + board[i + 1][j])
        if j < N - 1:
            move(i, j + 1, s + board[i][j + 1])


for T in range(int(input())):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    result = 25 * 13
    move(0, 0, board[0][0])
    print(f'#{T + 1} {result}')
