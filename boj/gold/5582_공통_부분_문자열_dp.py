# 220816
# pypy3 제출
import sys

input = sys.stdin.readline
str1 = input().rstrip()
str2 = input().rstrip()
n = len(str1)
m = len(str2)
result = 0

board = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if str1[i - 1] == str2[j - 1]:
            board[i][j] = board[i - 1][j - 1] + 1
            result = board[i][j] if board[i][j] > result else result

print(result)