import sys
sys.stdin = open("sample_input.txt")


def backtrack(i, change_cnt):
    global result
    if change_cnt >= result:
        return
    if i >= N:
        result = change_cnt
    else:
        for k in range(1, station[i] + 1):
            backtrack(i + k, change_cnt + 1)


for T in range(int(input())):
    N, *station = list(map(int, input().split()))
    station = [0] + station
    result = 100
    backtrack(1, 0)
    # 종점에 들어올 때는 1 추가할 필요 없으므로 다시 1을 빼줌
    result -= 1
    print(f'#{T + 1} {result}')
