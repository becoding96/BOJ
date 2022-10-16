# 220731
n = int(input())
weight = list(map(int, input().split()))
weight.sort()

if weight[0] > 1:  # 제일 가벼운 추가 1보다 크다면 답은 1
    print(1)
    exit()
# 그게 아니라면 가장 가벼운 추는 1이므로
r = 1  # 처음 표현할 수 있는 범위는 0 ~ 1, r은 안끊기고 현재 표현할 수 있는 최대값

# 두 번째 추부터 탐색
for i in range(1, n):
    # 추의 무게가 기존 표현 범위의 최대값보다 2이상 크다면 break
    # => 범위가 이어지지 않으므로
    if weight[i] > r[1] + 1:
        break
    r[1] += weight[i]

print(r[1] + 1)  # 최대값 + 1
