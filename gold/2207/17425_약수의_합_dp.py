# 220723
import sys

x_list = []
for _ in range(int(sys.stdin.readline())):
    x = int(sys.stdin.readline())
    x_list.append(x)

MAX = max(x_list)

eratos = [1] * (MAX + 1) # 모든 수는 1을 약수로 포함하고 있으므로 1로 초기화 
dp = [0] * (MAX + 1) # g(x) 배열, ex) dp[2] = g(2)
dp[1] = 1

for i in range(2, MAX + 1): 
    j = 1
    while i * j <= MAX: # 에라토스테네스의 체
        eratos[i * j] += i
        j += 1
    dp[i] = dp[i - 1] + eratos[i] # g(i)를 dp방식으로 계산

for x in x_list:
    print(dp[x])