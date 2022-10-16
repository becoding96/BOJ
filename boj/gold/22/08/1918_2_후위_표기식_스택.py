# 220818
# 인프런 강사님 풀이
import sys
from collections import deque

input = sys.stdin.readline
infix = input().rstrip()
stack = deque()
result = ''

for x in infix:
    if ord('A') <= ord(x) <= ord('Z'):
        result += x
    else:
        if x == '(':
            stack.append(x)
        elif x == '*' or x == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                result += stack.pop()
            stack.append(x)
        elif x == '+' or x == '-':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.append(x)
        elif x == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()

while stack:
    result += stack.pop()

print(result)
