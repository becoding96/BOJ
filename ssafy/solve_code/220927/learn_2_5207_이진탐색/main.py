import sys
sys.stdin = open("sample_input.txt")

for T in range(int(input())):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    result = 0

    for b in B:
        l = 0
        r = N - 1
        state = 0
        b_is_in_A = False
        is_bungal = True
        while l <= r:
            mid = (l + r) // 2
            if b > A[mid]:
                if state == -1 or state == 0:
                    state = 1
                    l = mid + 1
                else:
                    is_bungal = False
                    break
            elif b < A[mid]:
                if state == 1 or state == 0:
                    state = -1
                    r = mid - 1
                else:
                    is_bungal = False
                    break
            elif b == A[mid]:
                b_is_in_A = True
                break
        if is_bungal and b_is_in_A:
            result += 1

    print(f'#{T + 1} {result}')
