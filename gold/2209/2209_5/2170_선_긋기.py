# 220927

'''
입력받은 (x, y)들의 리스트를 x 기준으로 정렬
스택 생성, 스택에 리스트의 첫 x, y를 넣어놓음
스택 최상단을 t라 하고, 리스트를 순회하며 넣을지 판단할 x, y를 a, b라 하면
a가 t보다 작거나 같고, b가 t보다 크면 t를 pop()하고 b를 append
a가 t보다 작거나 같고, b가 t보다 작거나 같으면 놔둠
a가 t보다 크면 a, b 둘 다 append
나중에 pop하면서 계속 빼면 겹친 선분들을 제외한 선분의 길이를 계산 가능
'''

import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
points = sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda x: x[0])
result = 0

stack = deque([points[0][0], points[0][1]])
for i in range(1, N):
    if points[i][0] <= stack[-1] and points[i][1] > stack[-1]:
        stack.pop()
        stack.append(points[i][1])
    elif points[i][0] > stack[-1]:
        stack.append(points[i][0])
        stack.append(points[i][1])

while stack:
    y = stack.pop()
    x = stack.pop()
    result += y - x

print(result)
