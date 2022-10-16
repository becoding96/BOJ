import sys

sys.stdin = open("input.txt")

'''
메모리와 시간을 아끼기 위해
부분 집합을 따로 구하지 않고
부분 집합의 합만 구하는 방식으로 했더니
공집합일 때와 합해서 0이 될 때 구분이 안됐음.
결국 부분 집합을 구해서 길이가 0인지도 확인해야 했음. 
'''

for t in range(int(input())):
    array = list(map(int, input().split()))
    # 출력용 flag
    flag = 0

    # 비트 연산자를 이용해 부분집합을 구함
    for i in range(1, 1 << 10):  # 공집합 제거
        part_sum = 0
        for j in range(10):
            if i & (1 << j):
                part_sum += array[j]
        # 부분집합의 합이 0이면 flag = 1
        if part_sum == 0:
            flag = 1

    # flag 출력
    print(f'{t + 1} {flag}')