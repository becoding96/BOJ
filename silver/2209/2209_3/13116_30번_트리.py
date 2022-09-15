# 220913
import sys

input = sys.stdin.readline
for _ in range(int(input().rstrip())):
    A, B = map(int, input().split())
    A_B_min = min(A, B)

    set_A = set()
    set_B = set()

    while A >= 1:
        set_A.add(A)
        A //= 2
    
    while B >= 1:
        set_B.add(B)
        B //= 2
        
    print(max(set_A & set_B) * 10)
