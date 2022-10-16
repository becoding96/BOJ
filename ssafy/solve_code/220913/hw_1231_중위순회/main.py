import sys
sys.stdin = open("input.txt")


def inorder(v):
    if tree[v]:
        inorder(tree[v][0])
    print(alph[v], end='')
    if len(tree[v]) == 2:
        inorder(tree[v][1])


for T in range(10):
    N = int(input())
    tree = [[] for _ in range(N + 1)]
    alph = [' ']
    for _ in range(N):
        line = list(input().split())
        alph.append(line[1])
        for i in range(2, len(line)):
            tree[int(line[0])].append(int(line[i]))
    visit = []
    print(f'#{T + 1}', end=' ')
    inorder(1)
    print()
