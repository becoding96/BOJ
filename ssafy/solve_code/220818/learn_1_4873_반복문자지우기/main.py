import sys
sys.stdin = open("input.txt")

# 127ms
for T in range(int(input())):
    s = input().rstrip()
    stack = [s[0]]

    for i in range(1, len(s)):
        if stack and s[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(s[i])

    print(f'#{T + 1} {len(stack)}')