import sys
sys.stdin = open("input.txt")

# 연습문제 1 - extra 방식
for T in range(int(input())):
    infix = input()
    stack = []
    result = ''

    for x in infix:
        if ord('1') <= ord(x) <= ord('9'):
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

    print(f'#{T + 1} {result}')
