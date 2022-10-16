import sys
sys.stdin = open("input.txt")

for T in range(int(input())):
    N, P = map(int, input().split())
    q, r = N // P, N % P
    print(f'#{T + 1} {q ** (P - r) * (q + 1) ** r}')