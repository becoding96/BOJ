import sys
sys.stdin = open("input.txt")


def prim(r, V):
    MST = [0] * (V + 1)
    MST[r] = 1
    s = 0
    for _ in range(V):
        u = 0
        minV = 10
        for i in range(V + 1):
            if MST[i] == 1:
                for j in range(V + 1):
                    if MST[j] == 0 and 0 < adjM[i][j] < minV:
                        u = j
                        minV = adjM[i][j]
        s += minV
        MST[u] = 1
    return s


for T in range(int(input())):
    V, E = map(int, input().split())
    adjM = [[0] * (V + 1) for _ in range(V + 1)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        adjM[u][v] = w
        adjM[v][u] = w
    print(f'#{T + 1} {prim(0, V)}')
