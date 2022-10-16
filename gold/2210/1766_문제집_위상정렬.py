# 221012
import sys, heapq; input = sys.stdin.readline

N, M = map(int, input().split())
trail = [[] for _ in range(N + 1)]
pre_cnt = [0] * (N + 1)
for _ in range(M):
    a, b = map(int, input().split())
    trail[a].append(b)
    pre_cnt[b] += 1
q = []
result = ""

for i in range(1, N + 1):
    if pre_cnt[i] == 0:
        heapq.heappush(q, i)

while q:
    pr = heapq.heappop(q)
    result += str(pr) + " "
    for t in trail[pr]:
        pre_cnt[t] -= 1
        if pre_cnt[t] == 0:
            heapq.heappush(q, t)

print(result)
