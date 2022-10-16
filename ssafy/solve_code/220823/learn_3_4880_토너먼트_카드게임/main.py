import sys
sys.stdin = open("input.txt")


def rsp(arr):
    if len(arr) == 1:
        return arr

    mid = (len(arr) - 1) // 2
    left = rsp(arr[:mid + 1])
    right = rsp(arr[mid + 1:])

    result = left[0][1] - right[0][1]
    if result == 1 or result == -2:
        return left
    elif result == -1 or result == 2:
        return right
    else:
        return left


for T in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    num = [i + 1 for i in range(N)]
    arr = list(zip(num, arr))
    print(f'#{T + 1} {rsp(arr)[0][0]}')
