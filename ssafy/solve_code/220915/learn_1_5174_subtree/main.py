import sys
sys.stdin = open("input.txt")


def preorder(v):
    if v:
        global cnt
        cnt += 1
        preorder(ch1[v])
        preorder(ch2[v])


for T in range(int(input())):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    V = E + 1
    ch1 = [0] * (V + 1)
    ch2 = [0] * (V + 1)
    cnt = 0

    for i in range(E):
        p, c = arr[i * 2], arr[i * 2 + 1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c

    preorder(N)
    print(f'#{T + 1} {cnt}')
