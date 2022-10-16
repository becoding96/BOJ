# 220715
n = int(input())
point_list = []
for i in range(n):
    x, y = map(int, input().split())
    point_list.append([x, y])

point_list.sort(key = lambda p: (p[0], p[1]))  # lambda 정렬

for i in range(n):
    print(point_list[i][0], point_list[i][1])