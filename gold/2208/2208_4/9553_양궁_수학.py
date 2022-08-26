import math, sys

def rad(point):  
    if point[0] > 0 and point[1] == 0:
        return 0
    elif point[0] > 0 and point[1] > 0:
        return math.atan(point[1] / point[0])
    elif point[0] == 0 and point[1] > 0:
        return math.pi / 2
    elif point[0] < 0 and point[1] > 0:
        return math.pi + math.atan(point[1] / point[0])
    elif point[0] < 0 and point[1] == 0:
        return math.pi
    elif point[0] < 0 and point[1] < 0:
        return math.pi + math.atan(point[1] / point[0])
    elif point[0] == 0 and point[1] < 0:
        return 3 / 2 * math.pi
    elif point[0] > 0 and point[1] < 0:
        return 2 * math.pi + math.atan(point[1] / point[0])
    

input = sys.stdin.readline
for _ in range(int(input().rstrip())):
    N = int(input().rstrip())
    rad_sum = 0
    for _ in range(N):
        x1, y1, x2, y2 = map(int, input().split())
        if (x1 == 0 and y1 == 0) or (x2 == 0 and y2 == 0):
            continue
        angle = abs(rad((x1, y1)) - rad((x2, y2)))
        if angle > math.pi:
            angle = 2 * math.pi - angle
        if angle == math.pi:
            continue
        rad_sum += abs(angle)
    print(f'{round(rad_sum / (2 * math.pi), 5):.5f}')
