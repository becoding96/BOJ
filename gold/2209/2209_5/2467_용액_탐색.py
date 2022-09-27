# 220927

import sys

input = sys.stdin.readline
N = int(input().rstrip())
liquid = sorted(list(map(int, input().split())), key=lambda x: abs(x))
mix_min = 2000000000
result = [liquid[0], liquid[1]]

for i in range(N - 1):
    mix = abs(liquid[i] + liquid[i + 1])
    if mix < mix_min:
        mix_min = mix
        result[0], result[1] = liquid[i], liquid[i + 1]

result.sort()
print(*result)

