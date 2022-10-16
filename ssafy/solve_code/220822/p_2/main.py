def f(i, N, cumulated, T):                      # 누적 배열 cumulated, 찾고자하는 값 T
    if sum(cumulated) > T:                      # 프루닝(가지치기)
        return

    if i == N:                                  # 모든 원소가 고려된 경우
        if sum(cumulated) == T:                 # 부분집합의 합이 T면
            print(*cumulated)
        return
    else:
        cumulated.append(A[i])
        f(i + 1, N, cumulated, T)               # A[i]가 포함된 경우
        cumulated.pop()
        f(i + 1, N, cumulated, T)               # A[i]가 포함되지 않은 경우


A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
f(0, 10, list(), 10)
