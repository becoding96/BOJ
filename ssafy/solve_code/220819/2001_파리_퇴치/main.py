import sys
sys.stdin = open("input.txt")

# 153ms
for T in range(int(input())):
    N, M = map(int, input().split())
    fly = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    for i in range(N - M + 1):
        for j in range(N - M + 1):
            tmp = 0
            for k in range(M):
                for l in range(M):
                    tmp += fly[i + k][j + l]
            result = tmp if tmp > result else result

    print(f'#{T + 1} {result}')
