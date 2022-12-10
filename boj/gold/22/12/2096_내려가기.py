# 221208
import sys; input = sys.stdin.readline;

N = int(input().rstrip())
dp = [[0, 0] for _ in range(3)]  # [0, 0]에서 왼쪽이 최대, 오른쪽이 최소
tmp = [[0, 0] for _ in range(3)]  # 중간에 계산 결과가 바뀌는 걸 막기 위해 필요

for i in range(N):
    a, b, c = map(int, input().split())  # 입력을 받으면서 계산하고, 바로 버려야 메모리 초과가 안남
    tmp[0][0] = a + max(dp[0][0], dp[1][0])
    tmp[0][1] = a + min(dp[0][1], dp[1][1])
    tmp[1][0] = b + max(dp[0][0], dp[1][0], dp[2][0])
    tmp[1][1] = b + min(dp[0][1], dp[1][1], dp[2][1])
    tmp[2][0] = c + max(dp[1][0], dp[2][0])
    tmp[2][1] = c + min(dp[1][1], dp[2][1])

    dp[0][0], dp[0][1] = tmp[0][0], tmp[0][1]
    dp[1][0], dp[1][1] = tmp[1][0], tmp[1][1]
    dp[2][0], dp[2][1] = tmp[2][0], tmp[2][1]

max_rst, min_rst = 0, 9 * N
for j in range(3):
    max_rst = dp[j][0] if dp[j][0] > max_rst else max_rst
    min_rst = dp[j][1] if dp[j][1] < min_rst else min_rst

print(max_rst, min_rst)
