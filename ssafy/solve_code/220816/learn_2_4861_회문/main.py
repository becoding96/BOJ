import sys
sys.stdin = open('input.txt')

# 128ms
for T in range(int(input())):
    N, M = map(int, input().split())
    board = [list(input()) for _ in range(N)]
    flag = False                                # 회문 문자열을 찾으면 바로 break 하기 위한 변수

    for i in range(N):
        for j in range(N - M + 1):              # M길이의 윈도우가 이동하는 횟수
            for k in range(M // 2):             # 행 방향 회문 문자열 판단
                if board[i][j + k] != board[i][j + M - 1 - k]:
                    break
            else:
                result = ''.join(board[i][j: j + M])
                flag = True
                break

            for k in range(M // 2):             # 열 방향 회문 문자열 판단
                if board[j + k][i] != board[j + M - 1 - k][i]:
                    break
            else:
                result = ''
                for m in range(M):
                    result += board[j + m][i]
                flag = True
                break

        if flag:
            break

    print(f'#{T + 1} {result}')