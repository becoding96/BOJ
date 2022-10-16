import sys
sys.stdin = open("input.txt")

'''
0의 아스키코드 값에 1의 자리 숫자 n을 더하고
다시 해당 코드에 chr 함수를 사용하면
string 형태의 n이 반환된다.
'''

def itoa(n, s):
    if n == 0:
        print('0')
    minus = False
    if n < 0:                       # n이 음수인 경우 양수로 변환
        n = -n
        minus = True
    while n > 0:                    # n을 계속 10으로 나누면서 n이 0보다 큰 동안 반복
        r = n % 10                  # 10으로 나눠서 나머지인 1의 자리 추출
        s += chr(ord('0') + r)      # 1의 자리를 문자로 변환
        n //= 10                    # n을 10으로 나눔
    if minus:                       # 음수인 경우 -를 붙혀서 출력
        print('-' + s)
    else:
        print(s)

for T in range(int(input())):
    n = int(input())
    empty_string = ''
    print(f'#{T + 1} ', end = "")
    itoa(n, empty_string)