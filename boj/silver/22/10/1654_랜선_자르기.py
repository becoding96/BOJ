# 221029
import sys; input = sys.stdin.readline

K, N = map(int, input().split())
lans = [int(input().rstrip()) for _ in range(K)]
result = 0

l, r = 0, max(lans)

while l <= r:
    if r == 1:
        result = 1
        break
    cnt = 0
    mid = (l + r) // 2
    for lan in lans:
        cnt += lan // mid
    if cnt >= N:
        l = mid + 1
        result = mid
    else:
        r = mid - 1

print(result)
