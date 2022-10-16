import sys

sys.stdin = open("input.txt")

# 4방향을 탐색하기위한 배열 (델타)
di, dj = [0, 1, 0, -1], [-1, 0, 1, 0]

for t in range(int(input())):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    result = 0

    # 반복문을 돌며 현재 위치에서 4방향을 탐색했을 때
    # board 범위 내에 있을 때만 차이의 절대값을 결과에 더함
    for i in range(n):
        for j in range(n):
            for d in range(4):
                if 0 <= i + di[d] < n and 0 <= j + dj[d] < n:
                    result += abs(board[i][j] - board[i + di[d]][j + dj[d]])

    print(f'#{t + 1} {result}')