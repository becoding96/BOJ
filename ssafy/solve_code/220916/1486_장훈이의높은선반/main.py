import sys
sys.stdin = open("input.txt")

def f(i, n, s):
    global result
    if s >= result:
        return
    if i == n:
        if s >= B and s < result:
            result = s
    else:
        f(i + 1, n, s + heights[i])
        f(i + 1, n, s)

for T in range(int(input())):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    result = 200000
    f(0, N, 0)
    print(f'#{T + 1} {result - B}')
