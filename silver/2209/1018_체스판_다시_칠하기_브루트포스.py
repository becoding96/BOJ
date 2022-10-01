# 220915
import sys


def block_count(part):
    start = part[0][0]
    start2 = 'W' if part[0][0] == 'B' else 'B'
    cnt = 0
    cnt2 = 1
    for i in range(8):
        for j in range(8):
            if i == 0 and j == 0:  # 중요!!
                continue
            if (i + j) % 2:
                if part[i][j] == start:
                    cnt += 1
                if part[i][j] == start2:
                    cnt2 += 1
            else:
                if part[i][j] != start:
                    cnt += 1
                if part[i][j] != start2:
                    cnt2 += 1
    return min(cnt, cnt2)


def brute(board, row, col):
    result = 9999
    for i in range(row - 8 + 1):
        for j in range(col - 8 + 1):
            part = []
            for k in range(8):
                part.append(board[i + k][j:j + 8])
            tmp = block_count(part)
            result = tmp if tmp < result else result
    return result


input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]
print(brute(board, N, M))
