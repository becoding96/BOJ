import sys

sys.stdin = open("input.txt")

for t in range(int(input())):
    ch = [0] * 10
    n = int(input())
    nums = input()

    # ch 배열에 카드의 숫자를 인덱스로하는 부분을
    # 카드가 나올 때마다 1씩 더해줌
    # ch 배열에 카드가 숫자별로 얼마나 나왔는지 저장됨
    for num in nums:
        ch[int(num)] += 1

    # ch 배열을 탐색하면서 최대 장 수를 탐색
    maxNum = -1
    maxV = 0
    for i, c in enumerate(ch):
        if c >= maxV:
            maxV = c
            maxNum = i

    print(f'#{t + 1} {maxNum} {maxV}')