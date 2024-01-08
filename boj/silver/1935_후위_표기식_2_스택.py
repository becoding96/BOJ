# 220818
import sys
from collections import deque

input = sys.stdin.readline
N = int(input().rstrip())
postfix = input().rstrip()
nums = [int(input().rstrip()) for _ in range(N)]
stack = deque()

for x in postfix:
    if ord('A') <= ord(x) <= ord('Z'):
        stack.append(nums[ord(x) - ord('A')])
    elif x == '+':
        stack.append(stack.pop() + stack.pop())
    elif x == '-':
        stack.append(-stack.pop() + stack.pop())
    elif x == '*':
        stack.append(stack.pop() * stack.pop())
    elif x == '/':
        stack.append(1 / (stack.pop() / stack.pop()))

print(f'{stack.pop():.2f}')  # f-string 소수점 자리수 표현
