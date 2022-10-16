import sys
sys.stdin = open("input.txt")

# 140ms
for _ in range(10):
    T, E = map(int, input().split())
    link = list(map(int, input().split()))
    graph = {i: [] for i in range(100)}
    for i in range(0, len(link) - 1, 2):
        graph[link[i]].append(link[i + 1])
    ch = [0] * 100
    result = 0

    v = 0
    ch[v] = 1
    stack = []
    while True:
        for node in graph[v]:
            if node == 99:
                result = 1
                break
            if ch[node] == 0:
                stack.append(v)
                v = node
                ch[v] = 1
                break
        else:
            if stack:
                v = stack.pop()
            else:
                break

        if result:
            break

    print(f'#{T} {result}')




