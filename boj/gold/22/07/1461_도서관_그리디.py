# 220730
n, m = map(int, input().split())
position = list(map(int, input().split()))

negative = [x for x in position if x < 0]
positive = [x for x in position if x > 0]

negative.sort()
positive.sort()

result = 0
farthest = max(max(position), -min(position))

i = 0
while i <= len(negative) - 1:
    cur = abs(negative[i])
    result += cur * 2
    i += m

j = len(positive) - 1
while j >= 0:
    cur = positive[j]
    result += cur * 2
    j -= m

result -= farthest

print(result)