import sys
sys.stdin = open("input.txt")

# 131ms
dp = [0] * 31
dp[1] = 1
dp[2] = 3
for i in range(3, 31):
    dp[i] = dp[i - 1] + dp[i - 2] * 2

for T in range(int(input())):
    N = int(input())
    N //= 10
    print(f'#{T + 1} {dp[N]}')


