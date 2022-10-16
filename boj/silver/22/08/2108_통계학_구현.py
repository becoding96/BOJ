# 220810
import sys

input = sys.stdin.readline

n = int(input().rstrip())
array = [int(input().rstrip()) for _ in range(n)]
array.sort()

if n == 1:
    a = array[0]
    print(a)
    print(a)
    print(a)
    print(0)
    exit()

# 산술평균
print(round(sum(array) / n))

# 중앙값
print(array[n // 2])

# 최빈값
cnts = {}
for i in range(1, n + 1):
    cnts[i] = []

cnt = 1
max_cnt = 1

for i in range(1, n):
    if array[i] == array[i - 1]:
        cnt += 1
    else:
        cnts[cnt].append(array[i - 1])
        max_cnt = cnt if cnt > max_cnt else max_cnt
        cnt = 1

    if i == n - 1:
        cnts[cnt].append(array[i])
        max_cnt = cnt if cnt > max_cnt else max_cnt

cnts[max_cnt].sort()

if len(cnts[max_cnt]) >= 2:
    print(cnts[max_cnt][1])
else:
    print(cnts[max_cnt][0])

# 범위
print(array[-1] - array[0])
