import sys
sys.stdin = open("input.txt")

# 219ms
for T in range(int(input())):
    max_l = 0
    board = [[-1 for _ in range(15)] for _ in range(5)]
    result = ''

    for i in range(5):
        line = input()
        for j in range(len(line)):
            board[i][j] = line[j]
        max_l = len(line) if len(line) > max_l else max_l

    for col in range(max_l):
        for row in range(5):
            if board[row][col] != -1:
                result += board[row][col]

    print(f'#{T + 1} {result}')
