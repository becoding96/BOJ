# 220820
import sys

input = sys.stdin.readline
for _ in range(int(input().rstrip())):
    N = int(input().rstrip())
    arr1 = sorted(list(map(int, input().split())))
    M = int(input().rstrip())
    arr2 = list(map(int, input().split()))

    for x in arr2:
        result = 0
        s = 0
        e = N - 1
        while s <= e:
            mid = (s + e) // 2
            cur = arr1[mid]
            if cur > x:
                e = mid - 1
            elif cur < x:
                s = mid + 1
            else:
                result = 1
                break
        sys.stdout.write(str(result) + '\n')
