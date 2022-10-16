import sys

sys.stdin = open("input.txt")

for t in range(10):
    n = int(input())
    array = list(map(int, input().split()))
    cnt = [0] * 101
    maxV = array[0]
    minV = array[0]

    # 상자 높이의 최대, 최소 값을 구함
    for a in array:
        cnt[a] += 1
        maxV = a if a > maxV else maxV
        minV = a if a < minV else minV

    for _ in range(n):
        # 최대 높이와 최소 높이 차이가 1 이하이면
        # 덤프의 의미가 없으므로 break
        if maxV - minV <= 1:
            break

        # 최대 높이의 상자를 하나 뺌
        if cnt[maxV] == 1:
            cnt[maxV] -= 1
            maxV -= 1
            cnt[maxV] += 1
        else:
            cnt[maxV] -= 1
            cnt[maxV - 1] += 1

        # 최소 높이의 상자에 얹음
        if cnt[minV] == 1:
            cnt[minV] -= 1
            minV += 1
            cnt[minV] += 1
        else:
            cnt[minV] -= 1
            cnt[minV + 1] += 1

    print(f'#{t + 1} {maxV - minV}')




