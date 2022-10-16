# 220820

'''
좁은 조건을 더 위에 써줘야 함!
'''

import sys


def check(points):
    x1, y1, p1, q1, x2, y2, p2, q2 = points

    if p1 < x2 or q1 < y2 or p2 < x1 or q2 < y1:
        return 'd'

    if (
        (p1 == x2 and q1 == y2) or
        (x1 == p2 and q1 == y2) or
        (x1 == p2 and y1 == q2) or
        (p1 == x2 and y1 == q2)
    ):
        return 'c'

    if y1 == q2 or x1 == p2 or q1 == y2 or p1 == x2:
        return 'b'

    return 'a'


input = sys.stdin.readline
for _ in range(4):
    points = list(map(int, input().split()))
    print(check(points))
