# 0.13059s
import sys
sys.stdin = open("input.txt")

for T in range(int(input())):
    board = [[0 for _ in range(10)] for _ in range(10)]
    cnt = 0
    for N in range(int(input())):
        sq = tuple(map(int, input().split()))  # 좌표와 색 정보를 sq에 저장
        for i in range(sq[0], sq[2] + 1):  # 행은 sq[0] ~ sq[2]
            for j in range(sq[1], sq[3] + 1):  # 열은 sq[1] ~ sq[3]
                board[i][j] += sq[-1]  # 해당 범위에 색의 값만큼 더해줌

    for i in range(10):  # 3(보라색)인 칸이 몇 개인지 카운트
        for j in range(10):
            if board[i][j] == 3:
                cnt += 1

    print(f'#{T + 1} {cnt}')