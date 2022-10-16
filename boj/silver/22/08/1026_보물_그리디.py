# 220811
import sys

input = sys.stdin.readline
N = int(input().rstrip())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
result = 0

A.sort()

for i in range(N):
    a = A[i]
    b = B.pop(B.index(max(B)))
    result += a * b

print(result)