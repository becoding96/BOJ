import sys
from collections import deque

input = sys.stdin.readline
n = int(input().rstrip())
array = [int(input()) for _ in range(n)]
tmp = deque()
res = deque()
sign = deque()
cnt = 0

for i in range(1, n + 1):
    tmp.append(i)
    sign.append('+')
    while len(tmp) > 0 and tmp[-1] == array[cnt]:
        cnt += 1
        res.append(tmp.pop())
        sign.append('-')

while len(tmp):
    res.append(tmp.pop())
    sign.append('-')

if array == list(res):
    for s in sign:
        print(s)
else:
    print('NO')
