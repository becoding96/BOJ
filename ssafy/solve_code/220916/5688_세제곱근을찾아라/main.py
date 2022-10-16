import sys
sys.stdin = open("input.txt")

for T in range(int(input())):
    N = int(input())
    cube = int(N ** (1/3))  # 부동소수점 때문에 int
    result = -1
    # 부동소수점 문제 발생 시 int()의 버림 때문에 +1 까지 탐색
    for i in [cube, cube + 1]:
        if i ** 3 == N:
            result = i
    print(f'#{T + 1} {result}')
