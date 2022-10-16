import sys
sys.stdin = open("input.txt")


def bfs(v):
    q = [v]
    visited[v] = 1
    result = [v]
    while q:
        v = q.pop(0)
        for w in adj_dict[v]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = 1
                result.append(w)
    return result


V, E = map(int, input().split())
arr = list(map(int, input().split()))
adj_dict = {i: [] for i in range(1, V + 1)}
visited = [0 for _ in range(V + 1)]
for i in range(E):
    adj_dict[arr[i * 2]].append(arr[i * 2 + 1])
    adj_dict[arr[i * 2 + 1]].append(arr[i * 2])

result = bfs(1)
for i in range(V - 1):
    print(result[i], end="-")
print(result[V - 1])
