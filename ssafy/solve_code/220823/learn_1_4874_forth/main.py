import sys
sys.stdin = open("input.txt")

for T in range(int(input())):
    postfix = list(input().split())
    stack = []

    try:
        for x in postfix:
            if x == '+':
                stack.append(stack.pop() + stack.pop())
            elif x == '-':
                stack.append(-stack.pop() + stack.pop())
            elif x == '*':
                stack.append(stack.pop() * stack.pop())
            elif x == '/':
                q = stack.pop()
                d = stack.pop()
                stack.append(d // q)
            elif x == '.':
                if len(stack) == 1:                     # 연산이 제대로 되어서 숫자 하나가 남음
                    print(f'#{T + 1} {stack.pop()}')
                else:                                   # 연산자가 원래 필요한 숫자보다 많으면 위에서 에러가 나므로 except에 걸림
                    print(f'#{T + 1} error')            # 숫자가 많은건 에러가 안나므로 따로 예외 처리
                break
            else:
                stack.append(int(x))
    except:
        print(f'#{T + 1} error')

