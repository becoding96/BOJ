import sys
sys.stdin = open("input.txt")

# 226ms
for T in range(int(input())):
    line = input()
    stack = []
    result = 0

    for i in range(len(line)):
        if line[i] == '(':
            stack.append(line[i])
        else:
            stack.pop()
            if line[i - 1] == '(':
                result += len(stack)
            else:
                result += 1

    print(f'#{T + 1} {result}')