# 0.16281s
import sys
from collections import deque
sys.stdin = open("input.txt")

for T in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))

    arr.sort()  # 오름차순 정렬

    print(f'#{T + 1}', end=" ")  # 테스트 케이스 번호 출력

    q = deque(arr)  # 기존의 리스트를 deque 자료구조로 변환
    cnt = 0
    while q and cnt <= 8:  # q에 자료가 남아있고, 카운트가 8 이하일 때 반복
        print(q.pop(), end=" ")
        cnt += 1
        if q:  # 위에서 한번 뽑고, 하나도 남지 않았을 경우를 대비
            print(q.popleft(), end=" ")
            cnt += 1
    print()