# 220917

'''
N = 3(2 ** N = 8) 에서 8행 7열은?
첫 번째 Z에서 4번째 => (4(현재 크기의 반) ** 2) * 3(행과 열 못 넘기면 0, 열만 넘기면 1, 행만 넘기면 2, 행 열 넘기면 3)
두 번째 Z(첫 번째 큰 Z에서의 4번째 부분)에서는 4행 3열 => (2 ** 2) * 3
(왜 4행 3열? -> 행과 열에서 각각 현재 Z 크기의 반을 넘는다면 그만큼 뺀다) 
세 번째 Z에서는 2행 1열 => (1 ** 2) * 2
48 + 12 + 2 = 62
'''

import sys


# 현재 Z에서 몇 번째 부분인지 판별하는 함수
def where(half_size, row, col):  
    if row > half_size and col > half_size:
        return 3  # Z를 왼쪽 위부터 그릴 때 4번째 부분
    elif row > half_size:
        return 2  # 3번
    elif col > half_size:
        return 1  # 2번
    else:
        return 0  # 1번


N, r, c = map(int, sys.stdin.readline().split())
size = 2 ** N
r, c = r + 1, c + 1  # ! 0번부터 입력되므로 ! 조정
result = 0

while size >= 2:
    w = where(size // 2, r, c)
    result += ((size // 2) ** 2) * w
    # 한 단계 작은 Z에서는 몇 행 몇 열인지 찾기
    if w == 3:
        r -= size // 2
        c -= size // 2
    elif w == 2:
        r -= size // 2
    elif w == 1:
        c -= size // 2
    size //= 2  # 애초에 반으로 나누고 반복문 진행해도 되지만 의미상 현재의 Z 크기를 나타내기 위해
    
print(result)
