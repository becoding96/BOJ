import sys
sys.stdin = open("input.txt")

# 138ms
def check(arr):
    return len(set(arr)) == 9

for T in range(int(input())):
    board = [list(map(int, input().split())) for _ in range(9)]
    rotated_board = list(zip(*board))
    result = 1

    for i in range(9):
        for j in range(9):
            if not (check(board[i]) and check(rotated_board[i])):
                result = 0
                break

            if i % 3 == 0 and j % 3 == 0:
                tmp = board[i][j: j + 3] + board[i + 1][j: j + 3] + board[i + 2][j: j + 3]
                if not check(tmp):
                    result = 0
                    break

        if not result:
            break

    print(f'#{T + 1} {result}')