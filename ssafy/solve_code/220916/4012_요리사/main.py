import sys
sys.stdin = open("input.txt")

def comb(arr, r):
    result = []
    if r == 1:
        for i in arr:
            result.append([i])
    elif r > 1:
        for i in range(len(arr) - r + 1):
            for j in comb(arr[i + 1:], r - 1):
                result.append([arr[i]] + j)
    return result

for T in range(int(input())):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    arr = [i for i in range(N)]
    result = 20001
    A_materials = comb(arr, N // 2)
    for A in A_materials:
        B = list(set(arr) - set(A))
        A_sum = sum([board[i][j] for i in A for j in A])
        B_sum = sum([board[i][j] for i in B for j in B])
        result = min(abs(A_sum - B_sum), result)
    print(f'#{T + 1} {result}')
