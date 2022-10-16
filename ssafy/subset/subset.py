arr = [3, 6, 7, 1, 5, 4]
N = len(arr)

# 1 << N: 부분집합의 개수
# 공집합 제외하기 위해선 range안의 0을 1로 교체
for i in range(0, (1 << N)):
    for j in range(0, N):  # 원소의 수만큼 비트를 비교
        if i & (1 << j):  # i의 j번째 비트가 1이면 j번째 원소 출력
            print(f'{arr[j]}', end='')
    print()
