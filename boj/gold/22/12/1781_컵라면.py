# 221201

'''
데드라인 기준으로 오름차순 정렬
우선순위 큐에 컵라면 수를 넣음
우선순위 큐의 길이가 현재 시간이므로
새로들어온 문제의 데드라인이 현재 시간보다 이전이라면
힙큐에서 pop해야함!! => 최소힙큐이므로 컵라면 개수가 작은 문제가 빠져나감
'''

import heapq, sys; input = sys.stdin.readline

N = int(input().rstrip())
problems = sorted([tuple(map(int, input().split())) for _ in range(N)])
solved = []

for prob in problems:
    heapq.heappush(solved, prob[1])
    if prob[0] < len(solved):
        heapq.heappop(solved)

print(sum(solved))
