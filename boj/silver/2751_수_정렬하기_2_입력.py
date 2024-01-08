# 220718
# 입력 효율, input()말고 readline() 사용!
import sys

n = int(input())
l = [int(sys.stdin.readline()) for _ in range(n)]

l.sort()

for num in l:
    print(num)