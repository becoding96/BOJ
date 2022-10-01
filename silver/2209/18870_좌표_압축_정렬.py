# 220927

import sys

input = sys.stdin.readline
N = int(input().rstrip())
points = list(map(int, input().split()))

points_pretreated = sorted(list(set(points)))
dic = {points_pretreated[i]: i for i in range(len(points_pretreated))}
for point in points:
    print(dic[point], end=' ')
