# 220805
import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())  # 입력이 한 줄에 끝나므로 rstrip() 필요 없는 듯
q = deque(list(range(1, n + 1)))
result = deque()
cnt = 1

while q:
    for _ in range(k - 1):
        q.append(q.popleft())
    result.append(q.popleft())

print('<' + str(list(result)).lstrip('[').rstrip(']') + '>')
