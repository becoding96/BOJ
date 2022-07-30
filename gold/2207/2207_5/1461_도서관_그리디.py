# 220730
n, m = map(int, input().split())
position = list(map(int, input().split()))

negative = [x for x in position if x < 0]
positive = [x for x in position if x > 0]

negative.sort()
positive.sort()

result = 0
abs_max = 0

i = 0
while i <= len(negative) - 1:
    cur = abs(negative[i])
    result += cur * 2
    if cur > abs_max:
        abs_max = cur
    i += m

j = len(positive) - 1
while j >= 0:
    cur = positive[j]
    result += cur * 2
    if cur > abs_max:
        abs_max = cur
    j -= m

result -= abs_max

print(result)