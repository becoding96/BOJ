import sys
sys.stdin = open("input.txt")

hex_dic = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

def hex_to_bin(n):
    b = ''
    for i in range(4):
        if n & (1 << i):
            b = '1' + b
        else:
            b = '0' + b
    return b

for T in range(int(input())):
    N, hex_num = input().split()
    N = int(N)
    result = ''
    for i in range(N):
        digit = hex_num[i]
        if digit.isdigit():
            result += hex_to_bin(int(digit))
        else:
            result += hex_to_bin(hex_dic[digit])
    print(f'#{T + 1} {result}')
