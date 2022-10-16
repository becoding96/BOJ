import sys
sys.stdin = open("input.txt")

# 156ms
for T in range(int(input())):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    for i in range(N):
        h_cnt = 0                           # 가로 방향에서 1이 몇 번 연속해서 나오는지 카운트할 변수, i마다 생김
        h_list = []                         # h_cnt를 append할 리스트
        v_cnt = 0                           # 세로 방향에서 1이 몇 번 연속해서 나오는지 카운트할 변수, i마다 생김
        v_list = []                         # v_cnt를 append할 리스트

        for j in range(N):
            if board[i][j] == 1:            # 가로 방향, 빈칸이 나오면
                h_cnt += 1                      # 카운트 하나 증가
                if j == N - 1:                  # 빈칸이 아니더라도 마지막 칸에 도달하면
                    h_list.append(h_cnt)        # 카운트를 리스트에 append
            else:                           # 빈칸이 아니면
                h_list.append(h_cnt)            # 쌓아오던 카운트를 리스트에 append
                h_cnt = 0                       # 카운트를 다시 0으로 만듦

            if board[j][i] == 1:            # 세로 방향, 빈칸이 나오면
                v_cnt += 1                      # 카운트 하나 증가
                if j == N - 1:                  # 빈칸이 아니더라도 마지막 칸에 도달하면
                    v_list.append(v_cnt)        # 카운트를 리스트에 append
            else:                           # 빈칸이 아니면
                v_list.append(v_cnt)            # 쌓아오던 카운트를 리스트에 append
                v_cnt = 0                       # 카운트를 다시 0으로 만듦

        for x in h_list:                    # 가로 방향 리스트의 원소가
            if x == K:                          # K와 같으면
                result += 1                     # result 값 1 증가

        for x in v_list:                    # 세로 방향 리스트의 원소가
            if x == K:                          # K와 같으면
                result += 1                     # result 값 1 증가

    print(f'#{T + 1} {result}')