# 221015
import sys; input = sys.stdin.readline
from collections import deque

for _ in range(int(input().rstrip())):
    N, K = map(int, input().split())
    D_list = [0] + list(map(int, input().split()))
    trail = [[] for _ in range(N + 1)]
    pre_cnt = [0] * (N + 1)
    for _ in range(K):
        a, b = map(int, input().split())
        trail[a].append(b)
        pre_cnt[b] += 1
    W = int(input().rstrip())

    q = deque()
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        if pre_cnt[i] == 0:
            q.append(i)
            dp[i] = D_list[i]

    while q:
        v = q.popleft()
        for nv in trail[v]:
            dp[nv] = max(dp[v] + D_list[nv], dp[nv])
            pre_cnt[nv] -= 1
            if pre_cnt[nv] == 0:
                q.append(nv)
    
    print(dp[W])
