# 220826
import heapq, sys

input = sys.stdin.readline
N, H, T = map(int, input().split())
giants = []
for _ in range(N):
    heapq.heappush(giants, -int(input().rstrip()))

cnt = 0
for i in range(T):
    tallest = heapq.heappop(giants)
    if abs(tallest) < H:
        heapq.heappush(giants, tallest)
        break
    elif abs(tallest) == 1:
        heapq.heappush(giants, tallest)
        break
    else:
        tallest = -(abs(tallest) // 2)
        heapq.heappush(giants, tallest)
        cnt += 1

if H > abs(giants[0]):
    print("YES")
    print(cnt)
else:
    print("NO")
    print(abs(giants[0]))