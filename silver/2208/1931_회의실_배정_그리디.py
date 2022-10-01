# 220816
import sys

input = sys.stdin.readline
n = int(input().rstrip())
meeting = [tuple(map(int, input().split())) for _ in range(n)]

meeting.sort(key=lambda m: (m[1], m[0]))

end = 0
cnt = 0
for m in meeting:
    if m[0] >= end:
        end = m[1]
        cnt += 1

print(cnt)