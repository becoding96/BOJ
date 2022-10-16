arr = [3, 6]

n = len(arr)

for i in range(1 << n):  # 1 << n: 부분 집합의 개수
    sum = 0
    for j in range(n):  # 원소의 수 만큼 비트를 비교
        if i & (1 << j):  # i의 j번 비트가 1인 경우
            print(arr[j], end = " ")  # j번 원소 출력
            sum += arr[j]
    print()
    print("sum: " + str(sum))
