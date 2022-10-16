import sys
sys.stdin = open("input.txt")

for T in range(10):
    SIZE = int(input())
    magnetic = [list(map(int, input().split())) for _ in range(SIZE)]
    magnetic = list(zip(*magnetic))
    result = 0

    for i in range(SIZE):
        result += str(magnetic[i]).replace('0, ', '').count('1, 2')

    print(f'#{T + 1} {result}')