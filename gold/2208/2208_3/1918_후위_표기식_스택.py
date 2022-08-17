# 220818
import sys
from collections import deque


def postfix(formula):
    result = ''
    stack = deque()
    i = 0

    while i < len(formula):
        if formula[i] == '(':
            tmp = ''
            i += 1
            cnt = 1
            while True:
                if formula[i] == '(':
                    cnt += 1
                elif formula[i] == ')':
                    cnt -= 1
                    if cnt == 0:
                        break
                tmp += formula[i]
                i += 1
            result += postfix(tmp)

        c = formula[i]

        if ord('A') <= ord(c) <= ord('Z'):
            result += c

        if c == '+' or c == '-':
            while stack:
                result += stack.pop()
            stack.append(c)
        elif c == '*' or c == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                result += stack.pop()
            stack.append(c)

        i += 1

    while stack:
        result += stack.pop()

    return result


input = sys.stdin.readline
line = input().rstrip()

print(postfix(line))
