'''
달팽이 모양의 2차원 리스트를 출력하는 것이지만
달팽이 모양으로 이동한다 생각하면서 주석을 달아놓음
'''

# 0.17304s
import sys
from collections import deque

sys.stdin = open("input.txt")

di, dj = [0, 1, 0, -1], [1, 0, -1, 0]  # 달팽이의 방향을 정하기 위한 리스트

for T in range(int(input())):
    N = int(input())

    board = [[0 for _ in range(N)] for _ in range(N)]
    q = deque()  # 달팽이의 현재 위치를 저장하기 위한 큐

    board[0][0] = 1
    q.append((0, 0))  # (0, 0)을 현재 위치로 집어넣음
    d = 0  # di, dj 용 인덱스
    cnt = 1  # 1부터 늘어나는 cnt

    while len(q):  # q에 원소가 있는 동안 시행
        cur = q.popleft()  # q에서 원소 빼냄, 빼낸 원소의 [0]이 행, [1]이 열 인덱스
        ni, nj = cur[0] + di[d], cur[1] + dj[d] # 다음 행(i), 다음 열(j)
        cnt += 1  # 움직일 때마다 늘어남
        
        if (0 <= ni <= N - 1) and (0 <= nj <= N - 1) and (board[ni][nj] == 0):  # 다음 위치가 범위 내에 있고, 갔던 위치가 아닐 때
            board[ni][nj] = cnt  # 다음 위치에 cnt 저장
            q.append((ni, nj))  # q에 다음 위치를 append

        else:  # 벽에 막혔거나, 이미 갔던 위치가 나올 때
            d = (d + 1) % 4  # 방향을 돌리고, 다시 다음 위치를 정함
            ni, nj = cur[0] + di[d], cur[1] + dj[d]
            if (0 <= ni <= N - 1) and (0 <= nj <= N - 1) and (board[ni][nj] == 0):  # 한번 방향을 돌렸는데도 막히면 끝난 것이므로 else 부분은 설정할 필요 없음
                board[ni][nj] = cnt
                q.append((ni, nj))

    print(f'#{T + 1}')
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()