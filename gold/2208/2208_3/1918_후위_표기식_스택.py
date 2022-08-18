# 220818
import sys
from collections import deque

'''
주어진 문자열을 순회한다.
숫자가 나오면 결과에 더한다.
+, - 가 나오면 스택에 append하고, 이미 스택에 연산자가 있다면 pop해서 결과에 더한다.
*, / 가 나오면 스택에 append하고, 이미 스택에 *, /가 있다면 pop해서 결과에 더한다.
(+, -는 *, / 보다 우선 순위가 낮으므로 무시하고 pop하지 않고 append한다.)
괄호가 나오면 괄호 내부를 하나의 다른 연산식으로 보고 재귀 함수를 사용한다.
'''

def postfix(infix):
    result = ''
    stack = deque()
    i = 0

    while i < len(infix):
        if infix[i] == '(':
            tmp = ''
            i += 1
            cnt = 1  # 괄호 카운트, 닫는 괄호가 나오자마자 끝나는 방식에서 바꿈 (내부의 괄호로 인해 반복문이 종료될 수 있어서)
            while True:
                if infix[i] == '(':
                    cnt += 1
                elif infix[i] == ')':
                    cnt -= 1
                    if cnt == 0:
                        break
                tmp += infix[i]
                i += 1
            result += postfix(tmp)

        c = infix[i]

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
infix = input().rstrip()

print(postfix(infix))
