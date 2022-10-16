def comb(n, r):
    if r == 0:
        print(*c)
    elif n < r:
        return
    else:
        c[r - 1] = A[n - 1]  # 오름차순으로 출력하려면 c[-r] = A[-n]
        comb(n - 1, r - 1)
        comb(n - 1, r)


A = list(range(1, 6))
n = len(A)
r = 3
c = [0] * r
comb(n, r)
