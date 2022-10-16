import sys
from collections import deque
sys.stdin = open("input.txt")

def make_network(n, lst):
    net = [[] for _ in range(101)]
    for i in range(N // 2):
        net[lst[2 * i]].append(lst[2 * i + 1])
    return net

def bfs(v, lst):
    visited = [0] * 101
    visited[v] = 1
    q = deque([v])
    while True:
        length = len(q)
        result = 0
        for _ in range(length):
            cur = q.popleft()
            result = cur if result < cur else result
            for nv in lst[cur]:  # 동시에 연락을 취한다
                if visited[nv] == 0:
                    q.append(nv)
                    visited[nv] = 1
        if not q:
            return result

for T in range(10):
    N, start = map(int, input().split())
    from_to = list(map(int, input().split()))
    network = make_network(N, from_to)
    print(f'#{T + 1} {bfs(start, network)}')
