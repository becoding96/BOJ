import sys
sys.stdin = open("input.txt")

# 127ms
for T in range(int(input())):
    V, E = map(int, input().split())
    graph = {i: [] for i in range(1, E + 1)}

    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)

    depart, arrive = map(int, input().split())

    ch = [0] * (V + 1)
    stack = []
    result = 0

    v = depart
    ch[v] = 1
    while True:
        for node in graph[v]:
            if node == arrive:
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

    print(f'#{T + 1} {result}')
