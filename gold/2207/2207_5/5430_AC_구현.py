# 220726
import sys
from collections import deque

for _ in range(int(sys.stdin.readline())):
    p = sys.stdin.readline().rstrip() # 개행문자 제거
    n = int(sys.stdin.readline())
    # rstrip: 개행문자 제거, [1:-1]: 대괄호 제거
    dq = deque(sys.stdin.readline().rstrip()[1:-1].split(',')) # str 요소들을 가지는 리스트를 deque로
    if n == 0: # []가 입력되면 길이 1의 dq = ['']이 되기 때문에 따로 처리
        dq = deque()

    flag = False # dq가 비어있는데 'D'가 나왔는지
    R_cnt = 0 # R이 홀수번 나왔는지, 짝수번 나왔는지
    for i in range(len(p)):
        if p[i] == 'R':
            R_cnt += 1
        elif p[i] == 'D':
            if len(dq) == 0:
                flag = True
                break
            if R_cnt % 2: 
                dq.pop() # 뒤집힌 상태에서 D
            else:
                dq.popleft()

    if flag:
        print('error')
    else:
        if R_cnt % 2:
            dq.reverse()
            # 바로 list(dq)하면 안됨
            print("[" + ",".join(dq) + "]")
        else:
            print("[" + ",".join(dq) + "]")