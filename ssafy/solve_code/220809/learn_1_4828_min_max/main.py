import sys

sys.stdin = open("input.txt")

for t in range(int(input())):
    n = int(input())
    array = list(map(int, input().split()))
    minV = 1000001
    maxV = 0

    for a in array:
        minV = a if a < minV else minV
        maxV = a if a > maxV else maxV

    print(f'#{t + 1} {maxV - minV}')