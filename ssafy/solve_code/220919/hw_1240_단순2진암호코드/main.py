import sys
sys.stdin = open("input.txt")

password = {'0001101':0, '0011001':1, '0010011':2,
            '0111101':3, '0100011':4, '0110001':5,
            '0101111':6, '0111011':7, '0110111':8,
            '0001011':9}

for T in range(int(input())):
    N, M = map(int, input().split())
    board = [list(input()) for _ in range(N)]
    end = [0, 0]  # 유효 코드 부분 오른쪽 위 꼭짓점
    is_correct_password = 0
    result = 0

    for i in range(N):
        for j in range(M):
            if board[i][j] == '1':  # 시간 단축용 if
                if ''.join(board[i][j:j + 5]) == '10000':
                    end = [i, j]
                    break
        if end[1]:  # 찾았다면 j가 0일 수 없으므로
            break

    code = ''.join(board[end[0]][end[1] - 55:end[1] + 1])
    for i in range(8):
        digit = password[code[7 * i: 7 * (i + 1)]]
        result += digit
        if i % 2:
            is_correct_password += digit
        else:
            is_correct_password += digit * 3

    if is_correct_password % 10 == 0:
        print(f'#{T + 1} {result}')
    else:
        print(f'#{T + 1} 0')