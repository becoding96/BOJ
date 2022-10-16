import sys
sys.stdin = open("input.txt")

for T in range(int(input())):
    N = int(input())
    times = [tuple(map(int, input().split())) for _ in range(N)]
    times.sort(key=lambda x: x[1])
    cnt = 1
    end_time = times[0][1]
    for i in range(1, N):
        if times[i][0] >= end_time:
            cnt += 1
            end_time = times[i][1]
    print(f'#{T + 1} {cnt}')
