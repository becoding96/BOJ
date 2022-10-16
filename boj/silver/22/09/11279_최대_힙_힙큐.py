# 220830
import sys, heapq

input = sys.stdin.readline
heap = []
for _ in range(int(input().rstrip())):
    x = int(input().rstrip())
    if x == 0:
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, -x)
