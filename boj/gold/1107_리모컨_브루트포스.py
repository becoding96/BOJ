# 220918

'''
채널은 0부터 500000까지

타겟 숫자부터 양쪽으로 포인터 이동

ex)
N = 5457

5457 - 1 = 5456 => 6안됨
5457 + 1 = 54585 => 8안됨

5455 => 가능, ++
5459 => 가능, --
'''

import sys

input = sys.stdin.readline
N = int(input().rstrip())
M = int(input().rstrip())
if M == 0:  # 고장난 버튼이 없는 경우
    print(min(len(str(N)), abs(N - 100)))
    exit()
broken = list(map(int, input().split()))
pointer = 0
result = abs(N - 100)

while pointer <= abs(N - 100):
    left, right = N - pointer, N + pointer
    left = left if left > 0 else 0

    for digit in str(left):
        if int(digit) in broken:
            break
    else:
        result = len(str(left)) + pointer
        break

    for digit in str(right):
        if int(digit) in broken:
            break
    else:
        result = len(str(right)) + pointer
        break

    pointer += 1

print(min(result, abs(N - 100)))
