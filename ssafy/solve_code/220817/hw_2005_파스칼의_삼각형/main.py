import sys

sys.stdin = open("input.txt")

for T in range(int(input())):
    N = int(input())
    pascal = [[] for _ in range(N)]

    print(f'#{T + 1}')

    for i in range(1, N + 1):
        for j in range(i):
            if j == 0 or j == i - 1:
                pascal[i - 1].append(1)
            else:
                pascal[i - 1].append(pascal[i - 2][j - 1] + pascal[i - 2][j])
        print(*pascal[i - 1])




