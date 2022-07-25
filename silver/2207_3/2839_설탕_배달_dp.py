# 220716
n = int(input())

if n < 5:
    if n == 3:
        print(1)
    else:
        print(-1)
    exit()

dp = [9999 for _ in range(n + 1)]
dp[3] = 1
dp[5] = 1

for i in range(6, len(dp)):
    dp[i] = min(dp[i - 3] + 1, dp[i - 5] + 1)

if dp[n] > 9999:
    print(-1)
else:
    print(dp[n])