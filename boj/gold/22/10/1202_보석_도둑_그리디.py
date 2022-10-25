# 221025
import sys, heapq; input = sys.stdin.readline

N, K = map(int, input().split())
jewels = []
for _ in range(N):
    heapq.heappush(jewels, tuple(map(int, input().split())))
bags = sorted([int(input().rstrip()) for _ in range(K)])
result = 0

jewels_for_bag = []
for bag in bags:
    while jewels and bag >= jewels[0][0]:
        heapq.heappush(jewels_for_bag, -heapq.heappop(jewels)[1])
    if jewels_for_bag:
        result += -heapq.heappop(jewels_for_bag)
print(result)
