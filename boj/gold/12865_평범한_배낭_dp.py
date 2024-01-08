# 220725

# 물품은 종류 당 하나이므로
# 중복을 방지하기 위해서는 2차원 냅색 알고리즘 사용해야 한다.
# 그러나 2차원은 메모리를 많이 사용하기 때문에
# 1차원 배열의 끝에서 역으로 진행하는 것으로 해결한다.

N, K = map(int, input().split())
dp = [0] * (K + 1)

for i in range(N):
    W, V = map(int, input().split())
    for j in range(K, W - 1, -1):
        dp[j] = max(dp[j], dp[j - W] + V)

print(dp[K])