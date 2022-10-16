import sys
sys.stdin = open('input.txt')

for _ in range(10):
    T = int(input())
    board = [list(input()) for _ in range(100)]
    result = 1                                                      # 결과 변수
    flag = False                                                    # 회문 문자열을 찾으면 바로 break 하기 위한 변수

    for M in range(100, 1, -1):                                     # 윈도우의 길이(M)를 가장 상위 반복으로 설정 (100 ~ 2)
        for i in range(100):
            for j in range(100 - M + 1):                            # M길이의 윈도우가 이동하는 횟수
                for k in range(M // 2):                             # 행 방향 회문 문자열 판단
                    if board[i][j + k] != board[i][j + M - 1 - k]:
                        break
                else:
                    result = M                                      # 회문 문자열이면 결과에 M 저장
                    flag = True
                    break

                for k in range(M // 2):                             # 열 방향 회문 문자열 판단
                    if board[j + k][i] != board[j + M - 1 - k][i]:
                        break
                else:
                    result = M
                    flag = True
                    break

            if flag:
                break

        if flag:
            break

    print(f'#{T} {result}')