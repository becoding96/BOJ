import sys
sys.stdin = open("input.txt")

for T in range(int(input())):
    day, month, three_months, year = map(int, input().split())
    plan = list(map(int, input().split()))
    month = three_months if three_months < month else month
    dp = [0] * 12
    dp[0] = min(plan[0] * day, month)
    for i in range(3):
        dp[i] = min(dp[i - 1] + min(plan[i] * day, month), three_months)
    for i in range(3, 12):
        dp[i] = min(dp[i - 1] + min(plan[i] * day, month), dp[i - 3] + three_months)
    print(f'#{T + 1} {min(dp[11], year)}')