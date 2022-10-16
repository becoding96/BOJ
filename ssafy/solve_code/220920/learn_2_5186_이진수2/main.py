import sys
sys.stdin = open("input.txt")


def to_bin(f):
    result = ''
    while len(result) <= 11:
        f *= 2
        if f > 1:
            result += '1'
            f -= 1
        elif f < 1:
            result += '0'
        else:
            return result + '1'
    return 'overflow'


for T in range(int(input())):
    N = float(input())
    print(f'#{T + 1} {to_bin(N)}')
