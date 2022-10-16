import sys
sys.stdin = open("input.txt")

'''
진행마다 불필요하게 4방향 다 보는 풀이
가지치기로 시간 단축 후 패스
'''

def dfs(i, j, former_di, former_dj, d_cnt=0, n_history=[]):
    global start_i, start_j, result
    if d_cnt > 4:
        return
    if d_cnt == 4 and i == start_i and j == start_j:
        result = max(len(n_history), result)
    elif d_cnt == 4:                                                         # 마지막으로 방향이 꺾였을 때,
        if (start_i - i) * former_di > 0 and (start_j - j) * former_dj > 0:  # 시작 지점을 바라볼 때만
            ni, nj = i + former_di, j + former_dj                            # 해당 방향으로만(평소처럼 4방향이 아닌) 진행한다.
            if board[ni][nj] not in n_history:
                dfs(ni, nj, former_di, former_dj, d_cnt, n_history + [board[ni][nj]])
    else:
        for di, dj in [(1, 1), (1, -1), (-1, -1), (-1, 1)]:
            ni, nj = i + di, j + dj
            if ni < 0 or ni >= N or nj < 0 or nj >= N or board[ni][nj] in n_history:
                continue
            if former_di != di or former_dj != dj:
                dfs(ni, nj, di, dj, d_cnt + 1, n_history + [board[ni][nj]])
            else:
                dfs(ni, nj, di, dj, d_cnt, n_history + [board[ni][nj]])


for T in range(int(input())):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    result = -1
    for i in range(N):
        for j in range(N):
            if i in (0, N - 1) and j in (0, N - 1):
                continue
            start_i, start_j = i, j
            dfs(i, j, 0, 0)
    print(f'#{T + 1} {result}')
