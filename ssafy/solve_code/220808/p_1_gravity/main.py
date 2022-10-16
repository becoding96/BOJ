import sys
sys.stdin = open("input.txt")

'''
막대의 끝 부분에서 낙하 거리가 최대이다.
앞 부분은 길이가 더 짧은 막대들에 의해 낙하 거리가 줄어들기 때문이다.
막대마다 자신보다 이후에 나오면서, 길이가 짧은 막대의
개수를 카운트 해주면 낙하 거리가 나온다.
위치에 따라 낙하 거리가 달라지지 않냐는 의문이 생길 수 있지만,
인덱스가 증가하면서 카운트 기회도 줄어들기 때문에
(이후에 나오는 막대만 계산하기 때문에)
해당 과정도 이미 계산에 포함되어 있다.
'''

for t in range(1, int(input().rstrip()) + 1):
    n = int(input().rstrip())
    array = list(map(int, input().rstrip().split()))
    result = 0

    for i in range(n):
        cnt = 0
        for j in range(i + 1, n):
            if array[i] > array[j]:
                cnt += 1

        if cnt > result:
            result = cnt

    print(f'#{t} {result}')
