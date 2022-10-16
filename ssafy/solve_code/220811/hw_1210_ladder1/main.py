# 0.18679s
import sys
sys.stdin = open("input.txt")

def ladder(c, board):
    r = 99  # 마지막 행에서 시작
    board[r][c] = 0  # 지나온 부분을 0으로 덮음, 반복문 내에서도 동일

    while r > 0:  # 행이 0보다 큰 동안 반복
        # 왼쪽
        if c - 1 >= 0 and board[r][c - 1]:
            c -= 1
            board[r][c] = 0
        # 오른쪽
        elif c + 1 <= 99 and board[r][c + 1]:
            c += 1
            board[r][c] = 0
        # 위로 한 칸 올라감
        else:
            r -= 1
            board[r][c] = 0

    return c

for _ in range(10):
    T = int(input())
    board = [list(map(int, input().split())) for _ in range(100)]

    for col in range(100):
        if board[99][col] == 2:  # 마지막 행에서 값이 2인 부분을 찾으면 함수 실행
            result = ladder(col, board)

    print(f'#{T} {result}')


