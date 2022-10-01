# 220901
import sys

def factorial(n):
    result = n
    while n >= 3:
        n -= 1
        result *= n
    return result

def combination(n, r):
    if n == r:
        return 1
    elif r == 1 or n - r == 1:
        return n

    if r >= n // 2 + 1:
        r = n - r
    
    return int(factorial(n) / (factorial(n - r) * factorial(r)))

input = sys.stdin.readline
for _ in range(int(input().rstrip())):
    N, M = map(int, input().split())
    print(combination(M, N))
