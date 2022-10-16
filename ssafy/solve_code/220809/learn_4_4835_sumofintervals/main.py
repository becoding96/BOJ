import sys

sys.stdin = open("input.txt")

for t in range(int(input())):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    s = 0 # 구간의 시작 인덱스
    e = m # 구간의 끝 인덱스 + 1

    # 원소 a: 1 ~ 10000, m: 2 ~ 99
    minV = 10000 * 100
    maxV = 0

    while e <= n:
        array_sum = 0
        for a in array[s: e]:  # s에서 e - 1까지 합을 구함
            array_sum += a
        if array_sum < minV:  # 합이 기존의 최소값보다 작다면 최소값에 저장
            minV = array_sum
        if array_sum > maxV:  # 합이 기존의 최대값보다 크다면 최대값에 저장
            maxV = array_sum
        #  시작과 끝을 오른쪽으로 한 칸씩 이동
        s += 1
        e += 1

    print(f'#{t + 1} {maxV - minV}')