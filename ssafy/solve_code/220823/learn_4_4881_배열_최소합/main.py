import sys
sys.stdin = open("input.txt")


def backtrack(i, arr):
    global result
    s = sum(arr)
    if s > result:
        return
    if len(arr) == 3:
        result = s if s < result else result
        return
    for j in range(N):
        for t in arr:
            if j == t[0]:
                continue
        arr.append((j, board[i][j]))
        backtrack(i + 1, arr)


for T in range(int(input())):
    N = int(input())
    P = [i for i in range(N)]
    board = []
    for i in range(N):
        board.append({})
    result = 90
    backtrack(0, [])
    print(f'#{T + 1} {result}')
