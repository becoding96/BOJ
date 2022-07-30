# 나동빈님 풀이
import heapq

n, m = map(int, input().split())
array = list(map(int, input().split()))
positive = []
negative = []

# 가장 거리가 먼 책까지의 거리
largest = max(max(array), - min(array))

# heappop 함수는 가장 작은 값을 빼내서 리턴하므로
# 최대 힙(Max Heap)을 위해 원소를 음수로 구성
for p in array:
# 책의 위치가 양수인 경우
    if p > 0:
        heapq.heappush(positive, -p)
# 책의 위치가 음수인 경우
    else:
        heapq.heappush(negative, p)

result = 0

while positive:
    # 한 번에 m개씩 옮길 수 있으므로 m번 빼내기
    result += heapq.heappop(positive) # 1번
    for _ in range(m - 1): # m - 1번
        if positive:
            heapq.heappop(positive)

while negative:
    # 한 번에 m개씩 옮길 수 있으므로 m번 빼내기
    result += heapq.heappop(negative) # 1번
    for _ in range(m - 1): # m - 1번
        if negative:
            heapq.heappop(negative)
            
# 일반적으로 왕복 거리를 계산하지만, 가장 먼 곳은 편도 거리 계산
print(abs(result * 2) - largest)