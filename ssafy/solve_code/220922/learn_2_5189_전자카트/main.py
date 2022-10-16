import sys
sys.stdin = open("input.txt")


def perm(i, k, r):
    global result
    if i == r:
        case = [1] + p + [1]
        case_sum = 0
        for j in range(len(case) - 1):
            case_sum += board[case[j] - 1][case[j + 1] - 1]
        result = case_sum if case_sum < result else result
    else:
        for j in range(k):
            if used[j] == 0:
                used[j] = 1
                p[i] = arr[j]
                perm(i + 1, k, r)
                used[j] = 0


for T in range(int(input())):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    R = N - 1
    arr = [i for i in range(2, N + 1)]
    used = [0] * (N - 1)
    p = [0] * (N - 1)
    result = 100 * 11
    perm(0, N - 1, R)
    print(f'#{T + 1} {result}')
