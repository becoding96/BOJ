import sys

sys.stdin = open("input.txt")

for T in range(int(input())):
    stack = []
    result = 1

    for x in input():
        if x == '(':
            stack.append(x)
        else:
            if not stack:
                result = -1
                break
            else:
                stack.pop()

    if stack:
        result = -1

    print(f'#{T + 1} {result}')