import sys
sys.stdin = open("input.txt")

# 125ms
for T in range(int(input())):
    s = input().rstrip()
    stack = []
    i = 0
    result = 1

    for x in s:
        if x == "(" or x == "{":
            stack.append(x)
        elif x == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                result = 0
                break
        elif x == "}":
            if stack and stack[-1] == "{":
                stack.pop()
            else:
                result = 0
                break

    if stack:
        result = 0

    print(f'#{T + 1} {result}')
