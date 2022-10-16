for T in range(10):
    N = int(input())
    infix = input()
    stack = []
    postfix = ''
    stack2 = []

    # 중위 표기식을 후위 표기식으로 변경
    for x in infix:
        if ord('0') <= ord(x) <= ord('9'):
            postfix += x
        else:
            if x == '(':
                stack.append(x)
            elif x == '*' or x == '/':
                while stack and (stack[-1] == '*' or stack[-1] == '/'):
                    postfix += stack.pop()
                stack.append(x)
            elif x == '+' or x == '-':
                while stack and stack[-1] != '(':
                    postfix += stack.pop()
                stack.append(x)
            elif x == ')':
                while stack and stack[-1] != '(':
                    postfix += stack.pop()
                stack.pop()

    while stack:
        postfix += stack.pop()

    # 후위 표기식으로 계산
    for x in postfix:
        if ord('0') <= ord(x) <= ord('9'):
            stack2.append(int(x))
        elif x == '+':
            stack2.append(stack2.pop() + stack2.pop())
        elif x == '-':
            stack2.append(-stack2.pop() + stack2.pop())
        elif x == '*':
            stack2.append(stack2.pop() * stack2.pop())
        elif x == '/':
            stack2.append(1 / (stack2.pop() / stack2.pop()))

    print(f'#{T + 1} {stack2.pop()}')
