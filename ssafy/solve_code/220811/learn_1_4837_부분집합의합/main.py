# 0.16375s
import sys
sys.stdin = open("input.txt")

A = list(i for i in range(1, 13))

for T in range(int(input())):
    N, K = map(int, input().split())
    cnt = 0  # 결과 저장할 변수

    for i in range(1, 1 << 12):  # 공집합 제거
        part = []  # 부분 집합 변수
        for j in range(12):
            if i & (1 << j):
                part.append(A[j])
        # 부분집합의 길이가 N이고, 합이 K이면 카운트 증가
        if len(part) == N and sum(part) == K:
            cnt += 1

    print(f'#{T + 1} {cnt}')

