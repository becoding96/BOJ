import sys
sys.stdin = open("input.txt")

# 131ms
for T in range(int(input())):
    N = int(input())
    prime = [2, 3, 5, 7, 11]
    result = [0] * 5

    while N != 1:
        for i in range(5):
            if N % prime[i] == 0:
                N //= prime[i]
                result[i] += 1

    print(f'#{T + 1}', end=" ")
    print(*result)


