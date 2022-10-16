import sys
sys.stdin = open("input.txt")


def dijkstra(s, N):
    decided = [0] * (N + 1)
    decided[s] = 1
    for i in range(N + 1):
        D[i] = costs[s][i]

    for _ in range(N):
        minV = MAX_DIS
        w = 0
        for i in range(N + 1):
            if decided[i] == 0 and D[i] < minV:
                minV = D[i]
                w = i
        decided[w] = 1
        for v in range(N + 1):
            if 0 < costs[w][v] < MAX_DIS:
                D[v] = min(D[w] + costs[w][v], D[v])


for T in range(int(input())):
    N, E = map(int, input().split())
    MAX_DIS = N * 1000000
    costs = [[MAX_DIS] * (N + 1) for _ in range(N + 1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        costs[s][e] = w
    D = [0] * (N + 1)
    dijkstra(0, N)
    print(f'#{T + 1} {D[N]}')
