# 221214
N, K = map(int, input().split())

if K == 1:
    print(1)
    exit()
elif N == 1:
    print(K)
    exit()

dp = [[1 for _ in range(N)] for _ in range(K)]

for i in range(K):
    dp[i][0] = i + 1

for i in range(1, K):
    for j in range(1, N):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

print(dp[K - 1][N - 1] % 1_000_000_000)
