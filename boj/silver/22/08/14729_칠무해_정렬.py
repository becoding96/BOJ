# 220820
import sys

N = int(sys.stdin.readline().rstrip())
arr = sorted([float(sys.stdin.readline().rstrip()) for _ in range(N)])
for i in range(7):
    print(f'{arr[i]:.3f}')
