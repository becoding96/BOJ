# 220908
import sys
from collections import deque

input = sys.stdin.readline
N = int(input().rstrip())
board = [list(input().rstrip()) for _ in range(N)]
check = [[0 for _ in range(N)] for _ in range(N)]       # 색맹x 방문 체크
check_cb = [[0 for _ in range(N)] for _ in range(N)]    # 색맹 방문 체크
cnt = 0                                                 # 색맹x 결과
cnt_cb = 0                                              # 색맹 결과

for i in range(N):
    for j in range(N):
        # 색맹 ==============================================================================
        if (board[i][j] == 'R' or board[i][j] == 'G') and check_cb[i][j] == 0:
            cnt_cb += 1
            check_cb[i][j] = 1
            q = deque([(i, j)])
            while q:
                cur = q.popleft()
                for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    ni, nj = cur[0] + di, cur[1] + dj
                    if 0 <= ni < N and 0 <= nj < N and check_cb[ni][nj] == 0 and (board[ni][nj] == 'R' or board[ni][nj] == 'G'):
                        check_cb[ni][nj] = 1
                        q.append((ni, nj))
        elif check_cb[i][j] == 0:  # board[i][j] == 'B'
            cnt_cb += 1
            check_cb[i][j] = 1
            q = deque([(i, j)])
            while q:
                cur = q.popleft()
                for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    ni, nj = cur[0] + di, cur[1] + dj
                    if 0 <= ni < N and 0 <= nj < N and check_cb[ni][nj] == 0 and board[ni][nj] == 'B':
                        check_cb[ni][nj] = 1
                        q.append((ni, nj))
        # 색맹x =============================================================================
        if check[i][j] == 0:
            c = board[i][j]
            cnt += 1
            check[i][j] = 1
            q = deque([(i, j)])
            while q:
                cur = q.popleft()
                for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    ni, nj = cur[0] + di, cur[1] + dj
                    if 0 <= ni < N and 0 <= nj < N and check[ni][nj] == 0 and board[ni][nj] == c:
                            check[ni][nj] = 1
                            q.append((ni, nj))

print(cnt, cnt_cb)
