import sys
sys.stdin = open("input.txt")

for T in range(int(input())):
    N, M, L = map(int, input().split())
    tree = [0] * (N + 2)  # N + 1하면 안됨 => (N // 2 + 1) * 2

    leaf_min = 9999
    for _ in range(M):
        node, value = map(int, input().split())
        tree[node] = value
        leaf_min = node if node < leaf_min else leaf_min

    for i in range(leaf_min - 1, 0, -1):  # 뒤에서부터 와야함!
        if tree[i] == 0:
            tree[i] = tree[i * 2] + tree[i * 2 + 1]

    print(f'#{T + 1} {tree[L]}')