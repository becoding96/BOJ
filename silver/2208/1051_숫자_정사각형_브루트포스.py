# 220821
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
rec = [list(map(int, input().rstrip())) for _ in range(N)]
result = 1

for i in range(N):
    for j in range(M):
        std = rec[i][j]
        for k in range(j + 1, M):
            if (
                rec[i][k] == std and
                i + k - j < N and
                rec[i + k - j][j] == std and
                rec[i + k - j][k] == std
            ):
                area = (k - j + 1) ** 2
                result = area if area > result else result

print(result)
