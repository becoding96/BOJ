# 220805
import sys
from collections import deque

input = sys.stdin.readline

for _ in range(int(input().rstrip())):
    line = input().rstrip()
    stack = deque()
    flag = False
    for p in line:
        if p == '(':
            stack.append(p)
        else:
            try:
                stack.pop()
            except:
                flag = True
                break
    if flag or len(stack):
        print("NO")
        continue
    print("YES")
