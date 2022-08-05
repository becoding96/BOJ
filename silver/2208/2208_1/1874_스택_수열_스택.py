# 220805
import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
array = [int(input()) for _ in range(n)]
tmp = deque()
stack = deque()
sign = deque()
cnt = 0

for i in range(1, n + 1):
    tmp.append(i)
    sign.append('+')
    while len(tmp) > 0 and tmp[-1] == array[cnt]:
        cnt += 1
        stack.append(tmp.pop())
        sign.append('-')

while len(tmp):
    stack.append(tmp.pop())
    sign.append('-')

if array == list(stack):
    for s in sign:
        print(s)
else:
    print('NO')
