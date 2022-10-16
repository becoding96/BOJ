# 다른 조 풀이, dp 방식
import sys
sys.stdin = open('input.txt')

A = [range(1, 13)]
T = int(input())

for test in range(T):  # 부분집합에 대한 기본정보 입력
    N, K = map(int, input().split())
    subset = [[]]
    cnt = 0

    for i in A:  # 부분집합 생성
        for j in range(len(subset)):  # 갱신되는 subset의 인자 수만큼 추가
            subset.append(subset[j] + [i])

    for k in subset:  # 각 부분집합의 개수와 합으로 조건 확인
        if len(k) == N and sum(k) == K:
            cnt += 1

    if cnt >= 1:
        print(f'#{test + 1} {cnt}')
    else:
        print(f'#{test + 1} 0')