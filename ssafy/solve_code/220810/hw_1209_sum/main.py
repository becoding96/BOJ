# 0.20480s

import sys

sys.stdin = open("input.txt")

for _ in range(10):
    t = int(input())
    board = [list(map(int, input().split())) for _ in range(100)]
    result = 0

    eleven_to_five = 0  # 11시에서 5시 방향 대각선
    one_to_seven = 0  # 1시에서 7시 방향 대각선
    for i in range(100):
        eleven_to_five += board[i][i]
        one_to_seven += board[i][99 - i]

        horizon = 0  # 수평 방향
        vertical = 0  # 수직 방향
        for j in range(100):
            horizon += board[i][j]
            vertical += board[j][i]

        result = horizon if horizon > result else result
        result = vertical if vertical > result else result

    result = eleven_to_five if eleven_to_five > result else result
    result = one_to_seven if one_to_seven > result else result

    print(f'#{t} {result}')