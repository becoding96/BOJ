import sys
sys.stdin = open("input.txt")

def bfs(v):
    visited = [0] * (V + 1)
    visited[v] = 0
    q = [v]
    while q:
        cur = q.pop(0)
        for w in graph[cur]:
            if w == G:
                return visited[cur] + 1
            if visited[w] == 0:
                visited[w] = visited[cur] + 1
                q.append(w)
    return 0

for T in range(int(input())):
    V, E = map(int, input().split())
    graph = {i + 1: [] for i in range(V)}
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    S, G = map(int, input().split())
    print(f'#{T + 1} {bfs(S)}')