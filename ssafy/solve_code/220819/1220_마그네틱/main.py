import sys
sys.stdin = open("input.txt")

for T in range(10):
    SIZE = int(input())
    magnetic = [list(map(int, input().split())) for _ in range(SIZE)]
    magnetic = list(zip(*magnetic))
    result = 0

    for i in range(SIZE):
        tmp = list(magnetic[i])[:]
        while tmp and tmp[0] == 2:
            tmp.pop(0)
        while tmp and tmp[-1] == 1:
            tmp.pop()
        stack = []
        for x in tmp:
            if x != 0:
                stack.append(x)
        for j in range(len(stack) - 1):
            if stack[j] == 1 and stack[j + 1] == 2:
                result += 1

    print(f'#{T + 1} {result}')



