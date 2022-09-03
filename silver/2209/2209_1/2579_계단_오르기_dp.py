# 220904
import sys

input = sys.stdin.readline
N = int(input().rstrip())
stairs = [int(input().rstrip()) for _ in range(N)]
dp = [0] * N
dp[0] = stairs[0]
if N >= 2:
    dp[1] = stairs[0] + stairs[1]
if N >= 3:
    dp[2] = stairs[2] + max(stairs[0], stairs[1])
if N >= 4:
    for i in range(3, N):
        dp[i] = stairs[i] + max(dp[i - 2], stairs[i - 1] + dp[i - 3])
print(dp[-1])
