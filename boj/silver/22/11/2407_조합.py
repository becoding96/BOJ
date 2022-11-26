# 221126
factorial = [1] * 101
for i in range(2, 101):
    factorial[i] = factorial[i - 1] * i

n, m = map(int, input().split())
print(factorial[n] // (factorial[n - m] * factorial[m]))
