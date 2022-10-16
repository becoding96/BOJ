# 220810

# 카운팅 정렬

import sys

input = sys.stdin.readline

N = int(input())
cnts = [0] * 10001

for i in range(N):
    cnts[int(input())] += 1

for i in range(10001):
    if cnts[i] != 0:
        for _ in range(cnts[i]):
            print(i)
