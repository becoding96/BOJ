# 220729
n = int(input())
expected_lank = []

for i in range(n):
    expected_lank.append(int(input()))

expected_lank.sort()

result = 0
for i in range(n):
    result += abs(i + 1 - expected_lank[i])

print(result)