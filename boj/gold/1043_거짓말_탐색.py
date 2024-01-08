# 221028
import sys; input = sys.stdin.readline

N, M = map(int, input().split())
t_n, *t_set = map(int, input().split())
if t_n == 0: print(M); exit()
t_set = set(t_set)

h_board = []
for i in range(M):
    h_n, *h_set = map(int, input().split())
    h_set = set(h_set)
    h_board.append(h_set)

result = M
check = [0] * (M)
flag = True
while flag:
    flag = False
    for i in range(M):
        if check[i]:
            continue
        if t_set & h_board[i]:
            t_set = t_set | h_board[i]
            result -= 1
            check[i] = 1
            flag = True
    
print(result)
