import sys
sys.stdin = open('input.txt')

# 138ms
for T in range(int(input())):
    A, B = input().split()
    A = A.replace(B, ' ')  # B에 해당하는 부분을 한 글자인 ' '으로 바꿔줌
    print(f'#{T + 1} {len(A)}')