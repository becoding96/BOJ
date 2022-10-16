import sys

sys.stdin = open("input.txt")

n, r = map(int, input().split())
link = list(map(int, input().split()))
graph = {i: [] for i in range(1, n + 1)}
ch = [0] * (n + 1)
stack = []

for i in range(len(link)):
    if i % 2 == 0:
        graph[link[i]].append(link[i + 1])
        graph[link[i + 1]].append(link[i])

v = 1
ch[v] = 1
print(v, end=" ")

while True:
    for x in graph[v]:
        if ch[x] == 0:
            stack.append(v)
            v = x
            print(v, end=" ")
            ch[v] = 1
            break
    else:
        if stack:
            v = stack.pop()
        else:
            break




