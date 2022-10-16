# 220904

'''
f(n - 3)에서 오른쪽에 바로 3을 놓는 경우
f(n - 2)에서 오른쪽에 바로 2를 놓는 경우
f(n - 1)에서 오른쪽에 바로 1을 놓는 경우
를 합했을 때, f(n)과 값이 같아짐

f(n - 3)에서 1을 놓는 경우는 f(n - 2)에 포함되고
2를 놓는 경우는 f(n - 1)에 포함된다.
f(n - 2)에서 1을 놓는 경우는 f(n - 1)에 포함된다.
'''

N = int(input().rstrip())
arr = [int(input().rstrip()) for _ in range(N)]
index_max = max(arr)
dp = [1, 2, 4] + [0] * (index_max - 3)
for i in range(3, index_max):
    dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]
for n in arr:
    print(dp[n - 1])