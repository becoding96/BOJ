import sys
sys.stdin = open("input.txt")

for T in range(10):
    N, pw = input().split()
    N = int(N)
    stack = []
    for x in pw:
        if stack and stack[-1] == x:
            stack.pop()
        else:
            stack.append(x)

    print(f"#{T + 1} {''.join(stack)}")
