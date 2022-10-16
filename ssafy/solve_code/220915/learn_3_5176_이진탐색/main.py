import sys
sys.stdin = open("input.txt")

def inorder(arr, i, N):
    global v
    if i <= N:
        inorder(arr, i * 2, N)
        if arr[i] == 0:
            arr[i] = v
            v += 1
        inorder(arr, i * 2 + 1, N)

for T in range(int(input())):
    N = int(input())
    arr = [0] * (N + 1)
    v = 1
    inorder(arr, 1, N)
    print(f'#{T + 1}', arr[1], arr[N // 2])