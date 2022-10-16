import sys
sys.stdin = open("input.txt")

'''
카드 번호를 인덱스로 하는 배열을 만들고
카드 번호가 나올 때마다 해당 인덱스의 값을 +1 하면
번호마다 몇 장씩 있는지 계산된 배열이 나온다.
해당 카운트 배열을 반복문을 통해 순회하며 조건에 만족할 때마다 카운트한다.
'''

for t in range(1, int(input()) + 1):
    ch = [0] * 10
    triplet = run = 0
    cards = input()

    for c in cards:
        cur = int(c)
        ch[cur] += 1

    print(ch)

    i = 0
    # while문과 continue로 triple 또는 run이 2번 나오는 경우를 체크 가능
    while i < 10:
        if ch[i] >= 3:
            ch[i] -= 3
            triplet += 1
            continue

        if i <= len(ch) - 3 and ch[i] >= 1 and ch[i + 1] >= 1 and ch[i + 2] >= 1:
            ch[i] -= 1
            ch[i + 1] -= 1
            ch[i + 2] -= 1
            run += 1
            continue

        i += 1

    if triplet + run == 2:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')
