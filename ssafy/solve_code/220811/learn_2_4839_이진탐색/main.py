# 0.13287s
import sys
sys.stdin = open("input.txt")

# 이진 탐색 몇 번만에 원하는 값을 찾았는지 카운트해주는 함수
def count(total_pages, target_page):
    l = 1
    r = total_pages
    cnt = 1
    while l <= r:
        c = (l + r) // 2
        if c == target_page:
            return cnt
        if c > target_page:
            r = c
        elif c < target_page:
            l = c
        cnt += 1

for T in range(int(input())):
    P, Pa, Pb = map(int, input().split())

    # 카운트가 적은 쪽을 출력, 비기면 result가 변하지 않으므로 0 출력
    result = 0
    if count(P, Pa) < count(P, Pb):
        result = 'A'
    elif count(P, Pa) > count(P, Pb):
        result = 'B'

    print(f'#{T + 1} {result}')

