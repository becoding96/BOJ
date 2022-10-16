import sys
sys.stdin = open("input.txt")

password = {'0001101':'0', '0011001':'1', '0010011':'2',
            '0111101':'3', '0100011':'4', '0110001':'5',
            '0101111':'6', '0111011':'7', '0110111':'8',
            '0001011':'9'}

hex_dic = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

# 16진수 한 글자를 이진수로 변환
def hex_to_bin(n):
    b = ''
    for i in range(4):
        if n & (1 << i):
            b = '1' + b
        else:
            b = '0' + b
    return b

# 문자열 전체를 이진수로 변환
def hex_to_bin_line(line):
    result = ''
    for l in line:
        if l.isdigit():
            result += hex_to_bin(int(l))
        else:
            result += hex_to_bin(hex_dic[l])
    return result

for T in range(int(input())):
    N, M = map(int, input().split())
    board = set()
    codes = set()
    result = 0

    # 암호 코드가 있는 raw data -> board에 저장
    for _ in range(N):
        raw = input().rstrip().rstrip('0')  # 중간에 rstrip() 안해주면 제출 시 error남
        if raw:  # 0만 있는 줄은 rstrip('0')에서 다 지워져서 빈 문자열이므로, 유효한 줄만 board에 추가함
            board.add(hex_to_bin_line(raw).rstrip('0'))  # 변환한 뒤 오른쪽의 0들을 지워주고 암호 코드 후보들 board에 추가
    # 스캔하기 전의 raw data 탐색
    for rawdata in board:
        cur = rawdata
        while len(cur) > 0:  # 오른쪽에서부터 잘라내면서 진행
            # !! 배수 정하기 !!
            k = 1
            while len(cur) - k * 56 >= 0:
                tmp = cur[-56 * k:]
                check1 = '0' + ('1' * k) + '0'
                check2 = '1' + ('0' * k) + '1'
                if check1 in tmp or check2 in tmp:
                    break
                else:
                    k += 1
            # 오른쪽 k * 56 글자 빼내서 스캔
            code = ''
            for _ in range(8):
                last = ''
                raw_last = cur[-7 * k:]
                for i in range(7):
                    last += raw_last[i * k]
                cur = cur[:-7 * k]
                code = password[last] + code
            codes.add(code)
            # 남은 불필요한 0 제거
            cur = cur.rstrip('0')
            # 제거 후 cur가 남아있다면 다시 while 반복문 처음으로

    # 스캔한 코드들 유효성 검사
    for code in codes:
        judge = 0
        for i in range(4):
            judge += int(code[2 * i]) * 3 + int(code[2 * i + 1])
        if judge % 10 == 0:
            result += sum(map(int, code))

    print(f'#{T + 1} {result}')
