# 221022
import sys, heapq; input = sys.stdin.readline

for T in range(int(input().rstrip())):
    k = int(input().rstrip())
    min_q, max_q = [], []
    not_deleted = {}
    for i in range(k):
        oper, n = input().rstrip().split()
        n = int(n)
        if oper == 'I':
            not_deleted[i] = 1
            heapq.heappush(min_q, (n, i))
            heapq.heappush(max_q, (-n, i))
        else:
            if n == -1:
                while min_q and not_deleted[min_q[0][1]] == 0:
                    heapq.heappop(min_q)
                if min_q:
                    not_deleted[min_q[0][1]] = 0
                    heapq.heappop(min_q)
            else:
                while max_q and not_deleted[max_q[0][1]] == 0:
                    heapq.heappop(max_q)
                if max_q:
                    not_deleted[max_q[0][1]] = 0
                    heapq.heappop(max_q)
    
    while min_q and not_deleted[min_q[0][1]] == 0:
        heapq.heappop(min_q)
    while max_q and not_deleted[max_q[0][1]] == 0:
        heapq.heappop(max_q)

    if min_q:
        print(-max_q[0][0], min_q[0][0])
    else:
        print("EMPTY")
