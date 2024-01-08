# 220717
n = int(input())
dp = [0] * (n + 1)

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1 # 최대 횟수 저장, 1씩 빼는 것이 제일 오래 걸리기 때문
    if i % 3 == 0: # if elif 사용 X
        dp[i] = min(dp[i], dp[i // 3] + 1) # 나눠 떨어지더라도 // 사용해야 함.
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

print(dp[n])