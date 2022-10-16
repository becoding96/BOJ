import sys

sys.stdin = open("input.txt")

'''
현재 인덱스의 아파트 꼭대기에서 내려오면서
층마다 양옆 2개 아파트 층이 있는지 층 단위로 비교하면
시간이 너무 오래 걸릴 가능성이 높다.
양옆 2개 아파트 높이의 최대값을 구해서
현재 아파트 높이에서 뺐을 때 양수면
해당 수치만큼 카운트하는 방식으로 시간을 단축할 수 있다.

152ms
'''

for t in range(1, 11):
    n = int(input())
    apts = list(map(int, input().split()))
    cnt = 0

    side = [-2, -1, 1, 2]  # side: 비교용 리스트, 양 옆 총 4개의 아파트
    for i in range(2, n - 2):
        maxV = 0
        for j in side:  # 양옆 총 4개의 아파트 높이의 최대값 구함
            if maxV < apts[i + j]:
                maxV = apts[i + j]
        # 현재 아파트 높이에서 양옆 총 4개의 아파트 높이의 최대값 뺀 만큼 카운트에 더함
        if apts[i] - maxV > 0:
            cnt += apts[i] - maxV

    print(f'#{t} {cnt}')
